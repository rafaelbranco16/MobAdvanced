from backend.src.loaders.container import Container
from backend.src.controller.AIController import AIController
from backend.src.services.AIService import AIService


loader = Container()

loader.register("AIService", AIService())
loader.register("AIController", AIController())
