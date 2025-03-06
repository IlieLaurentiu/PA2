import tkinter as tk

root = tk.Tk()
root.title("Aplicație 2")

# Checkbutton-uri
tk.Checkbutton(root, text="Text 1").grid(row=0, column=0, sticky="e")
tk.Checkbutton(root, text="Text 2").grid(row=0, column=1, sticky="e")

# Spinbox
tk.Spinbox(root, values=("abc", "cde", "fgh", "ijk", "lmn")).grid(
    row=0, column=2, columnspan=2, sticky="ew"
)

# Butoane
tk.Button(root, text="Buton 1").grid(row=1, column=0, sticky="ew", padx=2, pady=2)
tk.Button(root, text="Buton 2").grid(row=1, column=1, sticky="ew", padx=2, pady=2)
tk.Button(root, text="Buton 3 Buton 3 Buton 3").grid(
    row=1, column=2, columnspan=2, sticky="w", padx=2
)

# Etichetă și câmp de introducere
tk.Label(root, text="Eticheta 1:").grid(row=2, column=0, sticky="e")
tk.Entry(root).grid(row=2, column=1, columnspan=3, sticky="we", padx=4)

# Text
tk.Label(root, text="TEXT TEXT TEXT TEXT").grid(row=3, column=0, columnspan=2, sticky="w")

# Cadru etichetă
cadruEticheta = tk.LabelFrame(root, text="Eticheta de cadru")
cadruEticheta.grid(row=3, column=2, columnspan=2, rowspan=4, ipadx=3, ipady=10)
tk.Entry(cadruEticheta).grid()

# Radiobutton-uri
var = tk.IntVar()  # Variabilă pentru a gestiona butoanele radio
tk.Radiobutton(root, text="Text 1", variable=var, value=1).grid(row=4, column=0, sticky="w")
tk.Radiobutton(root, text="Text 2", variable=var, value=2).grid(row=4, column=1, sticky="e")
tk.Radiobutton(root, text="Text 3", variable=var, value=3).grid(row=5, column=0, sticky="w")
tk.Radiobutton(root, text="Text 4", variable=var, value=4).grid(row=5, column=1, sticky="e")

root.mainloop()