# testing with flask
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    with open("interactive_spectrogram.html", 'r') as f:
        content = f.read()
    return render_template_string(content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

# Seems to work. Def need to optimize/learn more about web stuff to load faster.