from tkinter import END, StringVar, messagebox
from BD import nouvempl


def interface():
    import customtkinter
    app = customtkinter.CTk()
    app.title('Emplois du temps')
    app.minsize(700, 500)
    app.maxsize(700, 500)
    app.config(bg='#001220')

    font1 = ('Helvetica', 17, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')
    # var
    lundi1 = StringVar()
    lundi2 = StringVar()
    lundi3 = StringVar()
    lundi4 = StringVar()

    mardi1 = StringVar()
    mardi2 = StringVar()
    mardi3 = StringVar()
    mardi4 = StringVar()

    mercredi1 = StringVar()
    mercredi2 = StringVar()
    mercredi3 = StringVar()
    mercredi4 = StringVar()

    jeudi1 = StringVar()
    jeudi2 = StringVar()
    jeudi3 = StringVar()
    jeudi4 = StringVar()

    vendredi1 = StringVar()
    vendredi2 = StringVar()
    vendredi3 = StringVar()
    vendredi4 = StringVar()
    frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=800, height=500)
    frame1.place(x=0, y=0)

    frame1.place(x=0, y=0)
    sign_up_label = customtkinter.CTkLabel(frame1, text=f'Emlois du temps', fg_color='#0CC9A9',
                                           bg_color='#121111', corner_radius=5, width=120,
                                           )
    sign_up_label.place(x=300, y=5)

    lundi = customtkinter.CTkLabel(frame1, text='Lundi', text_color='#0CC9A9', font=font1)
    lundi.place(x=100, y=35)
    mardi = customtkinter.CTkLabel(frame1, text='Mardi', text_color='#0CC9A9', font=font1)
    mardi.place(x=210, y=35)
    mercredi = customtkinter.CTkLabel(frame1, text='Mercredi', text_color='#0CC9A9', font=font1)
    mercredi.place(x=320, y=35)
    jeudi = customtkinter.CTkLabel(frame1, text='jeudi', text_color='#0CC9A9', font=font1)
    jeudi.place(x=440, y=35)
    vendredi = customtkinter.CTkLabel(frame1, text='Vendredi', text_color='#0CC9A9', font=font1)
    vendredi.place(x=540, y=35)

    lundi1 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=lundi1,
                                    placeholder_text='Nom')
    lundi1.place(x=100, y=60)
    lundi2 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=lundi2,
                                    placeholder_text='Nom')
    lundi2.place(x=100, y=100)
    lundi3 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=lundi3,
                                    placeholder_text='Nom')
    lundi3.place(x=100, y=140)
    lundi4 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=lundi4,
                                    placeholder_text='Nom')
    lundi4.place(x=100, y=180)

    mardi1 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=mardi1)
    mardi1.place(x=210, y=60)
    mardi2 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=mardi2)
    mardi2.place(x=210, y=100)
    mardi3 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=mardi3)
    mardi3.place(x=210, y=140)
    mardi4 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e', border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=mardi4)
    mardi4.place(x=210, y=180)

    mercredi1 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=mercredi1)
    mercredi1.place(x=320, y=60)
    mercredi2 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=mercredi2)
    mercredi2.place(x=320, y=100)
    mercredi3 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=mercredi3)
    mercredi3.place(x=320, y=140)
    mercredi4 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=mercredi4)
    mercredi4.place(x=320, y=180)

    jeudi1 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                    border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=jeudi1)
    jeudi1.place(x=430, y=60)
    jeudi2 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                    border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=jeudi2)
    jeudi2.place(x=430, y=100)
    jeudi3 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                    border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=jeudi3)
    jeudi3.place(x=430, y=140)
    jeudi4 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                    placeholder_text_color="#a3a3a3",
                                    text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                    border_color='#004780',
                                    border_width=2, width=100, height=35, corner_radius=35, textvariable=jeudi4)
    jeudi4.place(x=430, y=180)
    vendredi1 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=vendredi1)
    vendredi1.place(x=540, y=60)
    vendredi2 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=vendredi2)
    vendredi2.place(x=540, y=100)
    vendredi3 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=vendredi3)
    vendredi3.place(x=540, y=140)
    vendredi4 = customtkinter.CTkEntry(frame1, font=font2, placeholder_text='Prénoms',
                                       placeholder_text_color="#a3a3a3",
                                       text_color='#fff', bg_color='#001220', fg_color='#001a2e',
                                       border_color='#004780',
                                       border_width=2, width=100, height=35, corner_radius=35, textvariable=vendredi4)
    vendredi4.place(x=540, y=180)

    option = ['IMTICIA', 'IGGLA', 'ICMP', 'ISAIA', 'TOUR', 'EMII', 'FIC', 'CAA', 'DTJA', 'BIO', 'ESIA']
    variable = StringVar()
    gender_select = customtkinter.CTkOptionMenu(frame1, dropdown_font=font2,
                                                bg_color='#121111', corner_radius=15,
                                                fg_color='#0CC9A9', font=font2,
                                                variable=variable, values=option, state='readonly',
                                                text_color='#fff', dropdown_hover_color='#0CC9A9', dropdown_fg_color=
                                                '#001220', width=125,
                                                height=30)
    gender_select.set('Classe')
    gender_select.pack()
    gender_select.place(x=250, y=240)

    option = ['1', '2', '3', '4', '5']
    variable1 = StringVar()
    gender_select1 = customtkinter.CTkOptionMenu(frame1, dropdown_font=font2,
                                                 bg_color='#121111', corner_radius=15,
                                                 fg_color='#0CC9A9', font=font2,
                                                 variable=variable1, values=option, state='readonly',
                                                 text_color='#fff', dropdown_hover_color='#0CC9A9', dropdown_fg_color=
                                                 '#001220', width=125,
                                                 height=30)
    gender_select1.set('Année')
    gender_select1.pack()
    gender_select1.place(x=400, y=240)

    # Définir la fonction prend avec n comme argument
    tabl, tabm, tabmerc, tabj, tabv, classent = [], [], [], [], [], []

    def prend():
        nonlocal tabl, tabm, tabmerc, tabj, tabv, classent
        # prend
        tabl = lundi1.get(), lundi2.get(), lundi3.get(), lundi4.get()
        tabm = mardi1.get(), mardi2.get(), mardi3.get(), mardi4.get()
        tabmerc = mercredi1.get(), mercredi2.get(), mercredi3.get(), mercredi4.get()
        tabj = jeudi1.get(), jeudi2.get(), jeudi3.get(), jeudi4.get()
        tabv = vendredi1.get(), vendredi2.get(), vendredi3.get(), vendredi4.get()
        classent = variable.get()
        annee = (variable1.get())

        print(classent)
        print(annee)
        print(tabl)
        print(tabl, tabm, tabmerc, tabj, tabv)

        def nouvemple(lundi, mardi, mercredi, jeudi, vendredi, classe, annee):
            nouvempl(lundi, mardi, mercredi, jeudi, vendredi, classe, annee)

        if (annee != "Année") & (classent != "Classe"):
            nouvemple(tabl, tabm, tabmerc, tabj, tabv, classent, annee)
            app.destroy()
        else:
            messagebox.showwarning("alert", "Impossible")


    sign_up_bt = customtkinter.CTkButton(frame1, text='REGISTER', text_color="#fff", font=font2, fg_color='#0CC9A9',
                                         hover_color='#33050B',
                                         bg_color='#121111', cursor='hand2', corner_radius=5, width=120,
                                         command=lambda: prend()
                                         )
    sign_up_bt.place(x=200, y=360)

    def effacer():
        gender_select.set('Classe')
        gender_select1.set('Année')
        lundi1.delete(0, END)
        lundi2.delete(0, END)
        lundi3.delete(0, END)
        lundi4.delete(0, END)

        mardi1.delete(0, END)
        mardi2.delete(0, END)
        mardi3.delete(0, END)
        mardi4.delete(0, END)

        mercredi1.delete(0, END)
        mercredi2.delete(0, END)
        mercredi3.delete(0, END)
        mercredi4.delete(0, END)

        jeudi1.delete(0, END)
        jeudi2.delete(0, END)
        jeudi3.delete(0, END)
        jeudi4.delete(0, END)

        vendredi1.delete(0, END)
        vendredi2.delete(0, END)
        vendredi3.delete(0, END)
        vendredi4.delete(0, END)

    effacer_btn = customtkinter.CTkButton(frame1, text='EFACER TOUT', text_color="#fff", font=font2, fg_color='#0CC9A9',
                                          hover_color='#33050B',
                                          bg_color='#121111', cursor='hand2', corner_radius=5, width=120,
                                          command=effacer
                                          )
    effacer_btn.place(x=400, y=360)

    app.mainloop()

    return lundi, mardi, mercredi, jeudi, vendredi


lundi = ["matory", "matory"]
mardi = ["ok", " "]
mercredi = [" ", "ok"]
jeudi = ["jrie", " "]
vendredi = ["no", "no"]
interface()
