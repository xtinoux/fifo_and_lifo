

import sqlite3




def recuperation_noms_etablissements():
    ''' pas de parametre
    retourne la liste des établissements sans répétition d'élémént
    '''    
    conn = sqlite3.connect('../static/db/fifoandlifo.db')
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







def insertion_reponse_db(identifiant,num_enigme,reponse):
    ''' etant donné identifiant= integer et num_enigme= integer
    insere la reponse dans la base de donnée
    '''
    
    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    #cursor.execute("""INSERT INTO classes  (identifiant,reponse01) VALUES (?,?) """,(identifiant,reponse))
    cursor.execute("""UPDATE classes SET reponse01 = ? WHERE identifiant = ?""", (reponse,identifiant))
    conn.commit()
    #cursor.execute(f"""SELECT evolution FROM classes WHERE identifiant = ? """, (identifiant,))
    # formated string
    #evolution = cursor.fetchone()
    conn.close()
    

# def incrementation(identifiant):
#     ''' incremente le numero de l'enigme'''


def reponse_db(identifiant,numero_enigme,reponse):
    ''' identifiant est un integer
    numero_enigme est une integer
    reponse est un texte'''




def niveau_evolution_classe(identifiant):
    ''' etant donné un etablissement et une classe
    retourne le numero de l'enigme en cours
    '''
    evolution = 0
    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute(f"""SELECT evolution FROM classes WHERE identifiant = ? """, (identifiant,))
    # formated string
    evolution = cursor.fetchone()
    conn.close()
    return evolution[0]


# def incrementation_niveau(etablissement,classe):
#     ''' a faire fonction qui incremente le niveau suite a une reponse'''
#     conn = sqlite3.connect('../static/db/fifoandlifo.db')
#         cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
#         cursor.execute(f"""SELECT evolution FROM classes WHERE etablissement = ? AND classe = ?""", (etablissement,classe))
#         # formated string
#         evolution = cursor.fetchone()
#         #print(liste_etab)
#         conn.close()



if __name__ == '__main__':
    
    etabs = recuperation_noms_etablissements()
    
    print(etabs)
    

    print(niveau_evolution_classe(3))
    print(niveau_evolution_classe(1))
    print(niveau_evolution_classe(4))
    print(niveau_evolution_classe(2))


    rep = 'bonsoir'
    insertion_reponse_db(4,1,rep)
    #print(niveau_evolution_classe('Lycée de Sada','NSI01'))
    #print(niveau_evolution_classe('Lycée de Sada','NSI02'))


  

