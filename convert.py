import html, re

prompt = ""
with open('test.txt', 'r') as f:
    prompt = f.read()

output_text = ""

# output_text += "<pre>"
# output_text += prompt
# output_text += "</pre>"

for i, line in enumerate(prompt.split('\n')):
    # output_text += line + "\\n"
    if i == 0:
        output_text += f"<p class=\"block block-paragraph first-block\">{html.escape(line)}</p>"
    elif i == len(prompt.split('\n')) - 1:
        output_text += f"<p class=\"is-focused is-focused-inside block block-paragraph last-block\">{html.escape(line)}</p>"
    else:
        output_text += f"<p class=\"block block-paragraph\">{html.escape(line)}</p>"


# Replace all quotes with \", single quotes with \', and backslashes with \\
output_text = re.sub(r'([\'])', r'\\\1', output_text)

# Write the modified content to a new file
with open('test.txt', 'w') as f:
    f.write(output_text)