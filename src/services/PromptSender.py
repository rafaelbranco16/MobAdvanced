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
    for chunk in chain.stream([all_items, content]):
        print(chunk, end="", flush=True)

def god_build_asker(content, all_items, all_gods, model):
    prompt = ChatPromptTemplate.from_template(
        """
        Based in this items {all_items} and this gods {all_gods}, 
        {content}.
        A build is composed by a set of 6 items.
        Physical Gods can only use Physical Items and vice-versa
        """
    )
    output_parser = StrOutputParser()
    chain = (
        {
            "all_items": RunnablePassthrough(), 
            "all_gods":RunnablePassthrough(),
            "content": RunnablePassthrough()
        }
        | prompt
        | model
        | output_parser
    )
    for chunk in chain.stream([all_items, all_gods, content]):
        print(chunk, end="", flush=True)