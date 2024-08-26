from src.adapters.llm_adapter import LLMAdapter
from src import config
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langfuse.decorators import observe
from dotenv import load_dotenv
import os


class GPTAdapter(LLMAdapter):
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
        self.model:ChatOpenAI = ChatOpenAI(model=config.gpt_model, api_key=os.getenv('GPT_API_KEY'))
        '''
    This is a temporary function just to test the API key

    Sends the prompt to the OpenAI module
    '''
    @observe()
    async def send_prompt(self, prompt:str, from_rag:str):
        print("Im here")
        full_rag = ""
        for item in from_rag:
            full_rag += str(item)
        sys_message = f'''
You are a Smite Game assistant. Give an answer from what is provided on this text:

{str(full_rag)}

Anything outside this you say that you don't have information about the matter.
'''
        human_message = f'''   
This is the question:

{prompt}
        '''
        messages = [
            SystemMessage(content=sys_message),
            HumanMessage(content=human_message)
        ]
        chain = self.model | StrOutputParser()
        response = chain.invoke(messages, config={"callbacks":[config.langfuse]})
        print(response)
        return str(response)