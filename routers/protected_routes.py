from fastapi import APIRouter
from controller.adding_task import add_task_to_user
from fastapi.responses import JSONResponse
from error_responses import responses

protected_router = APIRouter()


@protected_router.post("/api/add_task")
async def add_task():
    result = await add_task_to_user()
    if result is False:
        content_res = responses["400"]["message"] = "data is not updated"
        return JSONResponse(status_code=400, content=content_res)
    return {"message": "task added"}


@protected_router.get("/api/get_tasks")
async def get_task():
    return {"message" : "this are the tasks"}
