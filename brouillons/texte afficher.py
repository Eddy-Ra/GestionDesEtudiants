import tkinter as tk


def show_tooltip(event, text):
    x, y, _, _ = event.widget.bbox("insert")
    x += event.widget.winfo_rootx() + 25
    y += event.widget.winfo_rooty() + 25
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



# Configuration de l'interface
root = tk.Tk()
root.geometry("300x200")

# Création d'un bouton
btn = tk.Button(root, text="Passer le curseur ici")
btn.pack(pady=50)

# Ajout des événements pour le tooltip
tooltip_window = None
btn.bind("<Enter>", lambda event: show_tooltip(event, "Ceci est un tooltip !"))
btn.bind("<Leave>", hide_tooltip)

# Lancement de la boucle principale
root.mainloop()
