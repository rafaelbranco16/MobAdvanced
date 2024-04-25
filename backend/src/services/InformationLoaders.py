from langchain_community.document_loaders import JSONLoader


def load_json_document(filePath):
    loader = JSONLoader(
        file_path=filePath,
        jq_schema='.',
        text_content=False
    )
    return loader.load()