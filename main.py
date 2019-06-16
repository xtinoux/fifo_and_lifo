 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.login('/login')
def login():
	"""
	Gestion du login de la classe
	Verification des identifiants + récupération des éléments de la classe
	"""
	pass

@app.enigme1('/enigme1')
def enigme1():
	"""
	Gestion de la première enigme

	"""
	pass

@app.enigme2('/enigme2')
def enigme2():
	"""

	"""
	pass

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)