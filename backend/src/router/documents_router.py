from fastapi import APIRouter, UploadFile, File
from src.loaders.loader import loader
from src.controllers.document_loader_controller import DocumentLoaderController

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
        document_loader_controller:DocumentLoaderController = loader.resolve("DocumentLoaderController")
        return await document_loader_controller.insert_verified_document(file)
    
    '''
    Starts the action to get all the documents into the AI folder
    '''
    @document_router.get("/all/documents")
    async def get_all_documents():
        document_loader_controller:DocumentLoaderController = loader.resolve("DocumentLoaderController")
        return await document_loader_controller.get_all_documents()
    
    @document_router.get("/download/{file_name}")
    async def download_file(file_name:str):
        document_loader_controller:DocumentLoaderController = loader.resolve("DocumentLoaderController")
        return await document_loader_controller.download_file(file_name)
    
    @document_router.get("/remove/{file_name}")
    async def remove_file(file_name:str):
        document_loader_controller:DocumentLoaderController = loader.resolve("DocumentLoaderController")
        return await document_loader_controller.remove_file(file_name)