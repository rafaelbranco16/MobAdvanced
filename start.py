from src.services import InformationLoaders
from src.services.ModelLoader import create_model
import json
from pathlib import Path
from pprint import pprint
from src.services.PromptSender import build_asker

def main():
    model = create_model()
    file_content = InformationLoaders.load_json_document('./files/items.json')
    build_asker(file_content, "Give me all attack items", model)

if __name__ == "__main__":
    main()