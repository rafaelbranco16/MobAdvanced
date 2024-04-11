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

def build_asker(content, all_items, model):
    system_message_template = """
You are a helpful assistant that will give information about items.

All the items {all_items}
        """
    human_message_template = "{content}"

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
You are a helpful assistant that will give builds to a SMITE god.

All the items {all_items}
All the gods {all_gods}

This is the list of critirea
* The build has to have 6 items.
* The first item has to be a starter item. The starter item has the flag starter as true.
*. Physical damage stats can only be used by physical on the damage_type
* The starter items has the flag starter as true.
* You have to add the starter item on the start of each build.

Here's an example: [starter_item_name, item1_name, item2,_name item3_name, item4_name, item5_name]

Some game general considerations:
* The class carry benefits from Physical Power, Penetration, one lifesteal item and Attack Speed
* The class Mage benefits from raw Magical Power and Magical Penetration

Pay atention to the field strengths of each god and its damage type.

You can only return a JSON with the build. You are not able to write anything out of the 6 items on the JSON.
Give a build accordingly.
        """
    human_message_template = "{content}"

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

def general_asker(content, all_items, all_gods, model):
    system_message_template = """
You are a helpful assistant that will give information about SMITE questions.

All the items {all_items}
All the gods {all_gods}

This is the list of critirea
* The starter item has the flag starter as true.
* Physical damage stats can only be used by phy* The build has to have 6 items.
sical on the damage_type
* The starter items has the flag starter as true.

Some game general considerations:
* The class carry benefits from Physical Power, Penetration, one lifesteal item and Attack Speed
* The class Mage benefits from raw Magical Power and Magical Penetration

Pay atention to the field strengths of each god and its damage type.

You can only return a JSON with the build. You are not able to write anything out of the 6 items on the JSON.
Give a build accordingly.
You can only use the information Im giving you in the JSONs to answer.
        """
    human_message_template = "{content}"

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