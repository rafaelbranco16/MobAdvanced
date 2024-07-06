from backend.src.loaders import loader
from backend.src.services.AIService import AIService


class AIController:
    '''
    Constructor
    '''
    def __init__(self) -> None:
        self.ai_service:AIService = loader.loader.resolve("AIService")

    def get_random_build(self):
        return self.ai_service.get_random_build()