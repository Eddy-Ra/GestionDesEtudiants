import sqlite3
from datetime import datetime


def convert_image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    return binary_data


def annoncepb(contenu):
    conn = sqlite3.connect('ma_base_de_donnees.db')
    curs = conn.cursor()

    date = datetime.now()
    print(date)
    # Créer un objet curseur
    curs.execute('''
                CREATE TABLE IF NOT EXISTS annonces (
                    id INTEGER PRIMARY KEY,
                    titre TEXT,
                    contenue TEXT,
                    date DATETIME
            )
        ''')
    curs.execute('INSERT INTO annonces (titre, contenue,date) VALUES (?,?, ?)', ("Annoce", contenu, date))
    conn.commit()

    conn.close()


def enregister(name, prenoms, genre, classe, age, date, tel, img, annee):
    conn = sqlite3.connect('ma_base_de_donnees.db')

    # Créer un objet curseur
    cursor = conn.cursor()
    # Créer une table 'utilisateurs' avec un champ pour stocker l'image
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listes (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            prénoms TEXT,
            genre TEXT,
            classe TEXT,
            âge INTEGER,
            date TEXT,
            tel INTEGER,
            photo BLOB,
            annee TEXT
    )
''')
    cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {classe}{annee} (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            prénoms TEXT,
            genre TEXT,
            classe TEXT,
            âge INTEGER,
            date TEXT,
            tel INTEGER,
            photo BLOB,
            annee TEXT
                
        )
    ''')

    nom_utilisateur = name
    prenom = prenoms
    age_utilisateur = int(age)
    chemin_image = img

    photo_utilisateur = convert_image_to_binary(chemin_image)
    cursor.execute('INSERT INTO listes (nom, prénoms,genre,classe,âge,date,tel, photo,annee) VALUES (?, ? , ?,?,?, ?,'
                   '?,?,?)',
                   (nom_utilisateur, prenom, genre, classe, age_utilisateur, date, tel, photo_utilisateur, annee))

    cursor.execute(f'INSERT INTO {classe}{annee} (nom, prénoms,genre,classe,âge,date,tel, photo,annee) VALUES (?, ? ,?, ?,'
                   '?, ?,'
                   '?,?,?)',
                   (nom_utilisateur, prenom, genre, classe, age_utilisateur, date, tel, photo_utilisateur, annee))

    conn.commit()

    conn.close()


def etudiantsbd(name, prenoms, genre, classe, age, date, tel, img, present, annee):
    conn = sqlite3.connect(f'bd/{prenoms}_bd.db')

    # Créer un objet curseur
    cursor = conn.cursor()

    # apropos
    cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {prenoms} (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            prénoms TEXT,
            genre TEXT,
            classe TEXT,
            âge INTEGER,
            date TEXT,
            tel INTEGER,
            photo BLOB,
            annee TEXT
        )
    ''')
    # presence
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS presence(
                temps DATETIME,
                prénoms TEXT,
                nombres INTEGER,
                absence INTEGER)
    ''')
    # emplois
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS emplois(
                debut INTEGER,
                fin INTEGER,
                lundi TEXT,
                mardi TEXT,
                mercrediTEXT,
                jeudi TEXT,
                vendredi TEXT)
    ''')
    # notes
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Note(
                    id INTEGER PRIMARY KEY,
                    SD INTEGER,
                    RO INTEGER,
                    TC INTEGER,
                    PHOTO INTEGER,
                    MUSIC INTEGER,
                    TAV INTEGER,
                    JS INTEGER,
                    LC INTEGER,
                    MERISE INTEGER,
                    ED INTEGER,
                    PAO INTEGER,
                    PHP INTEGER,
                    Date DATETIME)
                    
        ''')
    nom_utilisateur = name
    prenom = prenoms
    age_utilisateur = int(age)
    chemin_image = img
    classes = classe
    presence = present
    absence = 0
    from datetime import datetime

    now = datetime.now()
    temp = now.strftime('%Y-%m-%d %H:%M:%S')

    photo_utilisateur = convert_image_to_binary(chemin_image)

    cursor.execute(
        f'INSERT INTO {prenom} (nom, prénoms,genre,classe,âge,date,tel, photo,annee) VALUES (?,?, ? , ?,?, ?,?,?,?)',
        (nom_utilisateur, prenom, genre, classe, age_utilisateur, date, tel, photo_utilisateur, annee))

    cursor.execute('INSERT INTO presence(temps,prénoms,nombres,absence) VALUES (?,?,?,?)',
                   (temp, prenom, presence, absence))
    cursor.execute(
        'INSERT INTO Note (SD, RO, TC, PHOTO, MUSIC, TAV, JS, LC, MERISE, ED, PAO, PHP,Date) VALUES (?, ?, ?, ?, ?, '
        '?, ?,?, ?, ?, ?, ?,?)',
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, now))

    conn1 = sqlite3.connect(f'emplois du temps/em_{classe}{annee}.db')
    cursor1 = conn1.cursor()
    cursor1.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    table = cursor1.fetchall()
    last_table = table[-1][0]

    cursor1.execute(f"SELECT * FROM {last_table};")

    data = cursor1.fetchall()
    cursor.executemany('INSERT INTO emplois VALUES (?,?,?,?,?,?,?)',
                       data)

    conn.commit()
    conn1.commit()

    conn.close()


def nouvempl(lundi, mardi, mercredi, jeudi, vendredi, classe, annee):
    conn = sqlite3.connect(f'emplois du temps/em_{classe}{annee}.db')
    curs = conn.cursor()
    # Utilisation de la date et l'heure pour générer un identifiant unique
    id_unique = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_table = f'emplois_{id_unique}'
    d = [7, 9, 14, 16]
    f = [9, 11, 16, 18]

    curs.execute(
        f'''CREATE TABLE IF NOT EXISTS {nom_table}(
                d TEXT,
                f TEXT,
                lundi TEXT,
                mardi TEXT,
                mercredi TEXT,
                jeudi TEXT,
                vendredi TEXT)'''
    )
    for i in range(max(len(d), len(f), len(lundi), len(mardi), len(mercredi), len(jeudi), len(vendredi))):
        curs.execute(
            f'INSERT INTO "{nom_table}" (d, f, lundi, mardi, mercredi, jeudi, vendredi) VALUES (?,?,?,?,?,?,?)',
            (d[i] if i < len(d) else None,
             f[i] if i < len(f) else None,
             lundi[i] if i < len(lundi) else None,
             mardi[i] if i < len(mardi) else None,
             mercredi[i] if i < len(mercredi) else None,
             jeudi[i] if i < len(jeudi) else None,
             vendredi[i] if i < len(vendredi) else None))

    conn.commit()  # Assurez-vous de committer les changements
    conn.close()


def hampiditranote(prenoms, SD, RO, TC, PHOTO, MUSIC, TAV, JS, LC, MERISE, ED, PAO, PHP):
    conn = sqlite3.connect(f'bd/{prenoms}_bd.db')
    curs = conn.cursor()
    date = datetime.now()
    # Créer un objet curseur
    curs.execute(
        'INSERT INTO Note (SD,RO,TC,PHOTO,MUSIC,TAV,JS,LC,MERISE,ED,PAO,PHP,Date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,)',
        (SD, RO, TC, PHOTO, MUSIC, TAV, JS, LC, MERISE, ED, PAO, PHP, date))
    conn.commit()

    conn.close()
