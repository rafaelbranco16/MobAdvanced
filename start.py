from fastapi import FastAPI
from backend.src.router import router
from injector import Injector

app = FastAPI()
app.include_router(router.router)

@app.get("/")
async def start():
    return {"message": "default"}