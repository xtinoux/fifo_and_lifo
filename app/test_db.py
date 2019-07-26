from sqlite3 import connect

# with connect(path_db) as conn:
#         cursor = conn.cursor()
#         cursor.execute("""SELECT etablissement FROM classes""")
#         liste_etab = cursor.fetchall()
# print(liste_etab)


class Outils_db():



    def __init__(self, path_db):
        """
        Initialise la base de données

        @arg {str} : 
        @return None 
        """
        self.path_db = path_db

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

    def get_lycee(self):
        """
        Renvoie la liste des lycees.

        @arg {objet} : self
        @return {list} : liste de dic cle lycee, id_classe, classe, password"""
        enigmes = []
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


def secret(nb_car=6):
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(nb_car))
    return password


if __name__ == '__main__':
    my_db = Outils_db("../static/db/fifoandlifo.db")
    for lycee,lycee_id in [("LPO de Sada","sada"), ("LPO de Kahani","kahani"), ("LPO Bamana","bamana"), ("LPO de Mamoudzou Nord","mdz-nord"), ("LPO de Petite Terre","petite-terre"), ("LPO du Nord","nord"), ("LPO de Chirongi","chirongui"), ("LPO de Brandélé","bandrele"), ("LPO de Dembeni","dembeni"), ("LPO de Kaweni","kaweni")]:
        for i in range(1, 4):
            my_db.add_lycee( id_classe=f"{lycee_id}-{i}",lycee=lycee, classe=f"NSI 0{i}", password=secret())

