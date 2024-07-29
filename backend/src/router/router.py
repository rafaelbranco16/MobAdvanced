from fastapi import APIRouter
from src.loaders.loader import loader
from src.controller.AIController import AIController

router = APIRouter()

class Router:
    @router.get("/builds/get_random_build")
    async def get_random_build():
        ai_controller:AIController = loader.resolve("AIController")
        return ai_controller.get_random_build()
    
    @router.get("/insert/document")
    async def insert_document():
        ai_controller:AIController = loader.resolve("AIController")
        return ai_controller.insert_document_content()
