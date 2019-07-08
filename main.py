from flask import Flask, render_template, request, flash, redirect,url_for
from app.db_utils import recuperation_noms_etablissements, recuperation_etab_et_classes
from app.COULEURS import *
import logging



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
        if request.form['password'] == '007' and request.form['username'] == 'james':
           flash('You were successfully logged in')
           return redirect(url_for('enigme', nb_enigme=None))
    return render_template("temp_login.html", ma_variable=dic_etab_classe)



@app.route('/enigme/', methods=['GET', 'POST'])
@app.route('/enigme/<int:nb_enigme>', methods=['GET', 'POST'])
def enigme(nb_enigme=None):
    """
    Gestion des enigmes
    """
    if not nb_enigme:
        return render_template('carousel.html', couleurs = VIOLETS, couleurs_d = VIOLETS_D, VIOLETS_D= VIOLETS_D, JAUNES_D=JAUNES_D, TURQUOISES_D=TURQUOISES_D)

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
            reponse = request.form.get("reponse")
            test_value = request.form.get("test")
            reponse_values = request.form.get("reponse")
            
            if reponse:
                logging.info('Enregistrement de la réponse dans base de donnée')
                test_result = "Reponse enregistée"
                reponse_db(id_classe, reponse_values)
                return render_template(f"enigme{nb_enigme}.html", test_result="Résultat enregistée", final=True,  couleurs_d=VIOLETS_D)
            
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
    app.run(host="0.0.0.0", port=8080, debug=True)


# Test MOCK ->
# 
# function truc(){
#     this.a = 5;
#     onclick((p, o) => {
#        this.a = 6
#     });
# }