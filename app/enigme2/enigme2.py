import os
import sys
try:
    from reponse_utils import *
except Exception as e:
    # Ajout du répértoire parent au chemin.
    currentdir = os.getcwd()
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    from reponse_utils import *


def nombre_mystere():
    """
    Fonction qui renvoie le nombre mystere de l'enigme

    @arg : Aucun
    @return : int -> Le nombre mystere
    """
    for nb_possible in range(123456789, 987654322):
        if "0" in str(nb_possible) or not str(nb_possible)[4] == '5' or not len(set(str(nb_possible))) == 9:
            continue
        counter = 0
        for i in range(0, 9):
            nb_test = int(nb_possible / 10**i)
            if not nb_test % (9 - i):
                counter += 1
            else:
                break
        if counter == 9:
            return nb_possible


def reponse_enigme2(nb_propose):
        try:
            nb_propose = int(nb_propose)
        except Exception as e:
            return {"reponse": nb_propose, "status": "echec", "msg": "Assurez vous de fournir un nombre entier (ou une chaine de caractère numérique)"}
        if nb_propose == 381654729:
            return {"reponse": nb_propose, "status": "succés", "msg": "Bravo, le nombre proposé est le bon"}
        if not len(str(nb_propose)) == 9:
            return {"reponse": nb_propose, "status": "echec", "msg": "Le nombre proposé ne contient pas le bon nombre de chiffres"}
        if "0" in str(nb_propose):
                return {"reponse": nb_propose, "status": "echec", "msg": f"Le nombre ne doit pas contenir de 0"}
        if not len(set(str(nb_propose))) == 9:
                return {"reponse": nb_propose, "status": "echec", "msg": "Le nombre proposé contient plusieur fois le même chiffre"}
        for i in range(0, 9):
            nb_test = int(nb_propose / 10**i)
            if nb_test % (9 - i):
                return {"reponse": nb_propose, "status": "echec", "msg": f"Le nombre composé des {9 - i} premiers chiffres du  nombre {nb_propose} n'est pas divisible par {9 - i}"}


# @pep8
@timer
def code_enigme2(fonction):
    return fonction


if __name__ == '__main__':
    print(code_enigme2(nombre_mystere()))
