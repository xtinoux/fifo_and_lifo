texte = """bravo vous avez reussi a decrypter le message secret crypté par la methode de cesar.
ce codage comme vous pouvez le constater n'est pas tres efficace puisqu'une analyse de la repetition de la lettre la plus courante de la langue dans laquelle il a ete ecrit permet de connaitre le decallage.
les methodes de cryptages actuelles reposent plutot sur l'usage de cle privee - cle public.
"""

# Texte avec 2 erreurs et une lettre manquante
texte3 = """bravo vous avez reussi a decrypter le message secret crypté par la methode de cesar.
ce codage comme vous pouvez le constater n'est pas tres efficace puisqu'une analyse de la repetition de la lettre la plus courante de la langue dans laquelle il a ete ecrit permet de connaitre le decallage.
les methodes de cryptages actuelles reposent plutot sur l'usage de cle privee - cle prili.
"""

# Créaation d'une liste contenant les lettres de l'alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def crypter(texte, decallage=9, alphabet=alphabet):
    """
    Permet de crypter un texte avec la méthode de César

    @param (str) : texte en minuscule
    @param (int) : decallage
    @result (str) : texte crypté
    """
    alphabet_crypte = [alphabet[(i + decallage) % 26] for i in range(26)]
    texte_crypte = ""
    for i in texte:
        try:
            index_lettre = alphabet.index(i)
            texte_crypte += alphabet_crypte[index_lettre]
        except Exception as e:
            texte_crypte += i
    return texte_crypte


def decrypter(texte, alphabet=alphabet):
    """
    Décrypte un texte crypté à l'aide de la méthode de Cesar,
    en supposant que la lettre "e" soit la plus fréquente dans le texte

    @param (str) : texte crypté en minuscule
    @result (str) : texte décrypté en minuscule
    """
    occurences = [texte.count(lettre) for lettre in alphabet]
    index_max = occurences.index(max(occurences))
    decallage = 4 - index_max
    texte_decrypte = ""
    for lettre in texte:
        try:
            index_lettre = alphabet.index(lettre)
            texte_decrypte += alphabet[index_lettre + decallage]
        except Exception as e:
            texte_decrypte += lettre
    return texte_decrypte


def pourcentage_reussite(texte_reponse):
    nb_caracteres_original = len([lettre for lettre in texte])
    nb_caracteres_reponse = len([lettre for lettre in texte_reponse])
    nb_caracteres = min(nb_caracteres_original, nb_caracteres_reponse)
    print(nb_caracteres)
    caracteres_ok = 0
    for i in range(nb_caracteres):
        print(i)
        if texte[i].isalpha() and texte_reponse[i] == texte[i]:
            print(f"{texte[i]} == {texte_reponse[i]}")
            caracteres_ok += 1
        else:
            print(f"Attention {texte[i]}")
    print(caracteres_ok)
    nb_caracteres_alpha = len([lettre for lettre in texte if lettre.isalpha()])
    return {
      "nb_erreurs": nb_caracteres_alpha - caracteres_ok,
      "nb_caracteres_testes": nb_caracteres_alpha,
      "pourcentage_reussite": caracteres_ok / nb_caracteres_alpha * 100}


if __name__ == '__main__':
    texte_crypte = crypter(texte)
    print(texte_crypte)
    print("\n")
    print(decrypter(texte_crypte))
    print(pourcentage_reussite(texte3))
