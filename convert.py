import html

prompt = ""
with open('prompt.txt', 'r') as f:
    prompt = f.read()

html_text = ""

for i, line in enumerate(prompt.split('\n')):
    html_text += html.escape(line) + "\\n"
    # if i == 0:
    #     html_text += f"<p class=\"block block-paragraph first-block\">{html.escape(line)}</p>"
    # elif i == len(prompt.split('\n')) - 1:
    #     html_text += f"<p class=\"is-focused is-focused-inside block block-paragraph last-block\">{html.escape(line)}</p>"
    # else:
    #     html_text += f"<p class=\"block block-paragraph\">{html.escape(line)}</p>"


with open('slide_outline.txt', 'w') as f:
    f.write(html_text)
