import tkinter as tk
import customtkinter
import subprocess
import sys
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("IAE")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


def show_frame(event):
    framekely.place(x=screen_width - 310, y=screen_height - 140)


def hide_frame(event):
    framekely.place_forget()


def open_Student():
    win_path = "presence.py"
    subprocess.run([sys.executable, win_path])
    root.destroy()


def open_form():
    form_path = 'form.py'
    subprocess.run([sys.executable, form_path])


def play_next_video():
    global current_video_index, cap

    # Passage à la vidéo suivante dans la liste
    current_video_index = (current_video_index + 1) % len(video_paths)

    # Initialisation de la capture pour la prochaine vidéo
    cap.open(video_paths[current_video_index])

    # Lancement de la lecture de la nouvelle vidéo
    play_video()


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
        # cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # play_video()
        # Si la vidéo est terminée, passer à la vidéo suivante
        play_next_video()


white = '#fff'
BgColor1 = '#010332'
BgColor2 = '#050320'
BgColor3 = '#060117'
skyblue = '#0CC9A9'
rose = '#D80E29'
color = '#33050B'
yellow = '#ebff00'
roseb = '#33050B'

# video_path = ['bg/SAT1.mp4', 'bg/SAT2.mp4', 'bg/SAT3.mp4', 'bg/SAT4.mp4']
# cap = cv2.VideoCapture(video_path[3])

video_paths = ['bg/SAT1.mp4', 'bg/SAT4.mp4']
current_video_index = 0
cap = cv2.VideoCapture(video_paths[current_video_index])

# Récupération des dimensions de la vidéo
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calcul du facteur d'échelle pour redimensionner la vidéo à la taille de l'écran
scale_factor = max(screen_width / width, screen_height / height)

new_width = screen_width
new_height = screen_height

root.geometry(
    f"{new_width}x{new_height}+{int((screen_width - new_width) - 4)}+{int((screen_height - new_height) / 2)}")

# Création de la zone d'affichage de la vidéo
video_frame = tk.Frame(root, width=new_width, height=new_height)
video_frame.place(x=0, y=0)

# Création de l'étiquette pour afficher la vidéo
label = tk.Label(video_frame)
label.place(x=-2, y=-2)

# Lancement de la lecture de la vidéo
play_video()

img1 = Image.open("img/student1.png").resize((30, 30), Image.LANCZOS)
icon1 = ImageTk.PhotoImage(img1)
img2 = Image.open("img/prof.png").resize((30, 30), Image.LANCZOS)
icon2 = ImageTk.PhotoImage(img2)
img3 = Image.open("img/admin.png").resize((30, 30), Image.LANCZOS)
icon3 = ImageTk.PhotoImage(img3)

st_btn = customtkinter.CTkButton(root, text="STUDENT", font=("arial", 20), text_color=roseb,
                                 width=250, height=40,
                                 hover_color=rose, image=icon1,
                                 fg_color=skyblue, corner_radius=15, bg_color=BgColor2, command=open_Student)
st_btn.place(x=(screen_width * (40)) / 100, y=screen_height - 350)

prf_btn = customtkinter.CTkButton(root, text="PROFESORS", font=("arial", 20), text_color=roseb,
                                  width=250, height=40, hover_color=rose, image=icon2,
                                  fg_color=skyblue, corner_radius=15, bg_color=BgColor2, command=open_Student)
prf_btn.place(x=(screen_width * (40)) / 100, y=screen_height - 450)
ad_btn = customtkinter.CTkButton(root, text="ADMINISTRATION", font=("arial", 20), text_color=roseb,
                                 width=250, height=40, hover_color=rose, image=icon3,
                                 fg_color=skyblue, corner_radius=15, bg_color=BgColor2, command=open_form)
ad_btn.place(x=(screen_width * (40)) / 100, y=screen_height - 550)

framekely = customtkinter.CTkFrame(root, width=160, height=95, bg_color=BgColor3, fg_color=rose, corner_radius=15)

T_btn = customtkinter.CTkButton(root, text="T", text_color=white, fg_color=rose, font=("arial", 18), bg_color=BgColor3,
                                corner_radius=100, hover_color=skyblue, width=10, height=10)
T_btn.place(x=screen_width - 110, y=screen_height - 150)
T_btn.bind("<Enter>", show_frame)
T_btn.bind("<Leave>", hide_frame)

qt_btn = customtkinter.CTkButton(root, text="EXIT", text_color=white, fg_color=rose, font=("arial", 18),
                                 command=root.quit, bg_color=BgColor3,
                                 corner_radius=50, hover_color=skyblue, width=40, height=35)
qt_btn.place(x=screen_width - 140, y=screen_height - 80)

Inf_btn = customtkinter.CTkButton(root, text="INFO", text_color=white, fg_color=rose, font=("arial", 18),
                                  command=root.quit, bg_color=BgColor3,
                                  corner_radius=50, hover_color=skyblue, width=40, height=35)
Inf_btn.place(x=screen_width - 140, y=screen_height - 120)

root.attributes('-fullscreen', True)
root.mainloop()
