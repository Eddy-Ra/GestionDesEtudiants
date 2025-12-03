import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('ma_base_de_donnees.db')
cursor = conn.cursor()

# Fonction pour rechercher un nom dans la base de données


while True:
    prénoms = input("Entrez un nom (ou 'exit' pour quitter) : ")
    cursor.execute("SELECT * FROM listes WHERE prénoms = ?", (prénoms,))
    resultats = cursor.fetchone()

    if resultats:
        print("Résultats de la recherche :")
        print(resultats)
    else:
        print("Aucun résultat trouvé pour ce nom.")

    conn.close()
