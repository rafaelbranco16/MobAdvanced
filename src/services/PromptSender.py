from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def build_asker(content, all_items, model):
    prompt = ChatPromptTemplate.from_template(
        "Based in this items {all_items}, {content}"
    )
    output_parser = StrOutputParser()
    chain = (
        {"all_items": RunnablePassthrough(), "content": RunnablePassthrough()}
        | prompt
        | model
        | output_parser
    )
    chain.invoke([all_items, content])