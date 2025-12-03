import sqlite3
import bcrypt
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess
import sys

app = customtkinter.CTk()
app.title('Administration')
app.geometry("500x300+400+150")
app.wm_overrideredirect(True)
# app.minsize(500,300)
# app.maxsize(500,300)
app.config(bg='#001220')

font1 = ('Helvetica', 17, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')




def quitter():
    app.destroy()
    recept_path = "main.py"
    subprocess.run([sys.executable, recept_path])


def lb_destroy():
    app.destroy()
    errr.destroy()
    lb_btn.destroy()
    username_lb.delete(0, customtkinter.END)
    password_lb.delete(0, customtkinter.END)





def user_conf(event):
    no_db = sqlite3.connect("Admin.db")
    cur = no_db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Prof(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                     password TEXT NOT NULL )""")

    global errr, lb_btn,count
    username = username_lb.get()
    password = password_lb.get()

    count = 0
    if username != '' and password != '':
        cur.execute("SELECT *  FROM Prof")
        raw = cur.fetchall()
        for raws in raw:
            count = int(raws[0])
        if count < 7:
            messagebox.showinfo('IAE', """You had to add username and password 
                                                           that you only know  for 
                                                           the confidential information !!!! """)
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cur.execute("INSERT INTO Prof(username,password)"
                        " VALUES(?,?)", [username, hashed_password])
            no_db.commit()
            messagebox.showinfo('IAE', 'Username and Password is added succesfully ☻.')
        else:
            cur.execute("SELECT username,password FROM Prof")
            resultats = cur.fetchall()
            for resultat in resultats:
                if resultat[0] == username:
                    if bcrypt.checkpw(password.encode('utf-8'), resultat[1]):
                        path_adm = 'Professor.py'
                        app.destroy()
                        subprocess.run([sys.executable, path_adm])

                    else:
                        # messagebox.showerror("ErrorValidation", "Your password is invalide.")
                        errr = customtkinter.CTkLabel(frame1, text="Password Incorrect.", text_color="#D80E29",
                                                      font=font2)
                        errr.place(x=226, y=250)
                        cmd0 = lambda: app.destroy()
                        cmd1 = lambda: errr.destroy()
                        cmd2 = lambda: lb_btn.destroy()
                        cmd3 = lambda: password_lb.delete(0, customtkinter.END)

                        lb_btn = customtkinter.CTkButton(frame1, text='Try Again', font=font4, fg_color="#001220",
                                                         text_color='#00bf77', cursor='hand2', width=40,
                                                         command=lambda: (cmd1(), cmd2(), cmd3(), cmd0))
                        lb_btn.place(x=385, y=250)
                        break
                else:
                    # messagebox.showerror("ErrorValidation",f"{username} is not valide.")
                    errr = customtkinter.CTkLabel(frame1, text="Username UNKNOWN.", text_color="#D80E29", font=font2)
                    errr.place(x=205, y=250)
                    cmd1 = lambda: errr.destroy()
                    cmd2 = lambda: lb_btn.destroy()
                    cmd3 = lambda: lb_destroy()
                    lb_btn = customtkinter.CTkButton(frame1, text='Try Again', font=font4, fg_color="#001220",
                                                     text_color='#00bf77', cursor='hand2', width=40,
                                                     command=lambda: (cmd1(), cmd2(), cmd3()))
                    lb_btn.place(x=385, y=250)


    else:
        messagebox.showinfo("fill the blank", "You must fill all blank to Valid!")

    no_db.commit()
    no_db.close()

frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=500, height=500)
frame1.place(x=0, y=0)

img = Image.open('img/prof.png').resize((200, 300), Image.LANCZOS)
img1 = ImageTk.PhotoImage(img)
image1_label = customtkinter.CTkLabel(frame1, image=img1, bg_color='#001220', text='')
image1_label.place(x=50, y=0)

sign_up_label = customtkinter.CTkLabel(frame1, text='PROFESSOR', text_color='#0CC9A9', font=font1)
sign_up_label.place(x=280, y=25)

username_lb = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Username', placeholder_text_color="#a3a3a3",
                                     text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                     border_width=2, width=200, height=35, corner_radius=35, )
username_lb.place(x=250, y=65)

password_lb = customtkinter.CTkEntry(frame1, font=font2, show='*', placeholder_text='Password',
                                     placeholder_text_color="#a3a3a3",
                                     text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                     border_width=2, width=200, height=35, corner_radius=35)
password_lb.place(x=250, y=135)
password_lb.bind("<Return>", user_conf)

sign_up_bt = customtkinter.CTkButton(frame1, text='VALIDE', text_color="#fff", font=font2, fg_color='#0CC9A9',
                                     hover_color='#33050B',
                                     bg_color='#121111', cursor='hand2', corner_radius=5, width=100, command=user_conf)
sign_up_bt.place(x=240, y=200)
cancel_bt = customtkinter.CTkButton(frame1, text='CANCEL', text_color="#fff", font=font2, fg_color='#0CC9A9',
                                    hover_color='#33050B',
                                    bg_color='#121111', cursor='hand2', corner_radius=5, width=100, command=quitter)
cancel_bt.place(x=360, y=200)


app.mainloop()
