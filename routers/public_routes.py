from fastapi import APIRouter

public_router = APIRouter()


@public_router.post("/login")
async def login():
    return {"message": "This is login"}
