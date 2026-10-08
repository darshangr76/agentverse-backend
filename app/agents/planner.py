from app.agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("planner")

    def run(self, state):

        state.agents["planner"] = "working"
        state.status = "planning"

        state.log(
            "planner",
            "Planner agent started analyzing the requirement."
        )

        requirement = state.requirement

        state.plan = {
            "project_goal": requirement,
            "requirements": [
                "Understand the user requirement",
                "Design the application architecture",
                "Create source code",
                "Create tests",
                "Run tests",
                "Fix failures",
                "Validate security",
                "Prepare deployment"
            ],
            "development_phases": [
                "planning",
                "architecture",
                "coding",
                "testing",
                "debugging",
                "security",
                "deployment"
            ]
        }

        state.tasks = [
            {
                "id": "TASK-001",
                "description": "Analyze requirements",
                "assigned_to": "planner",
                "status": "completed"
            },
            {
                "id": "TASK-002",
                "description": "Design application architecture",
                "assigned_to": "architect",
                "status": "pending"
            },
            {
                "id": "TASK-003",
                "description": "Implement application",
                "assigned_to": "coder",
                "status": "pending"
            },
            {
                "id": "TASK-004",
                "description": "Create and run tests",
                "assigned_to": "tester",
                "status": "pending"
            }
        ]

        state.agents["planner"] = "completed"

        state.log(
            "planner",
            "Requirement analysis completed and tasks created."
        )

        return state
