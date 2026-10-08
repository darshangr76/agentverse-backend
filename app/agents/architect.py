from app.agents.base_agent import BaseAgent


class ArchitectAgent(BaseAgent):

    def __init__(self):
        super().__init__("architect")

    def run(self, state):

        state.agents["architect"] = "working"
        state.status = "architecture"

        state.log(
            "architect",
            "Architect agent started designing the system."
        )

        requirement = state.requirement

        state.architecture = {
            "project_type": "web application",
            "frontend": {
                "technology": "HTML, CSS, JavaScript",
                "responsibility": "User interface"
            },
            "backend": {
                "technology": "Python FastAPI",
                "responsibility": "Business logic and REST APIs"
            },
            "database": {
                "technology": "SQLite",
                "responsibility": "Store application data"
            },
            "api": {
                "style": "REST API",
                "endpoints": [
                    "POST /login",
                    "POST /students",
                    "POST /attendance",
                    "GET /attendance/report"
                ]
            },
            "project_requirement": requirement
        }

        state.agents["architect"] = "completed"

        state.log(
            "architect",
            "System architecture designed successfully."
        )

        for task in state.tasks:
            if task["id"] == "TASK-002":
                task["status"] = "completed"

        return state
