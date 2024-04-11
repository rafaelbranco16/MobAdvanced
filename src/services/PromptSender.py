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
You are a helpful assistant that will give builds to smite with 6 items each.
For each build you'll have to consider if the item is for a physical damage god or magical damage god.
For Example, if the god is physical you can only give builds where in the stats the item has physical damage.
You can also give items information, only if asked. 
If asked a build return a JSON with a list of items
All the items {all_items}
        """
    human_message_template = "{content}"

    system_message = SystemMessagePromptTemplate.from_template(system_message_template)
    human_message=HumanMessagePromptTemplate.from_template(human_message_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    output_parser = StrOutputParser()
    chain = (
        {
            "all_items": RunnablePassthrough(), 
            "content": RunnablePassthrough()
        }
        | chat_prompt
        | model
        | output_parser
    )
    for chunk in chain.stream([all_items, content]):
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

Here's an example: [starter_item, item1, item2, item3, item4, item5]

Some game general considerations:
* The class carry benefits from Physical Power, Penetration, one lifesteal item and Attack Speed
* The class Mage benefits from raw Magical Power and Magical Penetration

Pay atention to the field strengths of each god and its damage type.

You can only return a JSON with the build. You are not able to write anything out of the 6 items on the JSON.
Give a build accordingly.
        """
    print(content)
    human_message_template = "Anhur"

    system_message = SystemMessagePromptTemplate.from_template(system_message_template)
    human_message=HumanMessagePromptTemplate.from_template(human_message_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    #print(chat_prompt)
    output_parser = StrOutputParser()
    chain = (
        {
            "all_items": RunnablePassthrough(),
            "all_gods": RunnablePassthrough(), 
            "content": RunnablePassthrough()
        }
        | chat_prompt
        | model
        | output_parser
    )
    for chunk in chain.stream([all_items, all_gods, content]):
        print(chunk, end="", flush=True)