from fastai.vision.all import *
import gradio as gr

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

model = load_learner('models/art-recognizer-v6.pkl')

def recognize_img(image):
    pred, idx, probs = model.predict(image)
    # Get all probabilities with their labels
    all_probs = dict(zip(artist_labels, map(float, probs)))
    # Sort by probability in descending order and take top 5
    top_5 = dict(sorted(all_probs.items(), key=lambda x: x[1], reverse=True)[:5])
    return top_5

# Gradio app interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 Art2Artist Recognizer")
    
    with gr.Row():
        with gr.Column():
            image = gr.Image(type="filepath", label="Upload Artwork")
            btn = gr.Button("Identify Artist", variant="primary")
        with gr.Column():
            label = gr.Label(num_top_classes=3, label="Artist Prediction")
    
    gr.Examples(
        examples=[
            'test_images/unknown (1).jpeg',
            'test_images/unknown (2).jpeg',
            'test_images/unknown (3).jpeg',
            'test_images/unknown (4).jpg'
        ],
        inputs=image,
        label="Example Artworks"
    )
    
    btn.click(fn=recognize_img, inputs=image, outputs=label)

demo.launch()