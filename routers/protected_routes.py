from fastapi import APIRouter
from config.models import add_task_to_db

protected_router = APIRouter()


@protected_router.post("/api/add_task")
async def add_task():
    add_task_to_db()
    return {"message": "This is serv1"}
