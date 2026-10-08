from app.agents.planner import PlannerAgent
from app.agents.architect import ArchitectAgent
from app.agents.coder import CoderAgent
from app.agents.tester import TesterAgent
from app.agents.debugger import DebuggerAgent
from app.agents.security import SecurityAgent
from app.agents.deployer import DeployerAgent


def get_agents():

    return {
        "planner": PlannerAgent(),
        "architect": ArchitectAgent(),
        "coder": CoderAgent(),
        "tester": TesterAgent(),
        "debugger": DebuggerAgent(),
        "security": SecurityAgent(),
        "deployer": DeployerAgent()
    }
