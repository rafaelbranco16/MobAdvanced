from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import router, documents_router
from src.config import config

app = FastAPI()
app.include_router(router.router)
app.include_router(documents_router.document_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[config["react_app_url"]],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def start():
    return {"message": "default"}