import sqlite3


def recuperation_noms_etablissements():
    ''' pas de parametre
    retourne la liste des etablissements
    '''    
    conn = sqlite3.connect('fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT etablissement FROM classes""")
    liste_etab = cursor.fetchall()
    #print(liste_etab)
    conn.close()
    return liste_etab   



def niveau_evolution_classe(identifiant):
    ''' pas de parametre
    retourne la liste des etablissements
    '''
    
    
    conn = sqlite3.connect('fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT etablissement FROM classes""")
    liste_etab = cursor.fetchall()
    #print(liste_etab)
    conn.close()
    return liste_etab   


#print(recuperation_noms_etablissements())  

if __name__ == '__main__':
    etabs = recuperation_noms_etablissements()
    print(etabs)
    print(recuperation_noms_etablissements())


  

