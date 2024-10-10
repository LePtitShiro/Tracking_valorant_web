from flask import Flask, render_template
from myapp.utils import *

app = Flask(__name__, template_folder='templates')  # Création de l'objet



@app.route('/')
def index():
    return render_template('accueil.html')


if __name__ == '__main__':
    app.run()
