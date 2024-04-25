from src.services.RAG import RAG
from src.services import InformationLoaders

def boot_rag() -> RAG:
    rag = RAG()
    gods = InformationLoaders.load_json_document('../files/gods.json')
    game_info = InformationLoaders.load_txt_document('../files/game.txt')
    rag.add_documents(gods)
    rag.add_documents(game_info)
    return rag