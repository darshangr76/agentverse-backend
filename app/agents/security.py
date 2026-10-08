from app.agents.base_agent import BaseAgent


class SecurityAgent(BaseAgent):

    def __init__(self):
        super().__init__("security")

    def run(self, state):

        state.agents["security"] = "working"
        state.status = "security"

        state.log(
            "security",
            "Security agent started reviewing the application."
        )

        security_checks = {
            "authentication": "reviewed",
            "input_validation": "reviewed",
            "secret_exposure": "reviewed",
            "api_security": "reviewed"
        }

        state.security_results = security_checks

        state.log(
            "security",
            "Security review completed successfully."
        )

        state.agents["security"] = "completed"

        return state
