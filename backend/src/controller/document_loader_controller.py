from src.services.document_loader_service import DocumentLoaderService
from src.loaders import loader
from fastapi import File, UploadFile


class DocumentLoaderController:
    def __init__(self) -> None:
        self.document_loader_service:DocumentLoaderService = loader.loader.resolve("DocumentLoaderService")
    '''
    Sends the service so the file can be saved
    '''
    async def insert_verified_document(self, file: UploadFile = File(...)):
        return await self.document_loader_service.save_valid_file(file)