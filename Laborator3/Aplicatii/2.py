import tkinter as tk

root = tk.Tk()
root.title('Căutare și Înlocuire')

# Etichete și câmpuri de introducere text
tk.Label(root, text="Căutare:").grid(row=0, column=0, sticky='e')
tk.Entry(root, width=60).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)

tk.Label(root, text="Înlocuire:").grid(row=1, column=0, sticky='e')
tk.Entry(root).grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=9)

# Butoane de acțiune
tk.Button(root, text="Căutare").grid(row=0, column=10, sticky='ew', padx=2, pady=2)
tk.Button(root, text="Caută tot").grid(row=1, column=10, sticky='ew', padx=2)
tk.Button(root, text="Înlocuire").grid(row=2, column=10, sticky='ew', padx=2)
tk.Button(root, text="Înlocuiește tot").grid(row=3, column=10, sticky='ew', padx=2)

# Opțiuni suplimentare
tk.Checkbutton(root, text='Potrivire cuvânt întreg').grid(row=2, column=1, columnspan=4, sticky='w')
tk.Checkbutton(root, text='Ține cont de majusculă/minusculă').grid(row=3, column=1, columnspan=4, sticky='w')
tk.Checkbutton(root, text='Înfășurare').grid(row=4, column=1, columnspan=4, sticky='w')

# Opțiuni direcție
tk.Label(root, text="Direcție:").grid(row=2, column=6, sticky='w')
tk.Radiobutton(root, text='În sus', value=1).grid(row=3, column=6, sticky='w')
tk.Radiobutton(root, text='În jos', value=2).grid(row=3, column=7, sticky='e')

root.mainloop()