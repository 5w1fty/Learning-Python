import tkinter as tk

def zeige_auswahl():
    auswahl = listbox.get(listbox.curselection())
    label.config(text=f"Du hast {auswahl} gewählt.")

root = tk.Tk()
root.title("Liste auswählen")

listbox = tk.Listbox(root)
for item in ["Apfel", "Banane", "Kirsche", "Orange"]:
    listbox.insert(tk.END, item)
listbox.pack()

button = tk.Button(root, text="Auswählen", command=zeige_auswahl)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
