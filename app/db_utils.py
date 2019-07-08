
import sqlite3
from random import randint

chemin = 'static/db/fifoandlifo.db'


def recuperation_noms_etablissements():
    ''' pas de parametre
    retourne la liste des établissements sans répétition d'élémént
    exemple utilisation
    print(recuperation_noms_etablissements())
    donne ['Lycée du Nord (Acoua)', 'Lycée de Sada', 'Lycée de Kahani']
    meme si il y a deux classes au lyvée de sada
    '''    
    conn = sqlite3.connect(chemin)
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
    Sous forme de dictionnaire, donne les etablissements puis toutes les classes de ces etablissements
    la clef du dictionnaire est le nom de l etablissement et la donnee correspondante est une liste avec les classes NSI de
    l'etablissemment 
    pourra etre utilisé pour les menus deroulants
    exemple
    print(recuperation_etab_et_classes())
    donne
    {'Lycée de Sada': ['NSI01', 'NSI02', 'NSI03'], 'Lycée de Kahani': ['NSI01', 'NSI02'], 'Lycée du Nord (Acoua)': ['NSI01']}
    '''    
    
    conn = sqlite3.connect(chemin)
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT etablissement,classe FROM classes""")
    liste_etab = cursor.fetchall()    # contient tous les établissements.
    conn.close()
    dico_etab = {}

    for i in range(len(liste_etab)):    # creont un dictionnaire vide des etablissements avec des listes vides
        dico_etab[liste_etab[i][0]] =  []

    for i in range(len(liste_etab)):
        dico_etab[liste_etab[i][0]].append(liste_etab[i][1])
    
    return dico_etab


def lecture_de_la_base():
    ''' fonction qui donne toute la base de donnees
    a utiliser avec parcimonie si la base est immense
    '''
    conn = sqlite3.connect(chemin)
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT * FROM classes""")
    liste_etab = cursor.fetchall()
    conn.close()
    return liste_etab


def reccup_identifiant(etablissement,classe):
    ''' fonction inetrne non utilisée par les utilisateurs
    donne l'identifiant etant donné un etablissement et une classe dans cet etablissement
    '''
    conn = sqlite3.connect(chemin)
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT identifiant,etablissement,classe FROM classes WHERE etablissement = ? AND classe = ?""", (etablissement,classe,))
    liste_etab = cursor.fetchone()
    conn.close()
    return(liste_etab[0])



def insertion_reponse_db(identifiant,num_enigme,reponse):
    ''' etant donné identifiant= integer  et num_enigme= integer pour l instant 1, 2 ou 3
    insere la reponse dans la base de donnée pour l'enigme numero num_enigme
    de plus valide la reponse par un True dans la base pour indiquer que l'enigme a ete effectuee
    '''
    conn = sqlite3.connect(chemin)
    cursor = conn.cursor()      #  definie un curseur(pointeur) qui parcours la base
   
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
    


def identification(identifiant,mdp):
    ''' repond false si le mdp affilié a l'identifiant est correct
    '''
    
    conn = sqlite3.connect(chemin)
    cursor = conn.cursor() #  definie un curseur(pointeur) qui parcours la base
    cursor.execute("""SELECT identifiant,mdp FROM classes WHERE identifiant = ?""", (identifiant,))
    liste_etab = cursor.fetchone()    # contient tous les établissements.
    conn.close()
    print(liste_etab)
    #print((liste_etab[1])
    print(mdp)
    if mdp == str(liste_etab[1]):
        return {identifiant: True}
    else:
        return {identifiant: False}
        


def raz_reponses_db():
    ''' RAZ de la base
    '''
    
    conn = sqlite3.connect(chemin)
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
    cela permet de voir l'evolution d un groupe dans le rallye des trois enigmes
    identifiant est la clef de la base de donnees (etablissement, classe) 
    compteur est une liste qui donne une liste de boolean
    False = non fait
    True = fait
    ''' 
    compteur = [False,False,False]   # pour l'instant il y trois enigmes non accessible
    valeur = 0

    conn = sqlite3.connect(chemin)
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




if __name__ == '__main__':
    chemin = '../static/db/fifoandlifo.db'
    print(recuperation_etab_et_classes())
    print(recuperation_noms_etablissements())
    print(reccup_identifiant('Lycée de Sada','NSI02'))
    print(reccup_identifiant('Lycée de Sada','NSI01'))
    print(reccup_identifiant('Lycée de Sada','NSI03'))
    print(reccup_identifiant('Lycée de Kahani','NSI01'))

    # print(enigmes_disponibles(4))
    # raz_reponses_db()
    # print(enigmes_disponibles(4))