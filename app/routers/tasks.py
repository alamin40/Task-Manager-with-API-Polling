from fastapi import APIRouter, HTTPException
from app.schemas.task_schema import Task, TaskCreate
from app.services import task_service

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
async def get_tasks():
    return await task_service.get_all_tasks()

@router.post("/tasks", response_model=int)
async def create_task(task: TaskCreate):
    return await task_service.create_task(task)

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, completed: bool):
    task = await task_service.update_task(task_id, completed)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "Task updated"}