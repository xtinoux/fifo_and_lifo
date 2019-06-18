from flask import Flask, render_template
from app.db_utils import recuperation_noms_etablissements


app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def hello_world():
	"""
	Page d'accueil, pour présenter le projet.

	"""
    return render_template("index.html")

@app.route('/login')
def login():
	"""
	Gestion du login de la classe
	Verification des identifiants + récupération des éléments de la classe
	"""
	liste_lycee =  recuperation_noms_etablissements()
	return render_template("login.html", ma_variable=liste_lycee)

@app.route('/enigme1')
def enigme1():
	"""
	Gestion de la première enigme

	"""
		def test():
		"""
		Effecute les tests de l'enigme

		"""
		pass
	
	pass

@app.route('/enigme2', methods=["GET", "POST"])
def enigme2():
	"""

	"""


	def test():
		"effecute les tests de l'enigme"
		pass

	if request.method = "POST"

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

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)