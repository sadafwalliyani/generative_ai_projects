import gradio as gr
from transformers import pipeline

get_completion = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


import gradio as gr
def summarize(input):
    output = get_completion(input)
    return output[0]['summary_text']

gr.close_all()
demo = gr.Interface(fn=summarize,
                    inputs=[gr.Textbox(label="Text to summarize", lines=10)],
                    outputs=[gr.Textbox(label="Result", lines=10)],
                    title="Text summarization with Sadaf Walliyani",
                    description="Summarize any text using the CNN model'!"
                   )
demo.launch(share=True)


