from src.rag.RAG import RAG
from langchain_community.document_loaders import DirectoryLoader
from src.loaders import loader
from src.adapters.llm_adapter import LLMAdapter
from langchain_core.documents import Document
import os
from langchain_community.document_loaders import JSONLoader
import src.logger.Logger as logger


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
        logger.print_info("Extracting information from the RAG")
        from_rag:str = self.rag.get_information(question)
        question:str = question + "\nThis question is about the class " + class_name
        logger.print_info("Sending the prompt")
        response = await self.llm_adapter.send_prompt(question, from_rag)
        return {"message": response }
    
    '''
    Adds a document to the RAG
    '''
    async def add_document_to_RAG(self, file_name:str):
        logger.print_info("Trying to add the file: " + file_name)
        try:
            path:str = os.getcwd() + "\\files\\AI_feed_documents\\" + file_name
            print(path)
            loader:JSONLoader = JSONLoader(path, jq_schema='.', text_content=False)
            docs = loader.load()
            self.rag.insert_documents(docs)
            logger.print_info("The file " + file_name + " was added successfully")  
            return {"message":f"The file {file_name} was loaded successfully."}
        except Exception as e:
            logger.print_warning("The file " + file_name + " had the following problem: " + str(e))
            return {"message":"Something went wrong." + str(e)}
 
