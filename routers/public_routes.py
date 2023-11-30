from fastapi import APIRouter, Form
from responses import responses
from controller.auth.login import login_auth
from controller.auth.register import register_to_db

public_router = APIRouter()


@public_router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):

    authrized_user = await login_auth(username, password)

    if authrized_user["authrized"] is not True:
        content_res = responses["401"]
        content_res["message"] = "user unauthrized"
        return content_res

    content_res = responses["200"]
    content_res["message"] = "login successfull"
    content_res["data"] = {"token": authrized_user["token"]}
    return content_res


@public_router.post("/register")
async def register(username: str = Form(...), password: str = Form(...),
                   name: str = Form(...), occupation: str = Form(...)):

    user_registration = await register_to_db(username, password, name, occupation)
    if not username or not password or not name or not occupation:
        content_res = responses["422"]
        content_res["message"] = "Both username and password are required"
        return content_res

    content_res = responses["200"]
    content_res["message"] = "registration successfull"
    return content_res
