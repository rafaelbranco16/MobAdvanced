from fastapi import File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from src.config import config
import shutil
import os
import pathlib

class DocumentLoaderService:
    '''
    Saves the file into the filesystem
    '''
    async def save_valid_file(self, file: UploadFile = File(...)):
        file_dir = config["ai_feed_files_location"]
        os.makedirs(file_dir, exist_ok=True)
        file_location = os.path.join(file_dir, file.filename)
        with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        return {"info": f"file '{file.filename}' saved at '{file_location}'"}

    '''
    Return all files into the filesystem
    '''
    async def get_all_documents(self):
        file_dir = config["ai_feed_files_location"]
        files_list = []
        file_path = os.path.join(os.getcwd(), file_dir)
        for file in os.listdir(file_path):
            suffix: str = pathlib.Path(file).suffix
            file_id = file
            
            files_list.append({
                "type": suffix,
                "file_name": file,
                "download_url": f"/download/{file_id}"
            })

        return files_list
    '''
    Returns a file from this server
    '''
    async def download_file(self, file_name:str):
        file_dir = config["ai_feed_files_location"]

        file_path = os.path.join(file_dir, file_name)
    
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")
        
        mime_type = {
            ".json": "application/json",
            ".md": "text/markdown",
            ".txt": "text/plain",
        }.get(os.path.splitext(file_name)[1], "application/octet-stream")
        return FileResponse(file_path, media_type=mime_type, filename=file_name)
    
    async def remove_file(self, file_name:str):
        file_dir = config["ai_feed_files_location"]
        file_path = os.path.join(file_dir, file_name)
        print(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"The file {file_name} was not found on the directory {file_dir}")
    