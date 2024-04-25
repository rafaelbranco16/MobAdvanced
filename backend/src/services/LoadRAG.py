from src.services.RAG import RAG
from src.services import InformationLoaders

def boot_rag() -> RAG:
    rag = RAG()
    gods = InformationLoaders.load_json_document('./files/gods.json')
    rag.add_documents(gods)
    return rag