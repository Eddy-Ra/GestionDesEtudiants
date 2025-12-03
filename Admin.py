import time
from tkinter import messagebox, BOTH, scrolledtext, filedialog
import tkinter as tk
import sqlite3
import customtkinter
import subprocess
import sys
import cv2
import PIL.Image, PIL.ImageTk
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime

from BD import annoncepb

font1 = ('Helvetica', 21, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

green1 = "#E2F1E7"
green2 = "#068962"
green3 = "#029809"
green4 = "#012705"

fenetre = tk.Tk()
fenetre.title("IAE")
fenetre.iconbitmap("img/logo.png")
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()
customtkinter.set_appearance_mode("#E2F1E7")
customtkinter.set_default_color_theme("green")


def cal_frame():
    global frame1, frmk
    frame1 = customtkinter.CTkScrollableFrame(fenetre, bg_color="#fff", fg_color="#E2F1E7", corner_radius=15,
                                              border_color="#068962", border_width=6, scrollbar_fg_color=green2,
                                              scrollbar_button_color=green3,
                                              scrollbar_button_hover_color=green4,
                                              width=600, height=470)
    frame1.place(x=screen_width - 640, y=140)
    frmk = customtkinter.CTkLabel(frame1, width=100, height=26, bg_color=green1, text="recent event", text_color=green2)


def rech(query):
    global tree, scrol

    conn = sqlite3.connect("ma_base_de_donnees.db")
    cur = conn.cursor()
    cur.execute("SELECT classe,nom,prénoms,id FROM listes WHERE nom LIKE ?", ['%' + query.lower() + '%'])
    resultats1 = cur.fetchall()
    cur.execute("SELECT classe,nom,prénoms,id FROM listes WHERE prénoms LIKE ?", ['%' + query.lower() + '%'])
    resultats = cur.fetchall()
    print(resultats)
    style = ttk.Style()
    # styliser le tableau
    style.configure("Custom.Treeview", background='#E2F5E7', foreground='#068962', rowheight=25,
                    fieldbackground="#012705", bordercolor="#068962", borderwidth=6,
                    font=('Helvetica', 12, 'bold'))
    style.map("Custom.Treeview", background=[('selected', '#068962')], foreground=[('selected', '#E2F1E7')])
    # creer le tableau
    tree = ttk.Treeview(fenetre, show='headings', style='Custom.Treeview', height=250)
    # l'entête du tableau
    tree['columns'] = ['Classe', 'Nom', 'Prenom', 'Matricule']
    tree.place(x=150, y=200, width=550, height=150)
    # tree.tag_configure('heading',background="red",foreground="red")
    tree.column("Classe", width=100)
    tree.column("Matricule", width=100)
    tree.column("Nom", width=150)
    tree.column("Prenom", width=150)
    # creer un scrolbar fonctionnel
    scrol = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
    scrol.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrol.set)
    diction = {}
    for column in tree['columns']:
        diction[column] = True
        tree.heading(column, text=column)
    for enreg in resultats:
        tree.insert("", 'end', enreg[3], values=(enreg[0], enreg[1], enreg[2], enreg[3]))
    for enreg in resultats1:
        tree.insert("", 'end', enreg[3], values=(enreg[0], enreg[1], enreg[2], enreg[3]))

    def selected_item(event):
        for s in tree.selection():
            item = tree.item(s)
            # affecter
            selected = item['values']
            print(f"vous avez selectionner {selected}")
            print(f"selected[0]={selected[0]} et {selected[1]}")
            cur.execute(
                f"SELECT id,nom,prénoms,genre,classe,âge,date,tel,photo,annee FROM {selected[0]} WHERE nom = ?",
                (selected[1],))
            c = cur.fetchall()
            for d in c:
                frm = customtkinter.CTkScrollableFrame(fenetre, bg_color="#fff", fg_color="#E2F1E7",
                                                       corner_radius=15,
                                                       border_color="#068962", border_width=6,
                                                       scrollbar_fg_color=green2, scrollbar_button_color=green1,
                                                       scrollbar_button_hover_color=green4,
                                                       width=600, height=470)
                frm.place(x=screen_width - 640, y=140)
                image = Image.open(BytesIO(d[8])).resize((151, 142), Image.LANCZOS)
                img = ImageTk.PhotoImage(image)

                ig = customtkinter.CTkLabel(master=frm, text="", image=img, bg_color=green1,
                                            corner_radius=10,
                                            width=150, height=150)
                ig.pack()
                clm = customtkinter.CTkLabel(master=frm, text=f"""{selected[0]}\n {d[0]}""",
                                             corner_radius=10, font=("Arial", 45), text_color=green3,
                                             width=90, height=35)
                clm.place(x=0, y=25)
                cl = customtkinter.CTkLabel(master=frm, text=f"Matricule:{selected[3]}",
                                            corner_radius=10, font=("Arial", 25), text_color=green2,
                                            width=150, height=35)
                cl.place(x=395, y=25)
                clq = customtkinter.CTkLabel(master=frm,
                                             text=f"""{d[1]}\n{d[2]}""",
                                             corner_radius=10, font=("Arial", 19), text_color="#28AB84",
                                             width=150, height=35)
                clq.place(x=395, y=65)
                cln = customtkinter.CTkLabel(master=frm,
                                             text=f"""Gender:{d[5]} \n Age:{d[3]} \n Date of birth:{d[4]}\nlast_presence:{d[7]} \n Tel:{d[6]} \n """,
                                             corner_radius=10, font=font2, text_color=green2,
                                             width=150, height=35)
                cln.pack(side=tk.BOTTOM)
                hide_cursor()

    # lier l'evenement de selection
    tree.bind("<<TreeviewSelect>>", selected_item)


def on_press(event):
    reche = recherche.get()
    if reche:
        rech(reche)


def pubannonce():
    fenetra = tk.Tk()
    fenetra.title("Annonces")
    fenetra.configure(background="#001220")
    fenetra.minsize(500, 500)
    fenetra.maxsize(500, 500)
    texte_saisi = scrolledtext.ScrolledText(fenetra, wrap=tk.WORD, width=50, height=10)
    texte_saisi.pack(pady=10)

    def enregistrer():
        texte = texte_saisi.get("1.0", tk.END)
        annoncepb(texte)
        messagebox.showwarning("alert", "Bien enregistrer")
        fenetra.destroy()

    bouton_enregeistrer = customtkinter.CTkButton(fenetra, text='REGISTER', text_color="#fff", font=font2,
                                                  fg_color='#0CC9A9',
                                                  hover_color='#33050B',
                                                  bg_color='#121111', cursor='hand2', corner_radius=5, width=120,
                                                  command=enregistrer
                                                  )
    bouton_enregeistrer.place(x=100, y=200)

    fenetra.mainloop()


def Annonce():
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
    else:
        tree.forget()
    conn.close()
    fenetra.mainloop()


# Fonction pour lire la vidéo
def play_video():
    ret, frame = cap.read()
    if ret:
        # Redimensionnement du frame en fonction du facteur d'échelle
        frame = cv2.resize(frame, (new_width, new_height))
        # Conversion du frame en format compatible avec tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = PIL.Image.fromarray(frame)
        frame = PIL.ImageTk.PhotoImage(image=frame)
        label.config(image=frame)
        label.image = frame
        # Appel récursif pour lire la prochaine frame
        label.after(10, play_video)
    else:
        # Rejouer la vidéo depuis le début si elle est terminée
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        play_video()


def show_tooltip(event, text):
    x, y, _, _ = event.widget.bbox("insert")
    x += event.widget.winfo_rootx() + 25
    y += event.widget.winfo_rooty() + 50
    global tooltip_window
    tooltip_window = tk.Toplevel(event.widget)
    tooltip_window.wm_overrideredirect(True)
    tooltip_window.wm_geometry(f"+{x}+{y}")
    label = tk.Label(tooltip_window, text=text, justify=tk.LEFT,

                     background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                     font=("tahoma", "8", "normal"))

    label.pack(ipadx=1)


def hide_tooltip(event):
    global tooltip_window
    if tooltip_window:
        tooltip_window.destroy()


def return_to_reception():
    fenetre.quit()
    fenetre.destroy()
    recept_path = "main.py"
    subprocess.run([sys.executable, recept_path])
    fenetre.destroy()


def update_time():
    now = datetime.now()
    date = now.strftime("%d/ %m /%Y")
    heur = now.strftime('%H : %M :  %S')
    date_lb = ttk.Label(fenetre, text=f"{date}")
    date_lb.configure(font=('Arial', 15), foreground="#068962", background="#fff", width=10)
    date_lb.place(x=screen_width - 125, y=screen_height / 9)
    heur_lb = ttk.Label(fenetre, text=f"{heur}")
    heur_lb.configure(font=('Arial', 15), foreground="#068962", background="#fff", width=10)
    heur_lb.place(x=screen_width - 125, y=screen_height / 7)
    fenetre.after(1000, update_time)


update_time()


def run_red():
    pathrtya = 'inscription.py'
    subprocess.run([sys.executable, pathrtya])


def hide_cursor():
    calendar_cursor.configure(bg_color="#fff", image="", width=0)
    event_cursor.configure(bg_color="#fff", image="", width=0)
    notification_cursor.configure(bg_color="#fff", image="", width=0)
    all_stud_cursor.configure(bg_color="#fff", image="", width=0)
    profesor_cursor.configure(bg_color="#fff", image="", width=0)
    calendar_btn.configure(fg_color="#fff")
    event_btn.configure(fg_color="#fff")
    noti_btn.configure(fg_color="#fff")
    all_stu_btn.configure(fg_color="#fff")
    profesor_btn.configure(fg_color="#fff")


def cursor(lb, btn, page):
    hide_cursor()
    btn.configure(fg_color="#029809")
    lb.configure(bg_color="#fff", width=32, height=35, image=icon11)
    page()


def create_Button():
    img4 = Image.open("img/admin.png").resize((30, 30), Image.LANCZOS)
    icon4 = ImageTk.PhotoImage(img4)
    img2 = Image.open("img/logo2.png").resize((30, 30), Image.LANCZOS)
    icon2 = ImageTk.PhotoImage(img2)
    img3 = Image.open("img/clock.png").resize((30, 30), Image.LANCZOS)
    icon3 = ImageTk.PhotoImage(img3)
    img9 = Image.open("img/logo.png").resize((25, 25), Image.LANCZOS)
    icon9 = ImageTk.PhotoImage(img9)
    img10 = Image.open("img/student.png").resize((25, 25), Image.LANCZOS)
    icon10 = ImageTk.PhotoImage(img10)

    qt_btn = customtkinter.CTkButton(fenetre, text="RETURN", fg_color="#068962", font=("arial", 18), bg_color='#fff',
                                     height=40,
                                     hover_color="#012705", corner_radius=13, command=return_to_reception)
    qt_btn.place(x=screen_width - 200, y=screen_height - 75)
    register_btn = customtkinter.CTkButton(fenetre, text="REGISTERING", fg_color="#068962", font=("arial", 18),
                                           bg_color='#fff',
                                           hover_color="#012705", corner_radius=10, command=run_red, width=250,
                                           height=40, image=icon2)
    register_btn.place(x=(screen_width / 2) - 250, y=screen_height - 480)
    edt_btn = customtkinter.CTkButton(fenetre, text="TIMETABLE", fg_color="#068962", font=("arial", 18),
                                      bg_color='#fff',
                                      hover_color="#012705", corner_radius=10, command=empl, width=250,
                                      height=40, image=icon3)
    edt_btn.place(x=(screen_width / 2) - 250, y=screen_height - 390)
    annonce_btn = customtkinter.CTkButton(fenetre, text="ANNONCE", fg_color="#068962", font=("arial", 18),
                                          bg_color='#fff',
                                          hover_color="#012705", corner_radius=10, width=250, height=40, image=icon4,
                                          command=pubannonce)
    annonce_btn.place(x=(screen_width / 2) - 250, y=screen_height - 300)
    fee_btn = customtkinter.CTkButton(fenetre, text="FEE", fg_color="#029809", font=("arial", 12),
                                      bg_color='#fff',
                                      hover_color="#012705", corner_radius=0, width=90, height=30, image=icon9,
                                      command=Annonce)
    fee_btn.place(x=screen_width - 640, y=screen_height - 110)
    mark_btn = customtkinter.CTkButton(fenetre, text="MARK", fg_color="#029809", font=("arial", 12),
                                       bg_color='#fff',
                                       hover_color="#012705", corner_radius=0, width=90, height=30, image=icon10)
    mark_btn.place(x=screen_width - 548, y=screen_height - 110)


def calendar_page():
    mot = customtkinter.CTkLabel(frame1, text="PAGE 1 \n coucou baby?", text_color="#068962", font=("Bold", 30),
                                 width=585, height=465)
    mot.pack(padx=20, pady=20)


def event_page():
    conn = sqlite3.connect('ma_base_de_donnees.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM annonces ORDER BY id DESC LIMIT 1')
    raws = curs.fetchone()
    if raws:
        titre, contenu = raws[1], raws[2]

        mot = customtkinter.CTkLabel(frame1, text=f"PAGE 2 \n {contenu}  ?", text_color="#068962", font=("Bold", 30),
                                     width=585, height=465)
        mot.pack(padx=20, pady=20)


def noti_page():
    # select dernier annnonce recent
    global dernier
    conn = sqlite3.connect('ma_base_de_donnees.db')
    curs = conn.cursor()
    curs.execute("""SELECT * FROM annonces""")
    raws = curs.fetchall()
    print(raws)
    for raw in raws:
        dernier = raw[2]
    noti_lb = customtkinter.CTkLabel(frame1, text=f"annonce recent \n {dernier}"
                                     , text_color="#068962", font=("Arial", 30), width=400, height=100)
    noti_lb.pack(padx=20, pady=20)


def all_stu_page():
    mot = customtkinter.CTkLabel(frame1, text="ALL_STUDENT \n HI everybody!", text_color="#068962", font=("Bold", 30),
                                 width=585, height=465)
    mot.pack(padx=20, pady=20)


def profesor_page():
    mot = customtkinter.CTkLabel(frame1, text="PROFESOR \n THAT'S COOL", text_color="#068962", font=("Bold", 30),
                                 width=585, height=465)
    mot.pack(padx=20, pady=20)


def show_lab(event):
    frmk.pack(side=tk.LEFT)


def hide_lab(event):
    frmk.pack_forget()


def empl():
    subprocess.run([sys.executable, 'changempl.py'])


# Chargement de la vidéo
video_path = "bg/IAE_2.mp4"
cap = cv2.VideoCapture(video_path)

# Récupération des dimensions de la vidéo
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calcul du facteur d'échelle pour redimensionner la vidéo à la taille de l'écran
scale_factor = max(screen_width / width, screen_height / height)

# Nouvelles dimensions de la vidéo
new_width = screen_width
new_height = screen_height

# Redimensionnement de la fenêtre principale et de la zone d'affichage de la vidéo
# root.geometry(f"{new_width}x{new_height}+{int((screen_width - new_width) / 2)}+{int((screen_height - new_height) / 2)}")
fenetre.geometry(
    f"{new_width}x{new_height}+{int((screen_width - new_width) - 4)}+{int((screen_height - new_height) / 2)}")

# Création de la zone d'affichage de la vidéo
video_frame = tk.Frame(fenetre, width=new_width, height=new_height)
video_frame.place(x=0, y=0)
# Création de l'étiquette pour afficher la vidéo
label = tk.Label(video_frame)
label.place(x=-2, y=-2)

img1 = Image.open("img/search.png").resize((25, 25), Image.LANCZOS)
icon1 = ImageTk.PhotoImage(img1)
rech1 = tk.StringVar()
recherche = customtkinter.CTkEntry(fenetre, bg_color="#fff", fg_color="#E2F1E7", border_width=2,
                                   border_color='#055D2B', width=250, height=40,
                                   placeholder_text="Search.....", placeholder_text_color="#055D2B", font=font2,
                                   corner_radius=15, text_color="#677470", textvariable=rech1)
recherche.place(x=(screen_width / 2) - 250, y=150)
recherche.bind('<Key>', on_press)
df = recherche.get()

cmd1 = lambda: rech(df)
cmd2 = lambda: recherche.delete(0, tk.END)
srbt = customtkinter.CTkButton(fenetre, image=icon1, width=25, height=25, bg_color="#E2F1E7", text='',
                               fg_color='#E2F1E7', hover_color='#81e39f', corner_radius=0,
                               command=lambda: (cmd1(), cmd2()))

srbt.place(x=(screen_width / 2) - 50, y=154)
create_Button()
play_video()

img1 = Image.open("img/calendar.png").resize((30, 30), Image.LANCZOS)
icon1 = ImageTk.PhotoImage(img1)
img5 = Image.open("img/event.png").resize((30, 30), Image.LANCZOS)
icon5 = ImageTk.PhotoImage(img5)
img6 = Image.open("img/notification.png").resize((30, 30), Image.LANCZOS)
icon6 = ImageTk.PhotoImage(img6)
img7 = Image.open("img/all student.png").resize((30, 30), Image.LANCZOS)
icon7 = ImageTk.PhotoImage(img7)
img8 = Image.open("img/professor.png").resize((30, 30), Image.LANCZOS)
icon8 = ImageTk.PhotoImage(img8)
img11 = Image.open("img/logo2.png").resize((25, 25), Image.LANCZOS)
icon11 = ImageTk.PhotoImage(img11)
calendar_btn = customtkinter.CTkButton(fenetre, image=icon1, bg_color="#fff", text='', width=33, fg_color="#fff",
                                       hover_color="#068962"
                                       , command=lambda: cursor(calendar_cursor, calendar_btn, calendar_page))

calendar_btn.bind("<Enter>", lambda event: show_tooltip(event, "Calendrier"))
calendar_btn.bind("<Leave>", hide_tooltip)
calendar_btn.place(x=screen_width / 2, y=90)

event_btn = customtkinter.CTkButton(fenetre, image=icon5, bg_color="#fff", text='', width=33, fg_color="#fff",
                                    hover_color="#068962", corner_radius=5
                                    , command=lambda: cursor(event_cursor, event_btn, event_page))
event_btn.place(x=(screen_width / 2) + 80, y=90)
event_btn.bind("<Enter>", lambda event: show_tooltip(event, "Dernier notification"))
event_btn.bind("<Leave>", hide_tooltip)
noti_btn = customtkinter.CTkButton(fenetre, image=icon6, bg_color="#fff", text='', width=33, fg_color="#fff",
                                   hover_color="#068962", corner_radius=5
                                   , command=lambda: cursor(notification_cursor, noti_btn, noti_page))
noti_btn.place(x=(screen_width / 2) + 160, y=90)
noti_btn.bind("<Enter>", lambda event: show_tooltip(event, "Dernier notification"))
noti_btn.bind("<Leave>", hide_tooltip)
all_stu_btn = customtkinter.CTkButton(fenetre, image=icon7, bg_color="#fff", text='', width=33, fg_color="#fff",
                                      hover_color="#068962"
                                      , command=lambda: cursor(all_stud_cursor, all_stu_btn, all_stu_page))
all_stu_btn.place(x=(screen_width / 2) + 240, y=90)
profesor_btn = customtkinter.CTkButton(fenetre, image=icon8, bg_color="#fff", text='', width=33, fg_color="#fff",
                                       hover_color="#068962"
                                       , command=lambda: cursor(profesor_cursor, profesor_btn, profesor_page))
profesor_btn.place(x=(screen_width / 2) + 320, y=90)

calendar_cursor = customtkinter.CTkLabel(fenetre, text='', bg_color="#fff", width=25, height=35)
calendar_cursor.place(x=(screen_width / 2) - 33, y=90)
event_cursor = customtkinter.CTkLabel(fenetre, text='', bg_color="#fff", width=30, height=35)
event_cursor.place(x=(screen_width / 2) + 47, y=90)
notification_cursor = customtkinter.CTkLabel(fenetre, text='', bg_color="#fff", width=30, height=32)
notification_cursor.place(x=(screen_width / 2) + 127, y=90)
all_stud_cursor = customtkinter.CTkLabel(fenetre, text='', bg_color="#fff", width=30, height=32)
all_stud_cursor.place(x=(screen_width / 2) + 207, y=90)
profesor_cursor = customtkinter.CTkLabel(fenetre, text='', bg_color="#fff", width=30, height=32)
profesor_cursor.place(x=(screen_width / 2) + 287, y=90)
cal_frame()

fenetre.attributes('-fullscreen', True)
fenetre.mainloop()
