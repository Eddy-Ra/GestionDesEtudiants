import subprocess
import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk

import PIL.Image
import PIL.ImageTk
import customtkinter
import cv2
from PIL import Image, ImageTk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("IAE")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Chargement de la vidéo
    video_path = "bg/SAT4.mp4"
    cap = cv2.VideoCapture(video_path)

    # Récupération des dimensions de la vidéo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


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



    def open_Student():
        win_path = "etudiant.py"
        subprocess.run([sys.executable, win_path])



    def open_form():
        root.destroy()
        form_path = 'form.py'
        subprocess.run([sys.executable, form_path])

    def open_prof():
        root.destroy()
        form_path = 'form2.py'
        subprocess.run([sys.executable, form_path])


    img1 = Image.open("img/student1.png").resize((30, 30), Image.LANCZOS)
    icon1 = ImageTk.PhotoImage(img1)
    img2 = Image.open("img/prof.png").resize((30, 30), Image.LANCZOS)
    icon2 = ImageTk.PhotoImage(img2)
    img3 = Image.open("img/admin.png").resize((30, 30), Image.LANCZOS)
    icon3 = ImageTk.PhotoImage(img3)

    st_btn = customtkinter.CTkButton(root, text="STUDENT", font=("arial", 20), text_color="#33050B",
                                     width=250, height=40,
                                     hover_color="#D80E29", image=icon1,
                                     fg_color="#0CC9A9", corner_radius=15, bg_color="#001218", command=open_Student)
    st_btn.place(x=screen_width * 0.4055, y=screen_height - 350)

    prf_btn = customtkinter.CTkButton(root, text="PROFESSOR", font=("arial", 20), text_color="#33050B",
                                      width=250, height=40, hover_color="#D80E29", image=icon2,
                                      fg_color="#0CC9A9", corner_radius=15, bg_color="#001218", command=open_prof)
    prf_btn.place(x=screen_width * 0.4055, y=screen_height - 450)
    ad_btn = customtkinter.CTkButton(root, text="ADMINISTRATION", font=("arial", 20), text_color="#33050B",
                                     width=250, height=40, hover_color="#D80E29", image=icon3,
                                     fg_color="#0CC9A9", corner_radius=15, bg_color="#001218", command=open_form)
    ad_btn.place(x=screen_width * 0.4055, y=screen_height - 550)

    qt_btn = customtkinter.CTkButton(root, text="EXIT", hover_color="#E20D38", font=("arial", 18), command=root.destroy,
                                     bg_color='#001119',
                                     corner_radius=15, fg_color="#0CC9A9", width=40, height=40, text_color="#33050B")
    qt_btn.place(x=screen_width - 140, y=screen_height - 80)

    Inf_btn = customtkinter.CTkButton(root, text="INFO", hover_color="#E20D38", font=("arial", 18), command=root.destroy,
                                      bg_color='#001119',
                                      corner_radius=15, fg_color="#0CC9A9", width=40, height=40, text_color="#33050B")
    Inf_btn.place(x=screen_width - 140, y=screen_height - 140)


    def update_time():
        now = datetime.now()
        date = now.strftime("%d/ %m /%Y")
        heur = now.strftime('%H : %M :  %S')
        date_lb = ttk.Label(root, text=f"{date}")
        date_lb.configure(font=('Arial', 15), foreground="#068962", background="#111", width=10)
        date_lb.place(x=screen_width - 125, y=4)
        heur_lb = ttk.Label(root, text=f"{heur}")
        heur_lb.configure(font=('Arial', 15), foreground="#068960002", background="#111", width=10)
        heur_lb.place(x=screen_width - 125, y=screen_height / 20)
        root.after(1000, update_time)


    update_time()
    root.attributes('-fullscreen', True)

    root.mainloop()
