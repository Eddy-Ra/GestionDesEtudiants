
import customtkinter


app = customtkinter.CTk()
app.title('Inscription')
app.geometry("500x300+400+150")
app.minsize(600, 480)
app.maxsize(600, 480)
app.config(bg='#001220')

font1 = ('Helvetica', 17, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')





def user_conf():
    frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=600, height=500)
    frame1.place(x=0, y=0)
    sign_up_label = customtkinter.CTkLabel(frame1, text='INSCRIPTION', text_color='#0CC9A9', font=font1)
    sign_up_label.place(x=280, y=25)

    nom = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Nom', placeholder_text_color="#a3a3a3",
                                         text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                         border_width=2, width=300, height=35, corner_radius=35, )
    nom.place(x=250, y=60)

    prenoms = customtkinter.CTkEntry(frame1, font=font2, show='*', placeholder_text='Prénoms',
                                         placeholder_text_color="#a3a3a3",
                                         text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                         border_width=2, width=300, height=35, corner_radius=35)
    prenoms.place(x=250, y=120)

    classe = customtkinter.CTkEntry(frame1, font=font2, show='*', placeholder_text='classe',
                                         placeholder_text_color="#a3a3a3",
                                         text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                         border_width=2, width=300, height=35, corner_radius=35)
    classe.place(x=250, y=180)

    daten = customtkinter.CTkEntry(frame1, font=font2, show='*', placeholder_text='Date et Lieu de naissance',
                                         placeholder_text_color="#a3a3a3",
                                         text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                         border_width=2, width=300, height=35, corner_radius=35)
    daten.place(x=250, y=240)

    age = customtkinter.CTkEntry(frame1, font=font2, show='*', placeholder_text='age',
                                         placeholder_text_color="#a3a3a3",
                                         text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                         border_width=2, width=300, height=35, corner_radius=35)
    age.place(x=250, y=300)


    tel = customtkinter.CTkEntry(frame1, font=font2, show='*', placeholder_text='téléphone',
                                         placeholder_text_color="#a3a3a3",
                                         text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                         border_width=2, width=300, height=35, corner_radius=35)
    tel.place(x=250, y=360)






    sign_up_bt = customtkinter.CTkButton(frame1, text='S'"'INSCRIRE", text_color="#fff", font=font2, fg_color='#0CC9A9',
                                         hover_color='#33050B',
                                         bg_color='#121111', cursor='hand2', corner_radius=5, width=120, command=user_conf)
    sign_up_bt.place(x=280, y=420)

    nom = nom.get()
    prenoms = prenoms.get()
    classe=classe.get()
    daten=daten.get()
    age=age.get()
    tel=tel.get()




    app.mainloop()
