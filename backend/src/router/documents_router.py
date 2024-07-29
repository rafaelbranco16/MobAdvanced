from fastapi import APIRouter, UploadFile, File
from src.loaders.loader import loader
from src.controller.document_loader_controller import DocumentLoaderController

document_router = APIRouter()

'''
This is a Router specified to work with documents
'''
class DocumentRouter:
    '''
    Starts the action about to save the document in the AI_feed_documents folder
    '''
    @document_router.post("/insert/document")
    async def insert_valid_document(file: UploadFile = File(...)):
        print(file)
        document_loader_controller:DocumentLoaderController = loader.resolve("DocumentLoaderController")
        return await document_loader_controller.insert_verified_document(file)