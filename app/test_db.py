from sqlite3 import connect
import json 

class Outils_db():

    def __init__(self, path_db):
        """
        Initialise la base de données

        @arg {str} : 
        @return None 
        """
        self.path_db = path_db

    ##################################
    # Méthode de création
    ##################################


    ##################################
    # Méthode d'initialisation
    ##################################

    def init_table_lycee(self):
        for lycee,lycee_id in [("LPO de Sada","sada"), ("LPO de Kahani","kahani"), ("LPO Bamana","bamana"), ("LPO de Mamoudzou Nord","mdz-nord"), ("LPO de Petite Terre","petite-terre"), ("LPO du Nord","nord"), ("LPO de Chirongi","chirongui"), ("LPO de Brandélé","bandrele"), ("LPO de Dembeni","dembeni"), ("LPO de Kaweni","kaweni")]:
            for i in range(1, 4):
                self.add_lycee( id_classe=f"{lycee_id}-{i}",lycee=lycee, classe=f"NSI 0{i}", password=secret())

    ##################################
    # Méthode de recuperation        #
    ##################################
    def get_enigmes(self):
        """
        Renvoie la liste des enigmes.

        @arg {objet} : self
        @return {list} : liste de dic cle id_enigme, resume, niveau, langage, titre
        """
        enigmes = []
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT id_enigme, resume, niveau, langage, titre FROM enigmes""")
            datas = cursor.fetchall()
            for data in datas:
                enigmes.append({'id_enimge': data[0],
                    'resume': data[1],
                    'niveau': data[2],
                    'langage': data[3],
                    'titre': data[4]})
        return enigmes

    def get_lycees(self):
        """
        Renvoie la liste des lycees.

        @arg {objet} : self
        @return {list} : liste de dic cle lycee, id_classe, classe, password"""
        lycees = []
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT id_classe, lycee, classe, password FROM lycee""")
            datas = cursor.fetchall()
            for data in datas:
                lycees.append({'id_classe': data[0],
                    'lycee': data[1],
                    'classe': data[2],
                    'password': data[3]})
        return lycees

    def get_classe_by_lycee(self):
        """
        Renvoie la liste des lycees sans doublons avec la liste des classes .

        @arg {objet} : self
        @return {list} : liste de dic || cle:lycee -> nom du lycée, cle:classes  liste de dic  classe et id_classe"""
        lycees = []
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT lycee FROM lycees""")
            datas = set(cursor.fetchall())
            for lycee in datas:
                tmp_classes = []
                cursor.execute("""SELECT id_classe, classe FROM lycees WHERE lycee = ?""",lycee)
                classes = cursor.fetchall()
                for classe in classes:
                    tmp_classes.append({'id_classe': classe[0],'classe': classe[1]})
                lycees.append({"lycee":lycee[0], "classes":tmp_classes})
        return lycees

    def update_enigme(self):
        """
        Mets à jour la base de donnes

        """
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT  FROM enigmes""")

    def add_lycee(self,id_classe,lycee,classe,password):
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO lycees (id_classe, lycee, classe, password) VALUES (?,?,?,?)''',(id_classe, lycee,classe,password,))
            conn.commit()

    def create_table_classe():
        """
        Creer une table dans la base de données spécifique à la classe
        pour contenir les réponses des énigmes.
        """
        pass

    def auth_by_idclasse(self, id_classe, password):
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT   password FROM lycees WHERE id_classe = ? """,(id_classe,))
            pswd = cursor.fetchone()[0]
        if password == pswd:
            return True
        return False         

def secret(nb_car=6):
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(nb_car))
    return password



if __name__ == '__main__':
    my_db = Outils_db("../static/db/fifoandlifo.db")
    print(my_db.auth_by_idclasse("sada-1","dsds"))
    print(my_db.auth_by_idclasse("sada-1","nKrQqq"))

