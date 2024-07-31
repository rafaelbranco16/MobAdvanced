from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import router, documents_router
from src.config import config

app = FastAPI()
app.include_router(router.router)
app.include_router(documents_router.document_router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def start():
    return {"message": "default"}