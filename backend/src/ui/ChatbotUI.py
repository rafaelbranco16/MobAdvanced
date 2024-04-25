import gradio as gr
import src.services.ModelLoader as ModelLoader
import src.services.InformationLoaders as Loaders
import src.services.PromptSender as Sender
from src.services.LoadRAG import boot_rag
from src.services.RAG import RAG


def chatbot():
    global rag
    rag = boot_rag()
    interface = gr.Interface(fn=ask_bot,
                            inputs=[
                                gr.Textbox(lines=2, placeholder="Type here...", label="Insert the question..."),
                                gr.Radio(["Build","God","Item"], label="What type of question...")
                            ],
                            outputs=gr.Textbox(interactive=False),
                            title="MobAdvanced",
                            )
    interface.launch(share=True)

def ask_bot(question, radio):
    return decider(question, radio)

def decider(question, radio):
    model = ModelLoader.create_model()
    if radio == "God":
        return Sender.god_informator(question=question, model=model, rag=rag)
    if radio == "Item":
        return Sender.item_asker(question, model)
    if radio == "Build":
        return Sender.god_build_asker(question, rag, model)