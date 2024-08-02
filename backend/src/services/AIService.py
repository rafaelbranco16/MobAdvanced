from src.rag.RAG import RAG
from langchain_community.document_loaders import DirectoryLoader

class AIService:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.rag = RAG()

    def get_random_build(self):
        return {"message":"This is a random build"}
    
    '''
    Insert a file into the AI RAG
    '''
    def insert_document_content(self, file_name):
        loader:DirectoryLoader = DirectoryLoader("files/AI_feed_documents/" + file_name)
        docs = loader.load()
        print(docs)