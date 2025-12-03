from tkinter import StringVar, OptionMenu, ttk, messagebox

from PIL import Image, ImageTk


def interface(sary):
    import customtkinter
    app = customtkinter.CTk()
    app.title('Inscription')
    app.geometry("500x300+400+150")
    app.minsize(600, 500)
    app.maxsize(600, 500)
    app.config(bg='#001220')

    font1 = ('Helvetica', 17, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')
    nomv = StringVar()
    prenomsv = StringVar()
    classev = StringVar()
    datev = StringVar()
    agev = StringVar()
    telv = StringVar()
    genrev = StringVar()
    kilasy = ["  ", "IMTICIA", "ISAIA"]
    frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=600, height=500)
    frame1.place(x=0, y=0)

    frame1.place(x=0, y=0)
    sign_up_label = customtkinter.CTkLabel(frame1, text='INSCRIPTION', fg_color='#0CC9A9',
                                           bg_color='#121111', corner_radius=5, width=120,
                                           )
    sign_up_label.place(x=330, y=5)
    img = Image.open(f'D:/bd/inconnu/{sary}.jpg').resize((200, 200), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(img)
    image1_label = customtkinter.CTkLabel(frame1, image=img1, bg_color='#001220', text='')
    image1_label.place(x=50, y=10)

    tnom = customtkinter.CTkLabel(frame1, text='Name:', text_color='#0CC9A9', font=font1)
    tnom.place(x=255, y=35)
    tprenoms = customtkinter.CTkLabel(frame1, text='Surname:', text_color='#0CC9A9', font=font1)
    tprenoms.place(x=255, y=95)
    tclass = customtkinter.CTkLabel(frame1, text='Classe:', text_color='#0CC9A9', font=font1)
    tclass.place(x=255, y=155)
    tdate = customtkinter.CTkLabel(frame1, text='Date de naissance:', text_color='#0CC9A9', font=font1)
    tdate.place(x=255, y=215)
    tage = customtkinter.CTkLabel(frame1, text='Age:', text_color='#0CC9A9', font=font1)
    tage.place(x=255, y=275)
    ttel = customtkinter.CTkLabel(frame1, text='Phone:', text_color='#0CC9A9', font=font1)
    ttel.place(x=255, y=335)
    tsex = customtkinter.CTkLabel(frame1, text="Sex:", text_color='#0CC9A9', font=font1)
    tsex.place(x=255, y=395)

    nom = customtkinter.CTkEntry(frame1, font=font2, placeholder_text_color="#a3a3a3",
                                 text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                 border_width=2, width=300, height=35, corner_radius=35, textvariable=nomv,
                                 placeholder_text='Nom')
    nom.place(x=250, y=60)
    prenoms = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                     placeholder_text_color="#a3a3a3",
                                     text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                     border_width=2, width=300, height=35, corner_radius=35, textvariable=prenomsv)
    prenoms.place(x=250, y=120)

    option1 =  ['IMTICIA', 'IGGLA', 'ICMP', 'ISAIA', 'TOUR', 'EMII', 'FIC', 'CAA', 'DTJA', 'BIO', 'ESIA']
    variable2 = StringVar()
    classe = customtkinter.CTkOptionMenu(frame1, dropdown_font=font2,

                                         bg_color='#001220', corner_radius=15,
                                         fg_color='#001220', font=font2,
                                         variable=variable2, values=option1, state='readonly',
                                         text_color='#fff', dropdown_hover_color='#0CC9A9', dropdown_fg_color=
                                         '#001220', width=300, height=30)
    classe.set('IMTICIA')
    classe.pack()
    classe.place(x=250, y=180)
    option1 = ["1", "2", "3", "4", "5"]
    variable3 = StringVar()
    classean = customtkinter.CTkOptionMenu(frame1, dropdown_font=font2,
                                           bg_color='#001220', corner_radius=15,
                                           fg_color='#001220',
                                           font=font2,
                                           variable=variable3, values=option1, state='readonly',
                                           text_color='#fff', dropdown_hover_color='#0CC9A9', dropdown_fg_color=
                                           '#001220', width=300, height=30)
    classean.set('Annee')
    classean.pack()
    classean.place(x=350, y=180)

    daten = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Date of birth',
                                   placeholder_text_color="#a3a3a3",
                                   text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                   border_width=2, width=300, height=35, corner_radius=35, textvariable=datev)
    daten.place(x=250, y=240)
    age = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='age',
                                 placeholder_text_color="#a3a3a3",
                                 text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                 border_width=2, width=300, height=35, corner_radius=35, textvariable=agev)
    age.place(x=250, y=300)
    tel = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='téléphone',
                                 placeholder_text_color="#a3a3a3",
                                 text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                 border_width=2, width=300, height=35, corner_radius=35, textvariable=telv)
    tel.place(x=250, y=360)
    option = ['Male', 'Female']
    variable1 = StringVar()
    gender_select = customtkinter.CTkOptionMenu(frame1, dropdown_font=font2,
                                                bg_color='#121111', corner_radius=15,
                                                fg_color='#0CC9A9', font=font2,
                                                variable=variable1, values=option, state='readonly',
                                                text_color='#fff', dropdown_hover_color='#0CC9A9', dropdown_fg_color=
                                                '#001220', width=125,
                                                height=30)
    gender_select.set('Sexe')
    gender_select.pack()
    gender_select.place(x=350, y=400)

    def prend():
        nom_value = nomv.get()
        prenoms_value = prenomsv.get()
        classe_value = variable2.get()
        daten_value = datev.get()
        age_value = agev.get()
        tel_value = telv.get()
        genre_val = variable1.get()
        anne = variable3.get()
        if anne == "Annee" or genre_val == "Sex":
            messagebox.showinfo("Alerte", "Veuillez completez vos sexe et classe")
        else:
            return nom_value, prenoms_value, classe_value, daten_value, age_value, tel_value, genre_val, anne

        return nom_value, prenoms_value, classe_value, daten_value, age_value, tel_value, genre_val, anne

    sign_up_bt = customtkinter.CTkButton(frame1, text='REGISTER', text_color="#fff", font=font2, fg_color='#0CC9A9',
                                         hover_color='#33050B',
                                         bg_color='#121111', cursor='hand2', corner_radius=5, width=120,
                                         command=lambda: (app.destroy())
                                         )
    sign_up_bt.place(x=350, y=460)
    app.mainloop()
    nom_value, prenoms_value, classe_value, daten_value, age_value, tel_value, genre, annee = prend()
    print(genre)
    print(classe_value)
    print(annee)
    return nom_value, prenoms_value, classe_value, daten_value, age_value, tel_value, genre, annee
