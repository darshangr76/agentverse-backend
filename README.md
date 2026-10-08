# Autonomous AI Engineering Team - Backend

This folder contains the FastAPI backend for the Autonomous AI Engineering Team project.

## Main parts

- FastAPI API
- Project creation and project state
- Agent registry
- Multi-agent orchestrator
- Planner
- Architect
- Coder
- Tester
- Debugger
- Security
- Deployer

## Run

Create/activate a Python virtual environment and install:

    python -m pip install -r requirements.txt

Start the backend:

    python -m uvicorn app.main:app --reload

API:

    http://127.0.0.1:8000

Swagger:

    http://127.0.0.1:8000/docs

## API flow

1. POST /projects
2. POST /projects/{project_id}/plan
3. POST /projects/{project_id}/run
4. GET /projects/{project_id}

## Integration note

The `app/agents/registry.py` file is the main integration point for replacing the placeholder agents with the team's actual AI agents.

The orchestrator accesses agents through:

    self.agents["planner"]
    self.agents["architect"]
    self.agents["coder"]
    self.agents["tester"]
    self.agents["debugger"]
    self.agents["security"]
    self.agents["deployer"]

The current backend stores project state in memory, so restarting the server clears active projects.
