from app.agents.base_agent import BaseAgent


class DeployerAgent(BaseAgent):

    def __init__(self):
        super().__init__("deployer")

    def run(self, state):

        state.agents["deployer"] = "working"
        state.status = "deployment"

        state.log(
            "deployer",
            "Deployment agent started preparing the application."
        )

        deployment_result = {
            "environment": "local",
            "status": "ready",
            "deployment_type": "local development"
        }

        state.log(
            "deployer",
            "Application deployment preparation completed."
        )

        state.agents["deployer"] = "completed"
        state.status = "completed"

        return state
