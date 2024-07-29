from fastapi import File, UploadFile
from src.config import config
import shutil
import os

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
