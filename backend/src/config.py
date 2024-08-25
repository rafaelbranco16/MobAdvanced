from dotenv import load_dotenv
import os

config = {
    "ai_feed_files_location":"files/AI_feed_documents",
    "react_app_url":"http://localhost:5173/"
}

gpt_model = "gpt-3.5-turbo"
groq_model = "llama-3.1-70b-versatile"

#Services
ai_service = {
    "name":"AIService",
    "path":"src.services.ai_service"
}
document_loader_service = {
    "name":"DocumentLoaderService",
    "path":"src.services.document_loader_service"
}

# Controllers
ai_controller = {
    "name":"AIController",
    "path":"src.controllers.ai_controller"
}
document_loader_controller = {   
    "name":"DocumentLoaderController",
    "path":"src.controllers.document_loader_controller"
}

# Adapters
llm_adapter = {
    "name":"GroqAdapter",
    "path":"src.adapters.groq_adapter"
}