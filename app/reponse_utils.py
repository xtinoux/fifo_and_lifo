import time
import functools


def timer(fonction_a_decorer):
    """
    Timer qui envoie le temps d'execution de la fonction
    """
    @functools.wraps(fonction_a_decorer)
    def wrapper(*args, **kwargs):
        #lancement du timer
        debut = time.time()
        #execution de la fonction avec ces arguments
        result = fonction_a_decorer(*args, **kwargs)
        #fin du timer
        fin = time.time()

        return {"resultat":result, "timer":fin - debut}
    return wrapper
 
 
 


if __name__ == '__main__':
    pass