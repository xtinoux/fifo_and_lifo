import os
import sys


def nombre_mystere():
    """
    Proposition de fonction pour le nombre mystere de l'enigme

    @arg : Aucun
    @return {int} : Le nombre mystere
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
        """
        Evaluation de l'enigme 2

        @arg {str} : Le nombre proposé sous forme d'une chaine de caratères ( ou non) 
        @return {dic} : dictionnaire contenant les clés status :  echec/succés et  msg :  un message
        """
        try:
            nb_propose = int(nb_propose)
        except Exception as e:
            return {"reponse": nb_propose, "status": "echec", "msg": "Assurez vous de fournir un nombre entier (ou une chaine de caractère numérique)", "points":0}
        if nb_propose == 381654729:
            return {"reponse": nb_propose, "status": "succés", "msg": "Bravo, le nombre proposé est le bon", "points":5}
        if not len(str(nb_propose)) == 9:
            return {"reponse": nb_propose, "status": "echec", "msg": "Le nombre proposé ne contient pas le bon nombre de chiffres", "points":2}
        if "0" in str(nb_propose):
                return {"reponse": nb_propose, "status": "echec", "msg": f"Le nombre ne doit pas contenir de 0", "points":4}
        if not len(set(str(nb_propose))) == 9:
                return {"reponse": nb_propose, "status": "echec", "msg": "Le nombre proposé contient plusieur fois le même chiffre", "points":2}
        for i in range(0, 9):
            nb_test = int(nb_propose / 10**i)
            if nb_test % (9 - i):
                return {"reponse": nb_propose, "status": "echec", "msg": f"Le nombre composé des {9 - i} premiers chiffres du  nombre {nb_propose} n'est pas divisible par {9 - i}",  "points":2}
        return {"reponse":nb_propose, "status":"inconnu", "msg": "Cas particulier", "points":0}


if __name__ == '__main__':
    print("Recherche du nombre inconnu")
    nb=nombre_mystere()
    print(reponse_enigme2(nb))
