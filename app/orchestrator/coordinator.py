import uuid
import time
import httpx

from app.orchestrator.state import ProjectState
from app.agents.registry import get_agents

SWARM_API = "http://localhost:4000"


class Orchestrator:

    def __init__(self):
        self.projects = {}
        self.agents = get_agents()

    def create_project(self, requirement: str):

        project = ProjectState()

        project.project_id = str(uuid.uuid4())
        project.requirement = requirement

        project.log(
            "orchestrator",
            "New software engineering project created."
        )

        self.projects[project.project_id] = project

        return project

    def start_planning(self, project_id: str):

        project = self.projects.get(project_id)

        if not project:
            raise ValueError("Project not found")

        self.agents["planner"].run(project)
        self.agents["architect"].run(project)

        return project

    def start_project(self, project_id: str):

        project = self.projects.get(project_id)

        if not project:
            raise ValueError("Project not found")

        project.log(
            "orchestrator",
            "Delegating to Node.js multi-agent core at " + SWARM_API
        )

        # Step 1: Local planner + architect (fast mock)
        self.agents["planner"].run(project)
        self.agents["architect"].run(project)

        # Step 2: Call the real Node.js swarm
        try:
            with httpx.Client(timeout=900.0) as client:

                resp = client.post(
                    f"{SWARM_API}/api/swarm/run",
                    json={"requirement": project.requirement}
                )
                resp.raise_for_status()

                run_id = resp.json()["runId"]

                project.log(
                    "orchestrator",
                    f"Swarm run started with id: {run_id}"
                )

                last_log_count = 0
                iterations = 0
                max_wait_seconds = 600
                start_time = time.time()

                while True:
                    time.sleep(3)
                    iterations += 1

                    if time.time() - start_time > max_wait_seconds:
                        project.log(
                            "orchestrator",
                            "Swarm timed out after 10 minutes."
                        )
                        project.status = "failed"
                        break

                    result = client.get(
                        f"{SWARM_API}/api/swarm/result/{run_id}"
                    )
                    result.raise_for_status()
                    data = result.json()

                    # Sync new log lines into project
                    for entry in data["logs"][last_log_count:]:
                        project.log("swarm", entry)

                    last_log_count = len(data["logs"])

                    status = data.get("status", "UNKNOWN")

                    # Map swarm status to backend agent states
                    if status == "PLANNING":
                        project.agents["planner"] = "working"
                    elif status == "CODING":
                        project.agents["planner"] = "completed"
                        project.agents["architect"] = "completed"
                        project.agents["coder"] = "working"
                    elif status == "TESTING":
                        project.agents["coder"] = "completed"
                        project.agents["tester"] = "working"
                    elif status == "FIXING":
                        project.agents["tester"] = "completed"
                        project.agents["debugger"] = "working"
                    elif status == "DONE":
                        project.agents["planner"] = "completed"
                        project.agents["architect"] = "completed"
                        project.agents["coder"] = "completed"
                        project.agents["tester"] = "completed"
                        project.agents["debugger"] = "completed"
                        project.agents["security"] = "completed"
                        project.agents["deployer"] = "completed"

                        project.generated_files = data.get("files", {})

                        project.status = "completed"

                        project.log(
                            "orchestrator",
                            f"Swarm completed. {len(project.generated_files)} files generated."
                        )
                        break

                    project.status = status.lower()

        except Exception as e:
            project.log(
                "orchestrator",
                f"Swarm call failed: {e}"
            )
            project.status = "failed"

        return project

    def get_project(self, project_id: str):

        return self.projects.get(project_id)
