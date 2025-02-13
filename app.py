from flask import Flask, request
from gamma_slide_creator import GammaSlideCreator
import html
import re

app = Flask(__name__)

Slides = GammaSlideCreator()
Slides.setup_method()
# Slides.create_slides()

def sanitise_slide_outline_and_save_to_file(slide_outline):
    output_text = ""

    for i, line in enumerate(slide_outline.split('\n')):
    # output_text += line + "\\n"
        if i == 0:
            output_text += f"<p class=\"block block-paragraph first-block\">{html.escape(line)}</p>"
        elif i == len(slide_outline.split('\n')) - 1:
            output_text += f"<p class=\"is-focused is-focused-inside block block-paragraph last-block\">{html.escape(line)}</p>"
        else:
            output_text += f"<p class=\"block block-paragraph\">{html.escape(line)}</p>"
    

    output_text = re.sub(r'(["\'])', r'\\\1', slide_outline)

    with open('slide_outline.txt', 'w') as f:
        f.write(output_text)

@app.route("/", methods=["GET", "POST"])
def index():
    # slide_outline = unquote(request.get_json("slide_outline"))
    slide_outline = str(request.get_data())[2:]
    print(slide_outline)
    sanitise_slide_outline_and_save_to_file(slide_outline)
    
    gamma_url = Slides.create_slides()

    return gamma_url
