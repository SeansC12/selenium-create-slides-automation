from flask import Flask, request
from gamma_slide_creator import GammaSlideCreator
import html

app = Flask(__name__)

Slides = GammaSlideCreator()
Slides.setup_method()
# Slides.create_slides()

def sanitise_slide_outline_and_save_to_file(slide_outline):
    html_text = ""

    for line in slide_outline.split('\n'):
        html_text += html.escape(line) + "\\n"

    with open('slide_outline.txt', 'w') as f:
        f.write(html_text)

@app.route("/", methods=["GET", "POST"])
def index():
    # slide_outline = unquote(request.get_json("slide_outline"))
    slide_outline = str(request.get_data())[2:]
    print(slide_outline)
    sanitise_slide_outline_and_save_to_file(slide_outline)
    
    gamma_url = Slides.create_slides()

    # slide_outline = unquote()
    return gamma_url
