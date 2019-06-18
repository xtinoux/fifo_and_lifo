import sqlite3


def recuperation_noms_etablissements():
    ''' pas de parametre
    retourne la liste des etablissements
    qui sont dans la base (pour afficher le menu choix etablissement par exemple)
    enleve les doublons
    '''    
    conn = sqlite3.connect('static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT etablissement FROM classes""")
    liste_etab = cursor.fetchall()
    #print(liste_etab)
    conn.close()
    #print(liste_etab[1])
    liste = []
    #print(len(liste_etab))
    for i in range(len(liste_etab)):
        liste.append(liste_etab[i][0])
          
    return list(set(liste))   



def niveau_evolution_classe(identifiant):
    ''' pas de parametre
    retourne la liste des etablissements
    '''
    conn = sqlite3.connect('static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base


    cursor.execute(f"""SELECT id_classe, niveau_enigme, echec_reussite_date FROM evolution WHERE id_classe={identifiant} """)
    # formated string
    evolution = cursor.fetchall()
    #print(liste_etab)
    conn.close()

    return evolution


def get_enigme(enigme_uid):
    """
    recuperation des donnes de l'enigme sous forme d'un dictionnaire
    """
    pass


if __name__ == '__main__':
    
    etabs = recuperation_noms_etablissements()
    print(etabs)
    #print(niveau_evolution_classe(2))
    #print(niveau_evolution_classe(5))
    #print(niveau_evolution_classe(1))
    #print(niveau_evolution_classe(4))
    #print(niveau_evolution_classe(3))


  

