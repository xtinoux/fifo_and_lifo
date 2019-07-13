import time
import functools


def timer(fonction_a_decorer):
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

def login_as(*args):
    def decorateur(fonction_a_decorer):
        @functools.wraps(fonction_a_decorer)
        def wrapper(*args, **kwargs):
            #lancement du timer
            try:
                if session['type'] in ["admin", uid]:
            #execution de la fonction avec ces arguments
                    result = fonction_a_decorer(*args, **kwargs)
                    return result
                else :
                    return render_template("login.html")
            except:
                return render_template("login.html")            #fin du timer
            return result, fin - debut
        return wrapper


@timer
def fonction_qui_prend_son_temps():
    time.sleep(1)


if __name__ == '__main__':
    print(fonction_qui_prend_son_temps()[1])