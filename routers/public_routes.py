from fastapi import APIRouter, Form, HTTPException

public_router = APIRouter()


@public_router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):

    if not username or not password:
        error_message = {
            "status": "login failed",
            "message": "Both username and password are required"
        }
        raise HTTPException(status_code=422, detail=error_message)

    return {"status": "login successfull"}


@public_router.post("/register")
async def register(username: str = Form(...), password: str = Form(...),
                   name: str = Form(...), occupation: str = Form(...)):

    if not username or not password or not name or not occupation:
        error_message = {
            "status": "login failed",
            "message": "Both username and password are required"
        }
        raise HTTPException(status_code=422, detail=error_message)
    print(username, password, occupation, name)

    return {"status": "registered successfull"}
