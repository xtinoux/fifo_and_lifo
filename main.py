from flask import Flask
from db_utils import recuperation_noms_etablissements


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
	"""
	Gestion du login de la classe
	Verification des identifiants + récupération des éléments de la classe
	"""
	etablissements = get_etab()
	pass

@app.route('/enigme1')
def enigme1():
	"""
	Gestion de la première enigme

	"""
	pass

@app.route('/enigme2')
def enigme2():
	"""

	"""
	pass


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