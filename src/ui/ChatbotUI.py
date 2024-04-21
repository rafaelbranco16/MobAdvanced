import gradio as gr
import src.services.ModelLoader as ModelLoader
import src.services.InformationLoaders as Loaders
import src.services.PromptSender as Sender

model = ModelLoader.create_model()

def chatbot():
    interface = gr.Interface(fn=ask_bot,
                            inputs=[
                                gr.Textbox(lines=2, placeholder="Type here..."),
                                gr.Radio(["Build","God"], label="What type of question...")
                            ],
                            outputs=gr.Textbox(interactive=False),
                            title="Ask a simple question about an item.",
                            )
    interface.launch()

def ask_bot(question, radio):
    print(radio)
    return Sender.build_asker(question, model)