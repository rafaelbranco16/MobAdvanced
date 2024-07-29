from src.loaders.container import Container
from src.controller.AIController import AIController
from src.controller.document_loader_controller import DocumentLoaderController
from src.services.AIService import AIService
from src.services.document_loader_service import DocumentLoaderService

loader = Container()

loader.register("AIService", AIService())
loader.register("AIController", AIController())
loader.register("DocumentLoaderService", DocumentLoaderService())
loader.register("DocumentLoaderController", DocumentLoaderController())
