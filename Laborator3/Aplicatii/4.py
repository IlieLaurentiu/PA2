import tkinter as tk

root = tk.Tk()
root.title("Aplicație 2")

# PRIMUL CADRU
cadru_1 = tk.Frame(root, bd=3, relief=tk.SUNKEN, height=100, width=100)
cadru_1.pack(fill=tk.X, side="left", padx=5, pady=5)

# Adăugăm caseta de text (control tip Entry) la cadru_1
textulAfisat = tk.StringVar()
entry = tk.Entry(cadru_1, textvariable=textulAfisat)
entry.pack()
textulAfisat.set("Aici inserați un text")

# Adăugăm 3 căsuțe de bifat (control tip Checkbutton) la cadru_1
tk.Checkbutton(cadru_1, text="1600").pack()
tk.Checkbutton(cadru_1, text="1877").pack()
tk.Checkbutton(cadru_1, text="1918").pack()

# Adăugăm un OptionMenu la cadru_1
optiune_selectata = tk.StringVar()
optiune_selectata.set("Alege un domnitor")
tk.OptionMenu(cadru_1, optiune_selectata,
              "Bogdan", "Neagoe Basarab", "Mihai Viteazul", "Matei Basarab",
              "Constantin Brâncoveanu").pack()

# AL DOILEA CADRU
cadru_2 = tk.Frame(root, bd=3, relief=tk.RAISED, height=200, width=400)
cadru_2.pack(fill=tk.Y, padx=5, pady=5, ipady=5, side="right")

# Adăugăm un control LabelFrame la cadru_2
cadruEticheta1 = tk.LabelFrame(cadru_2, text="Domni din Oltenia", padx=5, pady=5)
cadruEticheta1.pack(padx=10, pady=10)

# Adăugăm un control Message la cadruEticheta1
tk.Message(cadruEticheta1, text="Derulați sus-jos", width=200).pack()

# Adăugăm un control Listbox la cadruEticheta1
listaOptiuni = tk.Listbox(cadruEticheta1, height=3)
optiuni = ["Tudor Vladimirescu", "Barbu Dimitrie Știrbei", "Gheorghe Bibescu"]
for optiune in optiuni:
    listaOptiuni.insert(tk.END, optiune)
listaOptiuni.pack()

# Adăugăm un control LabelFrame la cadru_2
cadruEticheta2 = tk.LabelFrame(cadru_2, text="Bătălii victorioase ale românilor", padx=5, pady=5)
cadruEticheta2.pack(padx=10, pady=10)

# Adăugăm un control Message la cadruEticheta2
tk.Message(cadruEticheta2, text="Derulați din dreapta sus-jos", width=200).pack()

# Adăugăm un control Spinbox la cadruEticheta2
tk.Spinbox(cadruEticheta2, values=(1330, 1394, 1462, 1475, 1595)).pack()

root.mainloop()