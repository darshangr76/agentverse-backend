from typing import Dict, List, Any
from datetime import datetime


class ProjectState:

    def __init__(self):

        self.project_id = None
        self.requirement = None
        self.status = "created"

        self.plan = {}
        self.architecture = {}

        self.tasks: List[Dict[str, Any]] = []

        self.agents = {
            "planner": "waiting",
            "architect": "waiting",
            "coder": "waiting",
            "tester": "waiting",
            "debugger": "waiting",
            "security": "waiting",
            "deployer": "waiting"
        }

        self.test_results = {
            "passed": 0,
            "failed": 0,
            "total": 0
        }

        self.security_results = {}

        self.generated_files: Dict[str, str] = {}

        self.logs = []

    def log(self, agent: str, message: str):

        self.logs.append({
            "time": datetime.now().isoformat(),
            "agent": agent,
            "message": message
        })

    def to_dict(self):

        return {
            "project_id": self.project_id,
            "requirement": self.requirement,
            "status": self.status,
            "plan": self.plan,
            "architecture": self.architecture,
            "tasks": self.tasks,
            "agents": self.agents,
            "test_results": self.test_results,
            "security_results": self.security_results,
            "generated_files": self.generated_files,
            "logs": self.logs
        }
