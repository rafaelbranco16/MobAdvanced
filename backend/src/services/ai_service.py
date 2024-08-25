from src.rag.RAG import RAG
from langchain_community.document_loaders import DirectoryLoader
from src.loaders import loader
from src.adapters.llm_adapter import LLMAdapter
from langchain_core.documents import Document
import os
from langchain_community.document_loaders import JSONLoader
from pathlib import Path
from pprint import pprint



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
        print(os.getcwd())
        loader:JSONLoader = JSONLoader(os.getcwd() + "files/AI_feed_documents/" + file_name)
        docs = loader.load()

    '''
    Ask a question to the AI
    @param question - the question to be asked
    @param class_name - which class is the question about
    '''
    async def class_question(self, question:str, class_name:str):
        from_rag:str = self.rag.get_information(question)
        print(from_rag)
        question:str = question + "\nThis question is about the class " + class_name
        return {"message": await self.llm_adapter.send_prompt(question, from_rag) }
    
    '''
    Adds a document to the RAG
    '''
    async def add_document_to_RAG(self, file_name:str):
        try:
            path:str = os.getcwd() + "\\files\\AI_feed_documents\\" + file_name
            loader:JSONLoader = JSONLoader(path, jq_schema='.', text_content=False)
            docs = loader.load()
            self.rag.insert_documents(docs)
        
            return {"message":f"The file {file_name} was loaded successfully."}
        except Exception as e:
            return {"message":"Something went wrong." + str(e)}
 
