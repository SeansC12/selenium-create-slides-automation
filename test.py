import html

prompt = ""
with open('prompt.txt', 'r') as f:
    prompt = f.read()

sanitised = html.escape(prompt)

with open('sanitised.txt', 'w') as f:
    f.write(sanitised)
