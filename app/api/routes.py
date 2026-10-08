from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.orchestrator.coordinator import Orchestrator


router = APIRouter()

orchestrator = Orchestrator()


class RequirementRequest(BaseModel):
    requirement: str


@router.get("/")
def home():

    return {
        "message": "Autonomous AI Engineering Team Backend",
        "status": "running"
    }


@router.post("/projects")
def create_project(request: RequirementRequest):

    if not request.requirement.strip():
        raise HTTPException(
            status_code=400,
            detail="Requirement cannot be empty"
        )

    project = orchestrator.create_project(
        request.requirement
    )

    return {
        "message": "Project created",
        "project": project.to_dict()
    }


@router.post("/projects/{project_id}/plan")
def start_planning(project_id: str):

    try:

        project = orchestrator.start_planning(
            project_id
        )

        return {
            "message": "Planning completed",
            "project": project.to_dict()
        }

    except ValueError:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


@router.post("/projects/{project_id}/run")
def run_project(project_id: str):

    try:

        project = orchestrator.start_project(
            project_id
        )

        return {
            "message": "Autonomous engineering workflow completed",
            "project": project.to_dict()
        }

    except ValueError:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )


@router.get("/projects/{project_id}")
def get_project(project_id: str):

    project = orchestrator.get_project(
        project_id
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project.to_dict()
