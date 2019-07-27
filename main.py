from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
import json
import os
import logging
import functools



#Import des modules de l'application
PATH = os.path.abspath(os.path.split(__file__)[0])
os.chdir(PATH)

from app.db_utils import *
from app.flask_utils import login_as
from app.test_db import *
from app.COULEURS import *



my_db = Outils_db("static/db/fifoandlifo.db")



def reponse_db(*args):
    pass

id_classe = 1
# Initialisation de l'application Flask
app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key = 'motdepassesupersecret'


@app.route('/')
def hello_world():
    """
    Page d'accueil, pour présenter le projet.
    """
    #Test on initialise la session 
    return render_template("index.html")


@app.route('/debug_session')
def debug_session():
    """
    Page de débuggage pour connaitre la session
    """
    if not  "type" in session: 
        #Test on initialise la session
        session["type"] = 'rallye'
    return session["type"]


@app.route('/bonjour')
@login_as(type="rallye",redirect="login_classe")
def bonjour():
    """
    Page de présentation de l'équipe : 
    """
    equipe = ['denis', 'alan', 'joris', 'eric', 'etienne']
    return render_template('/bonjour.html', equipe=equipe)


@app.route('/login',methods=["GET", "POST"])
def login():
    """
    Gestion du login de la classe
    Verification des identifiants + récupération des éléments de la classe
    """
    # liste_lycee =  recuperation_noms_etablissements()
    dic_etab_classe= recuperation_etab_et_classes()
    if request.method == "POST":
        password = request.form['password']
        lycee = request.form['lycee']
        classe = request.form['section'].replace("radio","")
        auth = identification({"password":password, "lycee":lycee, "classe":classe})
        if auth:
            session["lycee"] = lycee
            session["classe"] = classe
            session["uid"] = auth
            flash('You were successfully logged in')
            return redirect(url_for('enigme', nb_enigme=None))
        else:
            flash('Mot de passe incorrect')
            return render_template("login.html", ma_variable=dic_etab_classe)
    return render_template("login.html", ma_variable=dic_etab_classe)


@app.route("/login2", methods=["GET", "POST"])
def login2():
    lycees = my_db.get_classe_by_lycee()
    if request.method == "POST":
        id_classe = request.form['id_classe']
        print(id_classe)
        password = request.form['password']
        auth = my_db.auth_by_idclasse(id_classe=id_classe, password=password)
        if auth:
            flash('You were successfully logged in')
            return redirect(url_for('choix_enigme', nb_enigme=None))
    return render_template("login2.html", lycees = lycees )


@app.route("/logout")
def logout():
    """
    Efface les informations de la session.
    """
    session.pop('uid', None)
    session.pop('classe', None)
    session.pop('lycee', None)
    session.pop('type', None)
    return "logout"


@app.route('/enigme/', methods=['GET', 'POST'])
@app.route('/enigme/<int:nb_enigme>', methods=['GET', 'POST'])
def enigme(nb_enigme=None):
    """
    Gestion des enigmes
    """
    if not nb_enigme:
        enigmes = my_db.recuperation_enigme()
        return render_template('carousel.html',
            enigmes=enigmes,
            enigmes_json = json.dumps(enigmes),
            couleurs=VIOLETS,
            couleurs_d=VIOLETS_D,
            VIOLETS_D=VIOLETS_D, 
            JAUNES_D=JAUNES_D,
            TURQUOISES_D=TURQUOISES_D)

    if nb_enigme:
        def test(*args):
            """
            Effecute les tests de l'enigme
            
            @param : liste de parametres
            @return : texte à afficher
            """
            try:
                resultat = 2 * args[0]
            except:
                resultat = "La valeur passer en parametre est incorrect"
            return resultat

        if request.method == 'POST':
            """
            Traitement des réponses aux formulaires
            """
            test_value = request.form.get("test")
            reponse_value = request.form.get("reponse")
            if reponse_value:
                test_result = "Reponse enregistée"
                reponse_db(id_classe, reponse_value)
                return render_template(f"enigme{nb_enigme}.html", test_result=test_result, final=True,  couleurs_d=VIOLETS_D)
            
            else:
                logging.info('On effectue un test')
                test_result = test(test_value)
                return render_template(f"enigme{nb_enigme}.html", test_result=test_result, final=False,  couleurs_d=VIOLETS_D)

    test_result = ""
    return render_template(f"enigme{nb_enigme}.html", test_result=test_result)


@app.route('/choixenigme/', methods=['GET', 'POST'])
@app.route('/choixenigme/<int:nb_enigme>', methods=['GET', 'POST'])
def choix_enigme(nb_enigme=None):
    """
    Choix des enigmes
    """
    if not nb_enigme:
        nb_enigme = 1
    enigmes = my_db.get_enigmes()
    len_enigmes = len(enigmes)
    try:
        enigme = enigmes[nb_enigme-1]
    except Exception as e:
        enigme = enigmes[nb_enigme % len_enigmes]
    return render_template('choixenigme.html', enigme=enigme, nb_enigme=nb_enigme, len_enigmes=len_enigmes)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """
    Authentification des utilisateurs
    """
    if request.method == 'POST':
        user = request.form.get("user")
        password = request.form.get("password")
        if auth(user, password):
            session["lycee"] = user["lycee"]
            session["classe"] = user["classe"]
            session["uid"] = user["uid"]     
            session["is_admin"] = user["is_admin"]           
    

@app.route("/restart", methods=['POST'])
def restart():
    """
    Permet de redemarrer le serveur de dev
    Utile pour la CI de GITLAB
    """
    if request.method == "POST":
        if request.form.get('token') == "Gwf7H6hHimEL4B6B":
            os.system("supervisordctl restart dev.fifoandlifo")


@app.route('/WelcomeKaribou')
def Welcome_Karibou():
    liste = ["Joris_lapuissance", "Denis_jeunepapa", "Eric_absent", "Etienne_monsieurréférence", "Alan_maispourquoi"]
    return render_template('/ALAN.html', equipe = liste)


@app.route('/testdesignprojet')
def testdesignprojet():
    return render_template('testdesignprojet.html')


@app.route('/test')
def test():
    return render_template('carousel.html', couleurs = VIOLETS, couleurs_d = VIOLETS_D, VIOLETS_D= VIOLETS_D, JAUNES_D=JAUNES_D, TURQUOISES_D=TURQUOISES_D)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)


# Test MOCK ->
# 
# function truc(){
#     this.a = 5;
#     onclick((p, o) => {
#        this.a = 6
#     });
# }