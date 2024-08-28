from src.loaders import loader
from src.services.ai_service import AIService


class AIController:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.ai_service:AIService = loader.loader.resolve("AIService")

    async def get_random_build(self):
        raise NotImplementedError()
    
    async def class_question(self, question:str, class_name:str):
        try:
            return await self.ai_service.class_question(question, class_name)
        except Exception as e:
            return {"message": str(e)}
    
    '''
    Add a new document to the RAG
    
    '''
    async def add_document_to_RAG(self, file_name):
        response = await self.ai_service.add_document_to_RAG(file_name)
        print(response)
        return response