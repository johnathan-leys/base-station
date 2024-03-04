# testing with flask
from flask import Flask, render_template_string

# Create instance "app" of the Flask class
app = Flask(__name__)    # __name__ = name of current module

# Decorator: Modifies function, implemented as functions which take other function as input. Usually add functions such as logging, modifying input...
# Used to specify URL route where index() should be triggered: if url is "/" (root url of web app) call index().
# Decorator, tells Flask to associate "index" function with url '/'. When request is made to '/', function is invoked
@app.route('/')    # '/' is usually default from browser
def index():        # Funtion reads,renders spectrogam file
    with open("interactive_spectrogram.html", 'r') as f:
        content = f.read()
    return render_template_string(content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)    # Accesible from any net interface, port 5k

# Seems to work. Def need to optimize/learn more about web stuff to load faster.
