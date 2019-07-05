from flask import Flask, render_template, request
from app.db_utils import recuperation_noms_etablissements
from app.COULEURS import *
import logging

def reponse_db(*args):
	pass

id_classe = 1

app = Flask(__name__, template_folder='template', static_folder='static')

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


@app.route('/login')
def login():
    """
    Gestion du login de la classe
    Verification des identifiants + récupération des éléments de la classe
    """
    liste_lycee =  recuperation_noms_etablissements()
    return render_template("login.html", ma_variable=liste_lycee)

@app.route('/enigme1', methods=['GET', 'POST'])
def enigme1():
    """
    Gestion de la première enigme
    """
    def test(*args):
        """
        Effecute les tests de l'enigme
        """
        try:
        	resultat = 2 * args[0]
        except:
        	resultat = "La valeur passer en parametre est incorrect"
        return resultat

    if request.method == 'POST':
    	reponse = request.form.get("reponse")
    	test_value = request.form.get("test")
    	reponse_values = request.form.get("reponse")
    	
    	if reponse:
    		logging.info('Enregistrement de la réponse dans base de donnée')
    		test_result = "Reponse enregistée"
    		reponse_db(id_classe, reponse_values)
    		return render_template("enigme1.html", test_result="Résultat enregistée", final=True)
    	
    	else:
    		logging.info('On effectue un test')
    		test_result = test(test_value)
    		return render_template("enigme1.html", test_result=test_result, final=False)

    test_result = ""
    return render_template("enigme1.html", test_result=test_result, couleurs_d=VIOLETS_D)


@app.route('/enigme2', methods=["GET", "POST"])
def enigme2():
    """

    """
    def test():
        "effecute les tests de l'enigme"
        pass
    return render_template("enigme2.html")


@app.route('/enigme3')
def enigme3():
    """

    """
    if request == "POST":
        rep = request.form('final_rep') 
        if rep:
            update_db('enigme3', rep)
        else : 
            test = request.form('test')
            resultat = fonction_test('enigme3',test)
    pass


@app.route('/admin')
def admin():
    """

    """
@app.route('/WelcomeKaribou')
def Welcome_Karibou():
    liste = ["Joris_lapuissance", "Denis_jeunepapa", "Eric_absent", "Etienne_monsieurréférence", "Alan_maispourquoi"]
    return render_template('/ALAN.html', equipe = liste)

@app.route('/testdesignprojet')
def testdesignprojet():
    return render_template('testdesignprojet.html')

@app.route('/test')
def test():
	return render_template('carousel.html', couleurs = VIOLETS, couleurs_d = VIOLETS_D)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
