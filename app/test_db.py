from sqlite3 import connect

# with connect(path_db) as conn:
#         cursor = conn.cursor()
#         cursor.execute("""SELECT etablissement FROM classes""")
#         liste_etab = cursor.fetchall()
# print(liste_etab)


class Outils_db():
    def __init__(self, path_db):
        self.path_db = path_db

    def recuperation_enigme(self):
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

    def update_enigme(self):
        with connect(self.path_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT  FROM enigmes""")

if __name__ == '__main__':
    my_db = Outils_db("../static/db/fifoandlifo.db")
    print(my_db.recuperation_enigme())
