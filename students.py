import subprocess
import sys
import tkinter as tk
import PIL.Image
import PIL.ImageTk
import customtkinter
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.title("IAE")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Chargement de la vidéo
video_path = "bg/SATURNE.mp4"
cap = cv2.VideoCapture(video_path)

# Récupération des dimensions de la vidéo
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calcul du facteur d'échelle pour redimensionner la vidéo à la taille de l'écran
scale_factor = max(screen_width / width, screen_height / height)

new_width = screen_width
new_height = screen_height

root.geometry(f"{new_width}x{new_height}+{int((screen_width - new_width) - 4)}+{int((screen_height - new_height) / 2)}")

# Création de la zone d'affichage de la vidéo
video_frame = tk.Frame(root, width=new_width, height=new_height)
video_frame.place(x=0, y=0)


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


# Création de l'étiquette pour afficher la vidéo
label = tk.Label(video_frame)
label.place(x=-2, y=-2)

# Lancement de la lecture de la vidéo
play_video()


def retourrec():
    form_path = 'main.py'
    subprocess.run([sys.executable, form_path])


def inscription():
    form_path = 'inscription.py'
    subprocess.run([sys.executable, form_path])


def presence():
    form_path = 'presence.py'
    subprocess.run([sys.executable, form_path])


img1 = Image.open("img/student1.png").resize((30, 30), Image.LANCZOS)
icon1 = ImageTk.PhotoImage(img1)
img2 = Image.open("img/prof.png").resize((30, 30), Image.LANCZOS)
icon2 = ImageTk.PhotoImage(img2)
img3 = Image.open("img/admin.png").resize((30, 30), Image.LANCZOS)
icon3 = ImageTk.PhotoImage(img3)

st_btn = customtkinter.CTkButton(root, text="PRESENCE", font=("arial", 20), text_color="#33050B",
                                 width=250, height=40,
                                 hover_color="#D80E29",
                                 fg_color="#0CC9A9", corner_radius=15, bg_color="#001218", command=presence)
st_btn.place(x=screen_width * 0.4055, y=screen_height - 400)

prf_btn = customtkinter.CTkButton(root, text="INSCRIPTION", font=("arial", 20), text_color="#33050B",
                                  width=250, height=40, hover_color="#D80E29",
                                  fg_color="#0CC9A9", corner_radius=15, bg_color="#001218", command=inscription)
prf_btn.place(x=screen_width * 0.4055, y=screen_height - 500)

qt_btn = customtkinter.CTkButton(root, text="EXIT", hover_color="#E20D38", font=("arial", 18), command=root.destroy,
                                 bg_color='#001119',
                                 corner_radius=15, fg_color="#0CC9A9", width=40, height=40,text_color="#33050B")
qt_btn.place(x=screen_width - 140, y=screen_height - 80)

Inf_btn = customtkinter.CTkButton(root, text="RETOUR", hover_color="#E20D38", font=("arial", 18), command=retourrec,
                                  bg_color='#001119',
                                  corner_radius=15, fg_color="#0CC9A9", width=40, height=40,text_color="#33050B")
Inf_btn.place(x=screen_width - 160, y=screen_height - 140)

root.attributes('-fullscreen', True)
root.mainloop()
