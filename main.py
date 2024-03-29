from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from app.db_utils import *
from app.test_db import *
from app.COULEURS import *
import logging


my_db = Outils_db("static/db/fifoandlifo.db")

def reponse_db(*args):
    pass

id_classe = 1

app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key = 'motdepassesupersecret'

@app.route('/')
def hello_world():
    """
    Page d'accueil, pour présenter le projet.

    """
    return render_template("index.html")

@app.route('/bonjour')
def bonjour():
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
    print(dic_etab_classe)
    if request.method == "POST":
        password = request.form['password']
        lycee = request.form['lycee']
        classe = request.form['section'].replace("radio","")
        print(f"password : {password}")
        print(f"lycee : {lycee}")
        print(f"classe : {classe}")
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

app.route("logout")
def logout():
    session.pop('uid', None)
    session.pop('classe', None)
    session.pop('lycee', None)
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
            print(request.form)
            if reponse_value:
                print('Enregistrement de la réponse dans base de donnée')
                test_result = "Reponse enregistée"
                reponse_db(id_classe, reponse_value)
                return render_template(f"enigme{nb_enigme}.html", test_result=test_result, final=True,  couleurs_d=VIOLETS_D)
            
            else:
                logging.info('On effectue un test')
                test_result = test(test_value)
                return render_template(f"enigme{nb_enigme}.html", test_result=test_result, final=False,  couleurs_d=VIOLETS_D)

    test_result = ""
    return render_template(f"enigme{nb_enigme}.html", test_result=test_result, couleurs_d=VIOLETS_D)

 

@app.route('/admin')
def admin():
    """

    """
    pass 
    
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