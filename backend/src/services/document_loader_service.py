from fastapi import File, UploadFile
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
        for file in os.listdir(file_dir):
              suffix:str = pathlib.Path(config["ai_feed_files_location"] + f"/{file}").suffix
              files_list.append({
                   "type":suffix,
                   "file_name":file
                })
        print(files_list)
        return files_list;