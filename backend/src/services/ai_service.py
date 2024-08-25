from src.rag.RAG import RAG
from langchain_community.document_loaders import DirectoryLoader
from src.loaders import loader
from src.adapters.llm_adapter import LLMAdapter
from langchain_core.documents import Document



class AIService:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.rag = RAG()
        self.llm_adapter:LLMAdapter = loader.loader.resolve("GroqAdapter")

    def get_random_build(self):
        return {"message":"This is a random build"}
    
    '''
    Insert a file into the AI RAG
    '''
    def insert_document_content(self, file_name):
        loader:DirectoryLoader = DirectoryLoader("files/AI_feed_documents/" + file_name)
        docs = loader.load()

    '''
    Ask a question to the AI
    @param question - the question to be asked
    @param class_name - which class is the question about
    '''
    async def class_question(self, question:str, class_name:str):
        from_rag:str = self.rag.get_information(question)
        question:str = question + "\nThis question is about the class " + class_name
        return await self.llm_adapter.send_prompt(question)
    
    '''
    Adds a document to the RAG
    '''
    async def add_document_to_RAG(self, file_name:str):
        try:
            loader:DirectoryLoader = DirectoryLoader("files/AI_feed_documents/" + file_name)
            print(loader.load())
            self.rag.insert_documents(loader)
            return {"message":f"The file {file_name} was loaded successfully."}
        except:
            return {"message":"Something went wrong."}
 
