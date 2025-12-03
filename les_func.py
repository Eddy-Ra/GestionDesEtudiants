from tkinter import ttk, BOTH

import customtkinter

import pyttsx3
from io import BytesIO
import tkinter as tk
import sqlite3
from datetime import timedelta

from PIL import Image, ImageTk


def affliste():
    conn = sqlite3.connect('ma_base_de_donnees.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM listes')
    fenetre = tk.Tk()
    fenetre.title("IAE")
    fenetre.iconbitmap("img/logo.png")

    rows = cursor.fetchall()
    vsb = ttk.Scrollbar(fenetre, orient="vertical")
    hsb = ttk.Scrollbar(fenetre, orient="horizontal")

    # Configuration du style pour le Treeview
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))
    style.configure("Treeview", font=('Arial', 10))

    # Création d'un Treeview pour afficher les résultats
    tree = ttk.Treeview(fenetre, columns=("id", "nom", "prenoms", "genre", "classe", "age", "date", "tel", "photo"),
                        show='headings'
                        , yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.heading("id", text="id")
    tree.heading("nom", text="nom")
    tree.heading("prenoms", text="prenoms")
    tree.heading("genre", text="genre")
    tree.heading("classe", text="classe")
    tree.heading("age", text="age")
    tree.heading("date", text="genre")
    tree.heading("tel", text="tel")
    tree.heading("photo", text="photo")
    vsb.configure(command=tree.yview)
    hsb.configure(command=tree.xview)
    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill=BOTH)

    conn.close()
    fenetre.mainloop()


moteur = pyttsx3.init()
voices = moteur.getProperty('voices')
moteur.setProperty('voice', 'fr')
moteur.setProperty('rate', 165)


def parler(texte):
    moteur.say(texte)
    moteur.runAndWait()


def affempl(classe, annee):
    font1 = ('Helvetica', 17, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')

    fenetre = tk.Tk()
    fenetre.title(f"emplois du temps {classe}{annee}")
    fenetre.geometry("600x600+400+150")
    fenetre.config(bg='#001220')
    fenetre.minsize(1200, 400)
    fenetre.maxsize(1200, 400)

    conn = sqlite3.connect(f'emplois du temps/em_{classe}{annee}.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    table = cursor.fetchall()
    last_table = table[-1][0]
    print(table)
    cursor.execute(f"SELECT * FROM {last_table};")
    raws = cursor.fetchall()

    y = 0

    for raw in raws:
        d, f, l, m, me, j, v = raw
        lu = tk.Label(fenetre, text=f"Lundi", font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)
        ma = tk.Label(fenetre, text=f"Mardi", font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)
        mer = tk.Label(fenetre, text=f"Mercredi", font=font2, bg='#001220', fg='#fff', width=15, height=2,
                       relief=tk.GROOVE)
        jeu = tk.Label(fenetre, text=f"Jeudi", font=font2, bg='#001220', fg='#fff', width=15, height=2,
                       relief=tk.GROOVE)
        ven = tk.Label(fenetre, text=f"vendredi", font=font2, bg='#001220', fg='#fff', width=15, height=2,
                       relief=tk.GROOVE)

        lu.pack()
        ma.pack()
        mer.pack()
        jeu.pack()
        ven.pack()

        lu.place(x=150, y=40)
        ma.place(x=350, y=40)
        mer.place(x=550, y=40)
        jeu.place(x=750, y=40)
        ven.place(x=950, y=40)

        d = tk.Label(fenetre, text=f"{d}h", font=font2, bg='#001220', fg='#fff', width=5, height=2, relief=tk.GROOVE)
        f = tk.Label(fenetre, text=f"{f}h", font=font2, bg='#001220', fg='#fff', width=5, height=2, relief=tk.GROOVE)
        l = tk.Label(fenetre, text=l, font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)
        m = tk.Label(fenetre, text=m, font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)
        me = tk.Label(fenetre, text=me, font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)
        je = tk.Label(fenetre, text=j, font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)
        v = tk.Label(fenetre, text=v, font=font2, bg='#001220', fg='#fff', width=15, height=2, relief=tk.GROOVE)

        y = y + 1
        d.place(x=10, y=y * 50 + 50)
        f.place(x=83, y=y * 50 + 50)
        l.place(x=150, y=y * 50 + 50)
        je.place(x=350, y=y * 50 + 50)
        m.place(x=550, y=y * 50 + 50)
        me.place(x=750, y=y * 50 + 50)
        v.place(x=950, y=y * 50 + 50)

    fenetre.mainloop()


def apropos(prenoms, matiere):
    print("apropos")
    print(prenoms)
    fenetre = tk.Tk()
    fenetre.title(prenoms)
    fenetre.minsize(500, 500)
    fenetre.maxsize(500, 500)
    fenetre.config(bg='#001220')
    conn = sqlite3.connect(f'bd/{prenoms}_bd.db')
    bd = sqlite3.connect('ma_base_de_donnees.db')
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    curseur = bd.cursor()
    curseur.execute(f'SELECT * FROM listes')
    cursor1.execute(f'SELECT * FROM {prenoms}')
    cursor2.execute(f'SELECT * FROM presence')
    rows = cursor1.fetchall()
    rows1 = cursor2.fetchall()
    tab = curseur.fetchall()
    nm = 0
    nbpr = 0
    presentf = ""

    for row in rows1:
        temps, prenomsbd, nbpr, nbrabs = row
        if prenomsbd == f'{prenoms}':
            nbpr = nbpr
            presentf = temps
            nbrabs = nbrabs

    for row in tab:
        id, noms, prenoms, sexe, classe, age, date, tel, photo, annee = row
        if prenoms == f'{prenoms}':
            nm = id

    from datetime import datetime
    now = datetime.now()
    temp = now.strftime('%Y-%m-%d %H:%M:%S')

    for row in rows:
        id, noms, prenoms, genre, classe, age, date, tel, photo, annee = row
        cl = classe

        def affemple():
            affempl(cl, annee)

        im = BytesIO(photo)
        image_data = Image.open(im)
        image_data = image_data.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(image_data)
        frame = customtkinter.CTkLabel(fenetre, bg_color='#001220', fg_color='#0CC9A9', width=500, height=500,
                                       corner_radius=10)

        image_label = customtkinter.CTkButton(fenetre, text="", image=img, width=200, height=200,
                                              hover_color="#001218")
        image_label.pack(pady=20, padx=20)
        nom = tk.Label(fenetre, text=f"Name: {noms}", font=("Arial", 12), fg="white", bg='#001220', )
        prenoms = tk.Label(fenetre, text=f"Surname: {prenoms}", font=("Arial", 12), fg="white", bg='#001220')
        age = tk.Label(fenetre, text=f"Age: {age}", font=("Arial", 12), fg="white", bg='#001220')
        classe = tk.Label(fenetre, text=f"Classe: {classe}", font=("Arial", 12), fg="white", bg='#001220')
        num = tk.Label(fenetre, text=f"Serial number: {nm}", font=("Arial", 12), fg="white", bg='#001220')
        nbpr1 = tk.Label(fenetre, text=f"Number of attendance: {nbpr}", font=("Arial", 12), fg="white", bg='#001220')
        nbabs1 = tk.Label(fenetre, text=f"Number of absences: {nbrabs}", font=("Arial", 12), fg="white", bg='#001220')
        presentf1 = tk.Label(fenetre, text=f"Last presence: {presentf}", font=("Arial", 12), fg="white",
                             bg='#001220')
        presentnow = tk.Label(fenetre, text=f"New presence: {temp}", font=("Arial", 12), fg="white",
                              bg='#001220')
        st_btn = customtkinter.CTkButton(fenetre, text="See timetable", font=("arial", 20),
                                         text_color="#33050B",
                                         width=250, height=35, hover_color="#D80E29", fg_color="#0CC9A9",
                                         corner_radius=15, bg_color="#001218", command=affemple)

        st_btn.place(x=240, y=450)
        mat = tk.Label(fenetre, text=f"You must during: {matiere}", font=("Arial", 12), fg="white",
                       bg='#001220')

        image_label.pack()
        nom.pack()
        prenoms.pack()
        age.pack()
        classe.pack()
        num.pack()
        nbpr1.pack()
        nbabs1.pack()
        presentf1.pack()
        presentnow.pack()
        mat.pack()

        image_label.place(x=20, y=10)
        nom.place(x=20, y=215)
        prenoms.place(x=20, y=235)
        num.place(x=20, y=255)
        classe.place(x=20, y=275)
        age.place(x=20, y=295)
        nbpr1.place(x=20, y=317)
        nbabs1.place(x=20, y=340)
        presentf1.place(x=20, y=360)
        presentnow.place(x=20, y=380)
        mat.place(x=20, y=400)
        frame.mainloop()

    conn.close()
    bd.close()

    fenetre.mainloop()


def presence(prenoms, classe, anne):
    conn = sqlite3.connect(f'bd/{prenoms}_bd.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM presence')
    rows = cursor.fetchall()

    print("                           Prenoms               nbr de presences                  nbr  abs ")
    import datetime

    isaia = sqlite3.connect(f'emplois du temps/em_{classe}{anne}.db')

    isaia1 = isaia.cursor()

    matiere = ""
    isaia1.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    table = isaia1.fetchall()
    last_table = table[-1][0]

    date = datetime.datetime.now().weekday()
    print(date)
    # heure = datetime.datetime.now().hour
    heure = 7

    if 7 <= heure < 9:
        isaia1.execute(f'SELECT * FROM {last_table} LIMIT 1 OFFSET 0')
        tabim = isaia1.fetchone()
        matiere = tabim[date + 1]
    if 9 <= heure < 11:
        isaia1.execute(f'SELECT * FROM {last_table} LIMIT 1 OFFSET 1')
        tabim = isaia1.fetchone()
        matiere = tabim[date + 1]
    if 14 <= heure < 16:
        isaia1.execute(f'SELECT * FROM {last_table} LIMIT 1 OFFSET 2')
        tabim = isaia1.fetchone()
        matiere = tabim[date + 1]
    if 14 <= heure < 18:
        isaia1.execute(f'SELECT * FROM {last_table} LIMIT 1 OFFSET 3')
        tabim = isaia1.fetchone()
        matiere = tabim[date + 1]

    if 7 <= heure <= 11 or 14 <= heure <= 18:
        print(heure)
        if matiere != "":
            absences = 0
            lerabd = ""
            from datetime import datetime
            nb = 0
            for row in rows:
                temps, prenoms, nombres, absences = row
                nb = nombres
                lerabd = datetime.strptime(temps, '%Y-%m-%d %H:%M:%S')
                absences = absences
                print(temps, '  :', prenoms, "                  ", nombres, "                              ",
                      absences)  # taloha

            nouveaux_nombres = nb + 1
            now = datetime.now()
            temp = now.strftime('%Y-%m-%d %H:%M:%S')
            print("voici")
            print(temp, '  :', prenoms, "                  ", nouveaux_nombres, "                              ",
                  absences)
            lera_jerena_zao = now
            lera_bd = lerabd + timedelta(minutes=5)
            if lera_jerena_zao > lera_bd:
                cursor.execute('INSERT INTO presence(temps,prénoms,nombres,absence) VALUES (?,?,?,?)',
                               (temp, prenoms, nouveaux_nombres, absences))
                parler(f"en {temp}")
                parler(f"Monsieur {prenoms}, vous devez aller au cours {matiere} ")
                apropos(prenoms, matiere)
            else:

                print("veuiller ressayer ay deuxiem cours")
                parler("veuiller ressayer ay deuxiem cours")
                apropos(prenoms, matiere)
        else:
            matiere = "retour à la maison ou faire une pause"
            print("retour à la maison ou va faire une pause")
            parler(f"Monsieur {prenoms}, retour à la maison ou faire une pause ")
            apropos(prenoms, matiere)

    else:
        matiere = "retour à la maison ou faire une pause"
        print("retour à la maison ou va faire une pause")
        parler(f"Monsieur {prenoms}, retour à la maison ou va faire une pause ")
        apropos(prenoms, matiere)
    conn.commit()
    conn.close()


def voir_annonce():
    conn = sqlite3.connect('ma_base_de_donnees.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM annonces ORDER BY id DESC LIMIT 1')
    raws = curs.fetchone()
    root = tk.Tk()
    root.title("Annonce")
    label_titre = tk.Label(root, text="Titre:", font=("Helvetica", 20, "bold"))
    label_titre.pack(pady=10)
    text_contenu = tk.Text(root, wrap=tk.WORD, width=80, height=20, font=15)
    text_contenu.pack(pady=10)
    if raws:
        titre, contenu = raws[1], raws[2]
        label_titre.config(text=f'Titre: {titre}')
        text_contenu.delete(1.0, tk.END)
        text_contenu.insert(tk.END, contenu)
    print(raws)
    root.mainloop()


def ajouter_note(prenoms):#ajout des notes

    font1 = ('Helvetica', 17, 'bold')
    con=sqlite3.connect(f"bd/{prenoms}_bd.db")
    curs=con.cursor()
    curs.execute("SELECT * FROM Note")
    raw=curs.fetchall()
    print(raw)
    note = tk.Tk()
    note.title("Notes")
    note.minsize(500, 600)
    note.config(bg='#001220')
    tx_SD = customtkinter.CTkLabel(note, text='SD:', text_color='#0CC9A9',font=font1)
    tx_SD.place(x=30, y=30)
    tx_RO = customtkinter.CTkLabel(note, text='RO:', text_color='#0CC9A9', font=font1)
    tx_RO.place(x=30, y=70)
    tx_TC = customtkinter.CTkLabel(note, text='TC:', text_color='#0CC9A9', font=font1)
    tx_TC.place(x=30, y=110)
    tx_PH = customtkinter.CTkLabel(note, text='PHOTO:', text_color='#0CC9A9', font=font1)
    tx_PH.place(x=30, y=150)
    tx_MU = customtkinter.CTkLabel(note, text='MUSIC:', text_color='#0CC9A9', font=font1)
    tx_MU.place(x=30, y=190)
    tx_TAV = customtkinter.CTkLabel(note, text='TAV:', text_color='#0CC9A9', font=font1)
    tx_TAV.place(x=30, y=230)
    tx_JS = customtkinter.CTkLabel(note, text='JS:', text_color='#0CC9A9', font=font1)
    tx_JS.place(x=30, y=270)
    tx_LC = customtkinter.CTkLabel(note, text='LC:', text_color='#0CC9A9', font=font1)
    tx_LC.place(x=30, y=310)
    tx_MER = customtkinter.CTkLabel(note, text='MERISE:', text_color='#0CC9A9', font=font1)
    tx_MER.place(x=30, y=350)
    tx_ED = customtkinter.CTkLabel(note, text='ED:', text_color='#0CC9A9', font=font1)
    tx_ED.place(x=30, y=390)
    tx_PAO = customtkinter.CTkLabel(note, text='PAO:', text_color='#0CC9A9', font=font1)
    tx_PAO.place(x=30, y=430)
    tx_PHP = customtkinter.CTkLabel(note, text='PHP:', text_color='#0CC9A9', font=font1)
    tx_PHP.place(x=30, y=470)
    SD = customtkinter.CTkEntry(note, placeholder_text='SD',
                                   placeholder_text_color="#a3a3a3",
                                   text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                   border_width=2, width=80, height=35, corner_radius=35,font=font1)
    SD.place(x=80, y=29)
    RO = customtkinter.CTkEntry(note, placeholder_text='RO',
                                placeholder_text_color="#a3a3a3",
                                text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                border_width=2, width=80, height=35, corner_radius=35, font=font1)
    RO.place(x=80, y=69)
    TC = customtkinter.CTkEntry(note, placeholder_text='TC',
                                placeholder_text_color="#a3a3a3",
                                text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                border_width=2, width=80, height=35, corner_radius=35, font=font1)
    TC.place(x=80, y=109)
    PHOTO = customtkinter.CTkEntry(note, placeholder_text='PHOTO',
                                placeholder_text_color="#a3a3a3",
                                text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                border_width=2, width=80, height=35, corner_radius=35, font=font1)
    PHOTO.place(x=100, y=149)
    note.mainloop()


#ajouter_note("Eddy")
