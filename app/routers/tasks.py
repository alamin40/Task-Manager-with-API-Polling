from fastapi import APIRouter, HTTPException
from app.schemas.task_schema import Task, TaskCreate
from app.services import task_service

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
async def get_tasks():
    return await task_service.get_all_tasks()