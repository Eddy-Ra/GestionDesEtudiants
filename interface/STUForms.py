import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

import cv2

from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


font1 = ('Helvetica',17,'bold')
font2 = ('Arial',17,'bold')
font3 = ('Arial',13,'bold')
font4 = ('Arial',13,'bold','underline')
font6 = ('Arial',20,'bold',)

logi = customtkinter.CTk()
logi.title('IAE(Register)')
logi.geometry("715x400+400+150")
logi.maxsize(715,400)
#creer un var canva pour placer l'img dans un canva
canva = customtkinter.CTkCanvas(logi,bg='gray16',width=715,height=400)
#le repertoire de l'img
filename = Image.open('too/iae.png')
filename.resize((715,400),Image.LANCZOS)
pic = ImageTk.PhotoImage(filename)
bg_lb = customtkinter.CTkLabel(logi, image=pic, text='')
bg_lb.place(x=0,y=0)
canva.pack()
def procedure():
    global nom_lb,prenom_lb,date_lb,gender_select,tel_lb,su_lb
    filiere = su_lb.get()
    name = nom_lb.get()
    surename = prenom_lb.get()
    birth = date_lb.get()
    phone = tel_lb.get()
    genre = gender_select.get()
    age = 2024-int(birth)

    vid = cv2.VideoCapture(0)
    if name !='' and surename !='' and filiere !='' and birth != '':
        while (True):
             capt, im = vid.read()
             cv2.imshow('Image Show', im)
             if cv2.waitKey(1) & 0xFF == ord("c"):
                break
             cv2.imwrite(f"C:\\Users\\Ranto Tolojanahary\\PycharmProjects\\IAE\\.venv\\img\\{name}.png",im)
        vid.release()
        messagebox.showinfo('Registering successfuly', 'Your are registered to our Database')
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://iae-2024-default-rtdb.firebaseio.com/'
        })
        ref = db.reference(f'{filiere}')
        data = {
            f"{name}":{
                         "Name":f"{name}",
                         "Surename":f"{surename}",
                         "Subject":f"{filiere}",
                         "Phone or Email":phone,
                         "Gender":f"{genre}",
                         "Age":age
                     }
            }
        for key,value in data.items():
            ref.child(key).set(value)
        cv2.destroyAllWindows()
        logi.destroy()
    else:
        messagebox.showerror('Error','You had to fill all Blank to proced.')


def named_pic():
    name = nom_lb.get()
    return name


tit_lb = customtkinter.CTkLabel(logi,text='REGISTERING',font=font6,text_color="#012705",bg_color="#81e39f")
tit_lb.place(x=295,y=78)


su_lb = customtkinter.CTkEntry(logi,font=font3,placeholder_text='Enter your subject....',placeholder_text_color='#055D2B',bg_color='#4ff39f',
                                fg_color='#81e39f',corner_radius=1,border_color='#055D2B',border_width=1,width=150,height=30,text_color='#D80E29')
su_lb.place(x=288,y=115)
nom_lb = customtkinter.CTkEntry(logi,font=font3,placeholder_text='name :......',placeholder_text_color='#055D2B',bg_color='#4ff39f',
                                fg_color='#81e39f',text_color='#012705',corner_radius=1,border_color='#055D2B',border_width=1,width=250,height=30)
nom_lb.place(x=250,y=155)
prenom_lb = customtkinter.CTkEntry(logi,font=font3,placeholder_text='surename:.......',placeholder_text_color='#055D2B',bg_color='#4ff39f',
                                fg_color='#81e39f',corner_radius=1,border_color='#055D2B',text_color='#012705',border_width=1,width=250,height=30)
prenom_lb.place(x=250,y=195)

date_lb =customtkinter.CTkEntry(logi,font=font3,placeholder_text='date of birth:.......',placeholder_text_color='#055D2B',bg_color='#4ff39f',
                                fg_color='#81e39f',corner_radius=1,border_color='#055D2B',text_color='#012705',border_width=1,width=250,height=30)
date_lb.place(x=250,y=235)

option =['Male','Female']
variable1 = StringVar()
gender_select = customtkinter.CTkOptionMenu(logi,dropdown_font=font2,dropdown_text_color='#fff',bg_color='#4ff39f',fg_color='#81e39f',font=font3,
                                          variable=variable1,values=option,state='readonly',text_color='#055D2B',button_hover_color='#D80E29',
                                         dropdown_hover_color='#055D2B',dropdown_fg_color='#4ff39f',width=125,height=30)
gender_select.set('Male')
gender_select.place(x=250,y=275)
tel_lb = customtkinter.CTkEntry(logi,font=font3,placeholder_text='Phone or email:......',placeholder_text_color='#055D2B',bg_color='#4ff39f',
                                fg_color='#81e39f',text_color='#012705',corner_radius=1,border_color='#055D2B',border_width=1,width=125,height=30)
tel_lb.place(x=375,y=275)
pro_btn =customtkinter.CTkButton(logi, text="PROCED",fg_color="#055D2B", font=font2,bg_color='#98e39f',
                                    hover_color="#012705" ,corner_radius=7,width=100,height=30,command=procedure)
pro_btn.place(x=250,y=315)
canc_btn =customtkinter.CTkButton(logi, text="CANCEL",fg_color="#055D2B", font=font2,bg_color='#98e39f',
                                    hover_color="#012705" ,corner_radius=7,width=100,height=30,command=logi.destroy)
canc_btn.place(x=395,y=315)

logi.mainloop()
