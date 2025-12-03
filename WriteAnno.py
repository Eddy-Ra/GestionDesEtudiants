import tkinter as tk
from tkinter import filedialog

app = tk.Tk()
app.title("ANNONCE")
app.geometry("700x780+300+20")
#app.maxsize("700*780")
app.configure(background='#98e39f')
app.wm_overrideredirect(True)
mess_input = tk.Entry(app, width=100,background='#4ff39f')
mess_input.pack(pady=10)

def on_key_press(event):
    if event.keysym == "Return":  # Lorsque la touche "Entrée" est pressé
        mess = mess_input.get()
        if mess:
            list_Box.insert(tk.END, mess)
            mess_input.delete(0, tk.END)
    elif event.keysym == "Escape":
        app.quit()


def button_click():
    print("Le bouton a été cliqué")

def add_mess():
    mess = mess_input.get()
    if mess:
        list_Box.insert(tk.END, mess)
        mess_input.delete(0, tk.END)


def edt_mess():
    messa = list_Box.curselection()
    if messa:
        new_mess = mess_input.get()
        if new_mess:
            list_Box.delete(messa)
            list_Box.insert(messa, new_mess)
            mess_input.delete(0, tk.END)


def delete_mess():
    message = list_Box.curselection()
    if message:
        list_Box.delete(message)


def Save():
    mes = list_Box.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            for me in mes:
                file.write(me + '\n')


def Load():
    file_path = filedialog.askopenfilename(filetypes=[("Text file", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            mess = [line.strip() for line in file.readlines()]
        list_Box.delete(0, tk.END)

        for mes in mess:
            list_Box.insert(tk.END, mes)


add_mess = tk.Button(app, text="Add-Message", command=add_mess, background='#81e39f')
add_mess.pack(pady=5)
add_mess.bind("<Key>", on_key_press)

list_Box = tk.Listbox(app, selectmode=tk.SINGLE, width=70, height=20, background='#4ff39f', font=('Arial',12))
list_Box.pack(pady=5)

BFrame = tk.Frame(app,background='#4ff39f')
BFrame.pack(pady=5)
edit_mess = tk.Button(BFrame, text="Edit-Message", command=edt_mess, background='#81e39f')
edit_mess.grid(row=0, column=0, padx=5)

delete_mess = tk.Button(BFrame, text="Delete-Message", command=delete_mess, background='#81e39f')
delete_mess.grid(row=0, column=1, padx=5)

save = tk.Button(app, text="Save", command=Save,background='#81e39f')
save.pack(pady=5)

load = tk.Button(app, text="Load", command=Load, background='#81e39f')
load.pack(pady=5)

qt = tk.Button(app, text="Exit", command=app.quit, background='#81e39f')
qt.pack(pady=5)

scroll = tk.Scrollbar(app,orient='vertical')
scroll.config(command=list_Box.yview)
scroll.pack(side='right', fill='y')
list_Box.config(yscrollcommand=scroll.set)
app.bind("<Key>", on_key_press)
app.mainloop()
