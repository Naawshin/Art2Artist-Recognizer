from fastai.vision.all import *
import gradio as gr

#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

artist_labels = ("Caravaggio's artwork",
                 "Claude Monet's artwork",
                 "Diego Rivera's artwork",
                 "Edgar Degas's artwork",
                 "Edvard Munch's artwork",
                 "Frida Kahlo's artwork",
                 "Gustav Klimt's artwork",
                 "Henri Matisse's artwork",
                 "Jackson Pollock's artwork",
                 "Joan Miró's artwork",
                 "Leonardo da Vinci's artwork",
                 "Mark Rothko's artwork",
                 "Michelangelo's artwork",
                 "Pablo Picasso's artwork",
                 "Paul Cézanne's artwork",
                 "Pierre-Auguste's artwork",
                 "Raphael's artwork",
                 "Rembrandt van Rijn's artwork",
                 "Salvador Dalí's artwork",
                 "Vincent van Gogh's artwork")

model = load_learner('models/art-recognizer-v2.pkl')

def recognize_img(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(artist_labels, map(float, probs)))

# Gradio app interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 Art2Artist Recognizer")
    
    with gr.Row():
        with gr.Column():
            image = gr.Image(type="filepath", label="Upload Artwork")
            btn = gr.Button("Identify Artist")
        with gr.Column():
            label = gr.Label(label="Prediction")
    
    gr.Examples(
        examples=['test_images/download (1).jpeg', 'test_images/download (2).jpeg',
                 'test_images/download (3).jpeg', 'test_images/download (4).jpeg'],
        inputs=image
    )
    
    btn.click(fn=recognize_img, inputs=image, outputs=label)

demo.launch(share=True)