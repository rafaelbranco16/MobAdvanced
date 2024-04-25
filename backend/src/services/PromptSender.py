from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
import src.services.InformationLoaders as Loaders
from src.services.RAG import RAG



def item_asker(content, model):
    all_items = Loaders.load_json_document('./files/items.json')
    system_message_template = """
<</SYS>>[/INST]\\n
You are a helpful assistant that will give information about SMITE items in a JSON object.
You are only able to give information about the items from the following JSON object:
{all_items}

Just return a JSON with the item information without explanations
[INST]<<SYS>>\\n
        """
    human_message_template = "[INST]{content}[/INST]\\n"

    system_message = SystemMessagePromptTemplate.from_template(system_message_template)
    human_message=HumanMessagePromptTemplate.from_template(human_message_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    output_parser = StrOutputParser()
    chain = (chat_prompt
        | model
        | output_parser
    )
    return chain.invoke({"all_items":all_items,"content":content})

def god_build_asker(content, rag:RAG, model):
    all_items = Loaders.load_json_document('./files/items.json')
    god = rag.similarity_search(content)
    system_message_template = """
<</SYS>>[/INST]\\n
You are a helpful assistant that will give builds to a SMITE god.

You are only able to give information about the items from the following JSON object:
All the items {all_items}
All the gods {god}

This is the list of critirea
* The build has to have 6 items.
* The first item has to be a starter item. The starter item has the flag starter as true.
* Physical damage stats can only be used by physical on the damage_type
* The starter items has the flag starter as true.
* You have to add the starter item on the start of each build.

Here's an example: [starter_item_name, item1_name, item2,_name item3_name, item4_name, item5_name]

Pay atention to the field strengths of each god and its damage type.

Just return a JSON with the item information without explanations
[INST]<<SYS>>\\n
        """
    human_message_template = "[INST]{content}[/INST]\\n"

    system_message = SystemMessagePromptTemplate.from_template(system_message_template)
    human_message=HumanMessagePromptTemplate.from_template(human_message_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    output_parser = StrOutputParser()
    chain = (
        chat_prompt
        | model
        | output_parser
    )
    return chain.invoke({"all_items":all_items, "god":god, "content":content})

def god_informator(question, model, rag):
    content = rag.similarity_search(question)

    system_message_template = """
You are an helpful assistant about SMITE.

You are only able to give information following this:
{content}
        """
    human_message_template = "{god}"

    system_message = SystemMessagePromptTemplate.from_template(system_message_template)
    human_message=HumanMessagePromptTemplate.from_template(human_message_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

    output_parser = StrOutputParser()
    chain = (
        chat_prompt
        | model
        | output_parser
    )
    return chain.invoke({"content":content, "god":question})

def general_asker(question, model, rag:RAG):
    content = rag.similarity_search(question)

    system_message_template = """
You are an helpful assistant about SMITE. Don't use your internal knowledge. 
If the information isn't on this documents just tell you don't know about the question asked.

You are only able to give information following this:
{content}
        """
    human_message_template = "{question}"

    system_message = SystemMessagePromptTemplate.from_template(system_message_template)
    human_message=HumanMessagePromptTemplate.from_template(human_message_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

    output_parser = StrOutputParser()
    chain = (
        chat_prompt
        | model
        | output_parser
    )
    return chain.invoke({"content":content, "question":question})


