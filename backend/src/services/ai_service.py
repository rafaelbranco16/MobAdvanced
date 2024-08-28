from src.rag.RAG import RAG
from src.loaders import loader
from src.adapters.llm_adapter import LLMAdapter
import src.logger.Logger as logger
from langchain_community.document_loaders import JSONLoader
import os
#Exceptions
from src.exceptions.RagConnectionError import RagConnectionError


class AIService:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.rag = RAG()
        self.llm_adapter:LLMAdapter = loader.loader.resolve("GroqAdapter")
    
    async def get_random_build(self):
        raise NotImplementedError()

    '''
    Ask a question to the AI
    @param question - the question to be asked
    @param class_name - which class is the question about

    Something like this:

    What is SMITE? This question is about the class Warrior
    '''
    async def class_question(self, question:str, class_name:str):
        logger.print_info("Extracting information from the RAG")
        from_rag = any
        response = any

        # RAG Access
        try:
            from_rag:str = self.rag.get_information(question)
            question:str = question + "\nThis question is about the class " + class_name
        except Exception as e:
            logger.print_error("This error occured while accessing the RAG: " + str(e))
            raise RagConnectionError("An error occured while fetching the information to answer your question.")

        logger.print_info("Sending the prompt...")

        # Response
        try:
            response = await self.llm_adapter.send_prompt(question, from_rag)
        except Exception as e: 
            logger.print_error("This error occured while sending the prompt: " + str(e))
            raise ConnectionError("Could not send the prompt to the AI.")
        
        return {"message": response }
    
    '''
    Adds a document to the RAG

    @param file_name the name of the file to be added to the RAG

    The way this works is pretty simple, but the problem is about the file to be added.
    For now it works only with JSONs, which is not recommended.
    The ideal was to have a unic RAG that could handle all this.
    The RAG still in development, therefor the way this is working is pretty straight forward
    It takes the path to the JSON and insert the file into the Vector database
    '''
    async def add_document_to_RAG(self, file_name:str):
        logger.print_info("Trying to add the file: " + file_name)
        try:
            path:str = os.getcwd() + "\\files\\AI_feed_documents\\" + file_name
            loader:JSONLoader = JSONLoader(path, jq_schema='.', text_content=False)
            docs = loader.load()
            self.rag.insert_documents(docs)

            logger.print_info("The file " + file_name + " was added successfully")  

            return {"message":f"The file {file_name} was loaded successfully."}
        except Exception as e:
            logger.print_warning("The file " + file_name + " had the following problem: " + str(e))

            return {"message":"Something went wrong." + str(e)}
 
