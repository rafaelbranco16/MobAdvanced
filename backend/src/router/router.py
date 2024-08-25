from fastapi import APIRouter
from src.loaders.loader import loader
from src.controllers.ai_controller import AIController
from src import config

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
    
    @router.get("/class/question")
    async def class_question(question, class_name):
        ai_controller:AIController = loader.resolve("AIController")
        return await ai_controller.class_question(question, class_name)
    
    @router.get("/document/add")
    async def add_document_to_RAG(file_name):
        ai_controller:AIController = loader.resolve(config.ai_controller["name"])
        return await ai_controller.add_document_to_RAG(file_name)
