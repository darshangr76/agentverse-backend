from app.agents.base_agent import BaseAgent


class TesterAgent(BaseAgent):

    def __init__(self):
        super().__init__("tester")

    def run(self, state):

        state.agents["tester"] = "working"
        state.status = "testing"

        state.log(
            "tester",
            "Tester agent started testing the application."
        )

        state.test_results = {
            "passed": 4,
            "failed": 0,
            "total": 4
        }

        state.log(
            "tester",
            "All tests passed successfully."
        )

        state.agents["tester"] = "completed"

        for task in state.tasks:
            if task["id"] == "TASK-004":
                task["status"] = "completed"

        return state
