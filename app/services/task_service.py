from app.models.task_model import tasks
from app.database import database
from app.schemas.task_schema import TaskCreate

async def create_task(task: TaskCreate):
    query = tasks.insert().values(title=task.title, description=task.description, completed=False)
    task_id = await database.execute(query)
    return task_id

async def get_all_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


