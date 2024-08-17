from src.services.document_loader_service import DocumentLoaderService
from src.loaders import loader
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse


class DocumentLoaderController:
    def __init__(self) -> None:
        self.document_loader_service:DocumentLoaderService = loader.loader.resolve("DocumentLoaderService")
    '''
    Sends the service so the file can be saved
    '''
    async def insert_verified_document(self, file: UploadFile = File(...)):
        return await self.document_loader_service.save_valid_file(file)
    '''
    Sends to the service to return all files into the AI folder
    '''
    async def get_all_documents(self):
        docs = await self.document_loader_service.get_all_documents()
        return {"documents": docs}
    
    '''
    Sends to the service to return a file
    '''
    async def download_file(self, file_name:str):
        return await self.document_loader_service.download_file(file_name=file_name)
    
    async def remove_file(self, file_name):
        try:
            await self.document_loader_service.remove_file(file_name)
            return {"message":"The file " + file_name + " was removed"}
        except FileNotFoundError as err:
            return JSONResponse(
                status_code=404,
                content={"detail":str(err)}
            )
        except:
            return JSONResponse(
                status_code=400,
                content={"detail":"Something went wrong"}
            )