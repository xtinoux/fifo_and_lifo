from flask import Flask, request

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/formulaire/', methods=["GET","POST"])
def formulaire():
	"""ici on  traite le formulaire"""
	if request.method == 'POST' :
		nom = request.form.get("reponse")
		print(nom)
		return nom
	return render_template("form.html")