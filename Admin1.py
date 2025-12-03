import sqlite3
import subprocess
import sys
import tkinter as tk
from datetime import datetime
from io import BytesIO
from tkinter import ttk, messagebox, BOTH
import customtkinter
import cv2
from PIL import ImageTk, Image

from BD import annoncepb


font1 = ('Helvetica', 21, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

fenetre = tk.Tk()
fenetre.title("IAE")
fenetre.iconbitmap("img/logo.png")

screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()
rech = tk.StringVar()
global listbox


# Fonction pour lire la vidéo
def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (new_width, new_height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(image=frame)
        label.config(image=frame)
        label.image = frame
        label.after(10, play_video)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        play_video()


def return_to_reception():
    fenetre.destroy()
    recept_path = "main.py"
    subprocess.run([sys.executable, recept_path])


def update_time():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    heur = now.strftime('%H : %M : %S')
    date_lb = ttk.Label(fenetre, text=f"{date}")
    date_lb.configure(font=('Arial', 23), foreground="#055D2B", background="#C6EED1", width=10)
    date_lb.place(x=(screen_width / 2) - 80, y=screen_height / 18)
    heur_lb = ttk.Label(fenetre, text=f"{heur}")
    heur_lb.configure(font=('Arial', 23), foreground="#055D2B", background="#C6EED1", width=10)
    heur_lb.place(x=(screen_width / 2) - 80, y=screen_height / 10)
    fenetre.after(1000, update_time)


update_time()


def create_Button():
    img4 = customtkinter.CTkImage(Image.open("img/admin.png").resize((30, 30), Image.LANCZOS))
    img2 = customtkinter.CTkImage(Image.open("img/logo2.png").resize((30, 30), Image.LANCZOS))
    img3 = customtkinter.CTkImage(Image.open("img/clock.png").resize((30, 30), Image.LANCZOS))

    def enregistrer():
        fenetre.destroy()
        subprocess.run([sys.executable, 'inscription.py'])

    def retour():
        fenetre.destroy()
        subprocess.run([sys.executable, 'main.py'])

    def empl():
        fenetre.destroy()
        subprocess.run([sys.executable, 'changempl.py'])

    qt_btn = customtkinter.CTkButton(fenetre, text="RETURN", fg_color="#068962", font=("arial", 18), bg_color='#98e39f',
                                     hover_color="#012705", corner_radius=25, command=retour)
    qt_btn.place(x=screen_width - 200, y=screen_height - 100)

    note = customtkinter.CTkButton(fenetre, text="NOTE", fg_color="#068962", font=("arial", 18),
                                   bg_color='#98e39f',
                                   hover_color="#012705", corner_radius=4, command=enregistrer, width=250,
                                   height=40, image=img2)
    note.place(x=(screen_width / 2) - 120, y=screen_height - 550)
    register_btn = customtkinter.CTkButton(fenetre, text="REGISTERING", fg_color="#068962", font=("arial", 18),
                                           bg_color='#98e39f',
                                           hover_color="#012705", corner_radius=4, command=enregistrer, width=250,
                                           height=40, image=img2)
    register_btn.place(x=(screen_width / 2) - 120, y=screen_height - 650)
    edt_btn = customtkinter.CTkButton(fenetre, text="TIMETABLE", fg_color="#068962", font=("arial", 18),
                                      bg_color='#98e39f',
                                      hover_color="#012705", corner_radius=4, command=empl, width=250,
                                      height=40, image=img3)
    edt_btn.place(x=(screen_width / 2) - 120, y=screen_height - 450)

    def btnannonce():
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM annonces')
        rows = cursor.fetchall()
        fenetra = tk.Tk()
        vsb = ttk.Scrollbar(fenetra, orient="vertical")
        hsb = ttk.Scrollbar(fenetra, orient="horizontal")

        # Configuration du style pour le Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))
        style.configure("Treeview", font=('Arial', 10))

        # Création d'un Treeview pour afficher les résultats
        tree = ttk.Treeview(fenetra, columns=("rang", "nom", "annonce"), show='headings'
                            , yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.heading("rang", text="rang")
        tree.heading("nom", text="nom")
        tree.heading("annonce", text="anonce")

        vsb.configure(command=tree.yview)
        hsb.configure(command=tree.xview)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")

        if rows:
            for row in rows:
                tree.insert("", "end", values=row)
                print("ok")
                tree.pack(expand=True, fill=BOTH)
        fenetra.mainloop()

    annonce_btn = customtkinter.CTkButton(fenetre, text="ANNONCE", fg_color="#068962", font=("arial", 18),
                                          bg_color='#98e39f',
                                          hover_color="#012705", corner_radius=4, width=250, height=40, image=img4,command=btnannonce
                                          )
    annonce_btn.place(x=(screen_width / 2) - 120, y=screen_height - 350)
    annoce = tk.Text(fenetre, width=30, height=15, font=100, )
    annoce.place(x=(screen_width / 2) + 330, y=225)

    def annonce_ent():
        contenu = annoce.get("1.0", tk.END)
        annoncepb(contenu)
        messagebox.showinfo("Alerte", f"ok bro")




    partager = customtkinter.CTkButton(fenetre, 250, 40, 4, text="Partager", fg_color="#068962", font=("arial", 18),
                                       bg_color='#98e39f',
                                       hover_color="#012705", command=annonce_ent
                                       )
    partager.place(x=1140, y=580)


def search_database(event=None):
    query = rech.get()
    listbox.delete(0, tk.END)

    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()

    cursor.execute("SELECT prénoms FROM listes WHERE prénoms LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()

    if query:
        for result in results:
            listbox.insert(tk.END, result[0])

        if not results:
            listbox.insert(tk.END, f"{query} n'est pas dans la bd")

    listbox.bind("<Double-Button-1>", fill_entry)
    conn.close()


def fill_entry(event=None):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        rech.set(selected_item)


def affichage():
    query = rech.get()
    # apropos(query, "voir")


def create_frame():
    global listbox  # Déclarer la variable listbox comme globale
    frameG = customtkinter.CTkFrame(fenetre, width=400, height=500, corner_radius=5)
    frameG.place(x=100, y=140)

    frameP = customtkinter.CTkFrame(frameG, fg_color='#91D6A1', bg_color="#91D6A1", corner_radius=25, width=390,
                                    height=489)
    frameP.place(x=5, y=5)

    frameG1 = customtkinter.CTkFrame(fenetre, bg_color="#91D6A1", width=400, height=500, corner_radius=5)
    frameG1.place(x=(screen_width - 480), y=140)

    frameP1 = customtkinter.CTkFrame(frameG1, fg_color='#91D6A1', bg_color="#91D6A1", corner_radius=25, width=390,
                                     height=489)
    frameP1.place(x=5, y=5)

    canva = customtkinter.CTkCanvas(frameP, bg='gray16', width=380, height=480)
    filename = Image.open('bg/bg1rr.png')
    filename.resize((390, 490), Image.LANCZOS)
    pic = ImageTk.PhotoImage(filename)
    bg_lb = customtkinter.CTkLabel(frameP, image=pic, text='')
    bg_lb.place(x=0, y=0.3)
    canva.place(x=5, y=5)

    canva1 = customtkinter.CTkCanvas(frameP1, bg='gray16', width=380, height=480)
    filename1 = Image.open('bg/bg1rr.png')
    filename1.resize((390, 490), Image.LANCZOS)
    pic1 = ImageTk.PhotoImage(filename1)
    bg_lb1 = customtkinter.CTkLabel(frameP1, image=pic1, text='')
    bg_lb1.place(x=0, y=0.3)
    canva1.place(x=5, y=5)

    tt = customtkinter.CTkLabel(frameP1, text="ANNONCE", text_color="#012705", font=font1)
    tt.place(x=150, y=18)

    recherche = customtkinter.CTkEntry(frameG, bg_color="#91D6A1", fg_color="#E2F1E7", border_width=2,
                                       border_color='#055D2B', width=250, height=40,
                                       placeholder_text="Search.....", placeholder_text_color="#055D2B", font=font2,
                                       corner_radius=15, text_color="#677470", textvariable=rech)
    recherche.place(x=80, y=20)
    recherche.bind("<KeyRelease>", search_database)

    listbox = tk.Listbox(frameG, width=30, height=15, font=100)
    listbox.place(x=30, y=75)
    img1 = Image.open("img/search.png").resize((25, 25), Image.LANCZOS)
    icon1 = ImageTk.PhotoImage(img1)
    srbt = customtkinter.CTkButton(frameG, image=icon1, width=25, height=25, bg_color="#E2F1E7", text='',
                                   fg_color='#E2F1E7', hover_color='#81e39f', corner_radius=4,
                                   command=affichage)
    srbt.place(x=280, y=24)
    srbt.place(x=280, y=24)


# Chargement de la vidéo
video_path = "bg/SATURNE 2.mp4"
cap = cv2.VideoCapture(video_path)

# Récupération des dimensions de la vidéo
new_width = screen_width
new_height = screen_height

# Redimensionnement de la fenêtre principale et de la zone d'affichage de la vidéo
fenetre.geometry(
    f"{new_width}x{new_height}+{int((screen_width - new_width) - 4)}+{int((screen_height - new_height) / 2)}")

# Création de la zone d'affichage de la vidéo
video_frame = tk.Frame(fenetre, width=new_width, height=new_height)
video_frame.place(x=0, y=0)
label = tk.Label(video_frame)
label.place(x=-2, y=-2)

create_frame()
create_Button()
play_video()


fenetre.mainloop()
