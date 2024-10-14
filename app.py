from flask import Flask, render_template, request, redirect, url_for
from myapp.utils import *

app = Flask(__name__, template_folder='templates')  # Création de l'objet

@app.route('/')
def index(value=False):
    return render_template('accueil.html', value=value)

@app.route('/profil/<username>', methods=['GET'])
def profil(username):
    print(username)
    return render_template('profil.html', name=get_player(username))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logique de vérification du login ici
        # TODO : ajouter une logistique d'authentification (utilisation de la fonction check_user)
        form = request.form
        # Ajouter la logique d'authentification
        return redirect(url_for('index', value=True))
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        form = request.form
        add_user(form)
        return redirect(url_for('index', value=True))
    else :
        return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
