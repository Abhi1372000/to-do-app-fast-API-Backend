from fastapi import APIRouter
from config.models import add_task_to_db


protected_router = APIRouter()


@protected_router.post("/api/add_task")
async def add_task():
    add_task_to_db()
    return {"message": "task added"}


@protected_router.get("/api/get_tasks")
async def get_task():
    return {"message" : "this are the tasks"}
