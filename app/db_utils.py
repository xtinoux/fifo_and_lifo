


import sqlite3
from random import randint



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



def recuperation_etab_et_classes():
    ''' 
    Sous forme de dictionnaire, donne un etablissement puis toutes les classes de cet etablissement
    la clef est le nom de l etablissement et la donnee correspondante est une liste avec les classes NSI 
    l'etablissemment 



    en cours de fabrication .......

    '''    
    
    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT etablissement,classe FROM classes""")
    liste_etab = cursor.fetchall()    # contient tous les établissements.
    #print(liste_etab)
    conn.close()
    dico_etab = {}

    for i in range(len(liste_etab)):    # creont un dictionnaire vide des etablissements avec des listes vides
        dico_etab[liste_etab[i][0]] =  []


    # aux =  dico_etab[liste_etab[0][0]]
    # print(aux)
    # aux.extend(['d'])   
    # print(aux)
    #print(dico_etab)
    # print(dico_etab[liste_etab[1][0]])
    # dico_etab[liste_etab[1][0]] = { liste_etab[5][1], liste_etab[4][1] }
    # print(dico_etab)
    # dico_etab[liste_etab[1][0]] = {5,'r','d'}
    #dico_etab[liste_etab[1][0]].append({'f'})
    #print(dico_etab)
    for i in range(len(liste_etab)):
        dico_etab[liste_etab[i][0]].append(liste_etab[i][1])
        print(dico_etab[ liste_etab[i][0] ])
        print(liste_etab[i][1])
    print(liste_etab)
    print(dico_etab)
    
    #return list(set(liste))


def lecture_de_la_base():
    '''  '''

    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    print(cursor)
    # for l in cursor:
    #     print(l)
    conn.close()

def insertion_reponse_db(identifiant,num_enigme,reponse):
    ''' etant donné identifiant= integer  et num_enigme= integer pour l instant 1, 2 ou 3
    insere la reponse dans la base de donnée pour l'enigme numero num_enigme
    de plus valide la reponse par un True dans
    '''
    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
   
    if num_enigme == 1:
        cursor.execute("""UPDATE classes SET reponse01 = ? WHERE identifiant = ?""", (reponse,identifiant))
        cursor.execute("""UPDATE classes SET enigme01_effectuee = ? WHERE identifiant = ?""", (1,identifiant))
    if num_enigme == 2:
        cursor.execute("""UPDATE classes SET reponse02 = ? WHERE identifiant = ?""", (reponse,identifiant))   
        cursor.execute("""UPDATE classes SET enigme02_effectuee = ? WHERE identifiant = ?""", (1,identifiant))
    if num_enigme == 3:
        cursor.execute("""UPDATE classes SET reponse03 = ? WHERE identifiant = ?""", (reponse,identifiant))   
        cursor.execute("""UPDATE classes SET enigme03_effectuee = ? WHERE identifiant = ?""", (1,identifiant))     
    conn.commit()
  
    conn.close()
    




def raz_reponses_db():
    ''' RAZ
    '''
    
    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    for i in range (1,7):        
            
            cursor.execute("""UPDATE classes SET reponse01 = ? WHERE identifiant = ?""", ('',i))
            cursor.execute("""UPDATE classes SET reponse02 = ? WHERE identifiant = ?""", ('',i))
            cursor.execute("""UPDATE classes SET reponse03 = ? WHERE identifiant = ?""", ('',i))
            cursor.execute("""UPDATE classes SET enigme03_effectuee = ? WHERE identifiant = ?""", (0,i)) 
            cursor.execute("""UPDATE classes SET enigme02_effectuee = ? WHERE identifiant = ?""", (0,i))
            cursor.execute("""UPDATE classes SET enigme01_effectuee = ? WHERE identifiant = ?""", (0,i))
    conn.commit()
  
    conn.close()
    
def enigmes_disponibles(identifiant):
    ''' donne les enigmes disponibles pour un groupe donné.
    groupe (etablissement, classe) 
    compteur est une liste qui donne une liste de boolean
    False = non fait
    True = fait
    ''' 
    compteur = [False,False,False]   # pour l'instant il y trois enigmes
    valeur = 0

    conn = sqlite3.connect('../static/db/fifoandlifo.db')
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT enigme01_effectuee FROM classes WHERE identifiant = ?""",(identifiant,))
    valeur  = cursor.fetchone()
    if valeur[0] == 1:
        compteur[0] = True
    cursor.execute("""SELECT enigme02_effectuee FROM classes WHERE identifiant = ?""",(identifiant,))
    valeur  = cursor.fetchone()
    if valeur[0] == 1:
        compteur[1] = True    
    cursor.execute("""SELECT enigme03_effectuee FROM classes WHERE identifiant = ?""",(identifiant,))
    valeur  = cursor.fetchone()
    if valeur[0] == 1:
        compteur[2] = True    


    conn.close()
    
          
    return compteur   






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




if __name__ == '__main__':


    recuperation_etab_et_classes()
    
    # etabs = recuperation_noms_etablissements()
    
    # print(etabs)

    # print(niveau_evolution_classe(3))
    # print(niveau_evolution_classe(1))
    # print(niveau_evolution_classe(4))
    # print(niveau_evolution_classe(2))
    

    # rep = 'c est cool on a reussi'
    # insertion_reponse_db(5,2,rep)
    # raz_reponses_db()
    # for i in range (1,7):
    #     print(enigmes_disponibles(i))

    # lecture_de_la_base()

    # lecture_de_la_base()

    # for i in range (1,7):
        
    #     for j in range(1,4):
    #         rep = 'rép'+ str(randint(0,100))
    #         insertion_reponse_db(i,j,rep)

    # for i in range (1,7):
    #     print(enigmes_disponibles(i))
    #     