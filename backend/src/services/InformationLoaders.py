from langchain_community.document_loaders import JSONLoader, TextLoader


def load_json_document(filePath):
    loader = JSONLoader(
        file_path=filePath,
        jq_schema='.',
        text_content=False
    )
    return loader.load()

def load_txt_document(filePath):
    loader = TextLoader(
        file_path=filePath, 
        encoding='UTF-8'
    )
    return loader.load()