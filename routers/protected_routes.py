from fastapi import APIRouter

protected_router = APIRouter()


@protected_router.post("/api/serv1")
async def serv1():
    return {"message": "This is serv1"}
