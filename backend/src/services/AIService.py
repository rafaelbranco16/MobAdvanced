from src.rag.RAG import RAG

class AIService:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.rag = RAG()

    def get_random_build(self):
        return {"message":"This is a random build"}
    
    def insert_document_content(self):
        if(self.rag is not any):
            return {"message": "The RAG was successfully created."}