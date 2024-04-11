import config
from langchain_openai import ChatOpenAI

def create_model():
    return ChatOpenAI(
        model=config.lm_model_name, 
        base_url=config.lm_url,
        api_key=config.lm_api_key    
    )