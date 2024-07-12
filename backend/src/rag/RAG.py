from langchain_chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

class RAG:
    '''
    Empty constructor
    Initializes the database with an empty Chroma vector database
    '''
    def __init__(self) -> None:
        self.vector_db:Chroma = Chroma(embedding_function=HuggingFaceEmbeddings())

    '''
    Insert a document into the database
    '''
    def insert_documents(self, document: Document):
        self.vector_db.add_documents([document])
    