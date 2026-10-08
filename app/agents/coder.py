from app.agents.base_agent import BaseAgent


class CoderAgent(BaseAgent):

    def __init__(self):
        super().__init__("coder")

    def run(self, state):

        state.agents["coder"] = "working"
        state.status = "coding"

        state.log(
            "coder",
            "Coder agent started implementing the application."
        )

        state.log(
            "coder",
            "Coder agent reviewed the project architecture."
        )

        state.log(
            "coder",
            "Application implementation completed."
        )

        state.agents["coder"] = "completed"

        for task in state.tasks:
            if task["id"] == "TASK-003":
                task["status"] = "completed"

        return state
