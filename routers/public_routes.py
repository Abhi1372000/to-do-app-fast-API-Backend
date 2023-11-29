from fastapi import APIRouter, Form
from responses import responses

public_router = APIRouter()


@public_router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):

    if not username or not password:
        content_res = responses["422"]
        content_res["message"] = "Both username and password are required"
        return content_res
    content_res = responses["200"]
    content_res["message"] = "login successfull"
    return content_res


@public_router.post("/register")
async def register(username: str = Form(...), password: str = Form(...),
                   name: str = Form(...), occupation: str = Form(...)):

    if not username or not password or not name or not occupation:
        content_res = responses["422"]
        content_res["message"] = "Both username and password are required"
        return content_res

    content_res = responses["200"]
    content_res["message"] = "registration successfull"
    return content_res
