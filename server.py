import uvicorn

from fastapi import FastAPI

from routers.public_routes import public_router
from routers.protected_routes import protected_router

app = FastAPI()


@app.get("/check")
def hell_check() -> dict:
    return {"Hello": "World"}


app.include_router(public_router, prefix="/api")
app.include_router(protected_router, prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
