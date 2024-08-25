from src.loaders import loader
from src.services.ai_service import AIService


class AIController:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.ai_service:AIService = loader.loader.resolve("AIService")

    def get_random_build(self):
        return self.ai_service.get_random_build()
    
    def insert_document_content(self, file_name):
        return self.ai_service.insert_document_content(file_name)
    
    async def class_question(self, question:str, class_name:str):
        return await self.ai_service.class_question(question, class_name)
    
    async def add_document_to_RAG(self, file_name):
        return await self.ai_service.add_document_to_RAG(file_name)