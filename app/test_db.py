from sqlite3 import connect

path_db = "../static/db/fifoandlifo.db"
with connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT etablissement FROM classes""")
        liste_etab = cursor.fetchall()
print(liste_etab)