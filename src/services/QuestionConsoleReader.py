from src.services import InformationLoaders
from src.services.ModelLoader import create_model
from src.services.PromptSender import build_asker, god_build_asker

def question_console_reader():
    choice = 100
    while choice != "0":
        choice = input(
            """
            Welcome to MobAdvanced: 
            1: Ask for items
            2: Ask for a build for a god
            3: Ask anything
            0: Exit
            """
        )
        decider(choice)

def decider(choice):
    if choice == "1":
        question = input("What is the item you want to know about?\n\n")
        model = create_model()
        build_asker(question, model)

    if choice == "2":
        question = input("You want a build for which god?\n\n")
        model = create_model()
        items_content = InformationLoaders.load_json_document('./files/items.json')
        gods_content = InformationLoaders.load_json_document('./files/gods.json')
        god_build_asker(question, items_content, gods_content, model)