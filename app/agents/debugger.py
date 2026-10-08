from app.agents.base_agent import BaseAgent


class DebuggerAgent(BaseAgent):

    def __init__(self):
        super().__init__("debugger")

    def run(self, state):

        state.agents["debugger"] = "working"
        state.status = "debugging"

        state.log(
            "debugger",
            "Debugger agent started analyzing test results."
        )

        failed_tests = state.test_results["failed"]

        if failed_tests > 0:
            state.log(
                "debugger",
                f"Found {failed_tests} failed test(s). Debugging required."
            )
            state.status = "debugging"
        else:
            state.log(
                "debugger",
                "No test failures found. Debugging is not required."
            )
            state.status = "testing"

        state.agents["debugger"] = "completed"

        return state
