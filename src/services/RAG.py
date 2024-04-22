from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents.base import Document
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

class RAG:
    def __init__(self):
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectordb:Chroma = Chroma(embedding_function=embedding_function)

    def add_documents(self, doc:Document):
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(doc)

        self.vectordb.add_documents(docs)

    def similarity_search(self, query):
        return self.vectordb.similarity_search(query)