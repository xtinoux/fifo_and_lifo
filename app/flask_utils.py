"""
Ensemble des décorateurs utiles pour le serveur
    - login_as : Gére les authentifications
    - enigme_open : Définie si une  enigme est valide
    - ...
"""
import functools
from flask import   Flask,\
                    render_template,\
                    request,\
                    flash, redirect,\
                    url_for,\
                    jsonify,\
                    session


def login_as(user_type, redirection="auth_individuel"):
    """
    Décorateur qui gère l'authentification des pages demandées.
    Les utilisateurs de type "admin" sont toujours autorisés.

    @param {str} : Ensemble des types d'authentification autorisée 
        exemple : rallye, eleve, prof
    """
    permissions = ["admin"]
    permissions.extend(user_type)
    def decorateur(fonction_a_decorer):
        @functools.wraps(fonction_a_decorer)
        def wrapper(*args, **kwargs):
            # On teste si session['type'] n'est pas disponible
            try:
                print(session)
                if session['type'] in permissions:
                # Execution de la fonction avec ces arguments
                    return fonction_a_decorer(*args, **kwargs)
                else :
                    print("Vous n'avez pas la permission d'acceder à cette page")
                    return redirect(url_for(redirection))
            except Exception as e:
                print(e)
                print("Vous n'êtes pas logger, il faut s'authentifier en premier")
                return redirect(url_for(redirection))            #fin du timer
        return wrapper
    return decorateur