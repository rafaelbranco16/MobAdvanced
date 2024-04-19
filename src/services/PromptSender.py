from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

def build_asker(all_items, content, model):
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
    for chunk in chain.stream({"all_items":all_items,"content":content}):
        print(chunk, end="", flush=True)

def god_build_asker(content, all_items, all_gods, model):
    system_message_template = """
<</SYS>>[/INST]\\n
You are a helpful assistant that will give builds to a SMITE god.

You are only able to give information about the items from the following JSON object:
All the items {all_items}
All the gods {all_gods}

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
    #print(chat_prompt)
    output_parser = StrOutputParser()
    chain = (
        chat_prompt
        | model
        | output_parser
    )
    for chunk in chain.stream({"all_items":all_items, "all_gods":all_gods, "content":content}):
        print(chunk, end="", flush=True)