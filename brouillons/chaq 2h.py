import tkinter as tk
import customtkinter
import sqlite3



# Créer la fenêtre principale



# Fonction pour afficher un message lorsqu'une case est cliquée)

font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')
fenetre = tk.Tk()
fenetre.title(f"emplois du temps ")
fenetre.geometry("500x500+400+150")
fenetre.minsize(600, 600)
fenetre.maxsize(600, 600)
fenetre.config(bg='#001220')
conn = sqlite3.connect(f'../emplois du temps/em_IMTICIA.db')
cursor = conn.cursor()
cursor.execute(f'SELECT * FROM emplois')
y = 0
for raw in cursor:
    d, f, l, m, me, j, v = raw

    for i in range(5):
        for j in range(4):
            bouton = tk.Button(fenetre, text=f"{d}h")
            bouton.grid(row=i, column=j, padx=10, pady=10)




# Créer une grille 3x3 de boutons

# Lancer la boucle principale
fenetre.mainloop()
