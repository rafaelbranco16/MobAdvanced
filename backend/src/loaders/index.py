from src import config

controllers = [
    config.ai_controller,
    config.document_loader_controller
]

services = [
    config.ai_service,
    config.document_loader_service
]

adapters = [
    config.llm_adapter
]