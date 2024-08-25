from src.adapters.llm_adapter import LLMAdapter
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from src import config


class GroqAdapter(LLMAdapter):
    '''
    The GPT Adapter works over the LangChain
    and uses it to send a prompt

    A future plan would be to use the LangGraph instead

    @param api_key the API key to access the model
    @param model the name of the model (probably from the configuration files)
    '''
    def __init__(self) -> None:
        super().__init__()
        self.define_model()
    
    '''
    Define the model based on the configuration files
    '''
    def define_model(self):
        load_dotenv()
        self.model:ChatGroq = ChatGroq(model=config.groq_model, api_key=os.getenv('GROQ_API_KEY'))
    '''
    This is a temporary function just to test the API key

    Sends the prompt to the OpenAI module
    '''
    async def send_prompt(self, prompt:str, from_rag:str):
        full_rag = ""
        for item in from_rag:
            full_rag += str(item)
        prompt = f'''
You are a Smite Game assistant. Give an answer from what is provided on this text:

{str(full_rag)}

Anything outside this you say that you don't have information about the matter.

This is the question:

{prompt}
        '''
        return self.model.invoke(prompt)