import tkinter as tk

root = tk.Tk()
root.title('Radacina, nivelul superior, containerul tuturor')

# MENIUL
# Cream un cadru (meniu bara) pentru plasarea meniului
meniuBara = tk.Frame(root)
meniuBara.pack(fill=tk.X)

# Cream Meniu 1 si subMeniu 1 in cadrul meniuBara
Meniu_1 = tk.Menubutton(meniuBara, text='Meniu 1')
Meniu_1.pack(side=tk.LEFT)

# SubMeniu 1
subMeniu_1 = tk.Menu(Meniu_1, tearoff=0)
Meniu_1['menu'] = subMeniu_1
subMeniu_1.add_command(label='subMeniu 1')

# Cream Meniu 2 si subMeniu 2 in cadrul meniuBara
Meniu_2 = tk.Menubutton(meniuBara, text='Meniu 2')
Meniu_2.pack(side=tk.LEFT)

# SubMeniu 2
subMeniu_2 = tk.Menu(Meniu_2, tearoff=0)
Meniu_2['menu'] = subMeniu_2
subMeniu_2.add_command(label='subMeniu 2')

# CADRUL 1
cadru_1 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
cadru_1.pack(side=tk.LEFT)

tk.Label(cadru_1, text='Eticheta cadrului 1').pack()

textulAfisat = tk.StringVar()
tk.Entry(cadru_1, textvariable=textulAfisat).pack()
textulAfisat.set('Continut caseta de text')

tk.Button(cadru_1, text='Buton\ndin cadrul 1').pack()
tk.Checkbutton(cadru_1, text='Casuta de bifat din cadrul 1').pack()

tk.Radiobutton(cadru_1, text='Rosu', value=1).pack()
tk.Radiobutton(cadru_1, text='Galben', value=2).pack()
tk.Radiobutton(cadru_1, text='Albastru', value=3).pack()

tk.Label(cadru_1, text='OptionMenu:\nJudetele Olteniei').pack()
tk.OptionMenu(cadru_1, tk.StringVar(), 'Dolj', 'Olt', 'Gorj', 'Valcea', 'Mehedinti').pack()

tk.Label(cadru_1, text='Mihai Viteazul\n(1593-1601)').pack()
imagineMV = tk.BitmapImage(file="MihaiViteazul.xbm")
etichetaMV = tk.Label(cadru_1, image=imagineMV)
etichetaMV.image = imagineMV
etichetaMV.pack()

# CADRUL 2
cadru_2 = tk.Frame(root, bd=2, relief=tk.GROOVE)
cadru_2.pack(side=tk.RIGHT)

tk.Label(cadru_2, text='Drapel afisat cu clasa:\nPhotoImage').pack()
drapel = tk.PhotoImage(file='Romania.gif')
drapel_label = tk.Label(cadru_2, image=drapel)
drapel_label.image = drapel
drapel_label.pack()

tk.Label(cadru_2, text='Listbox cu provinciile Romaniei').pack()
listaOptiuni = tk.Listbox(cadru_2, height=3)
provincii = ['Ardeal', 'Banat', 'Bucovina', 'Crisana', 'Dobrogea', 'Maramures', 'Moldova', 'Muntenia', 'Oltenia']
for line in provincii:
    listaOptiuni.insert(tk.END, line)
listaOptiuni.pack()

tk.Label(cadru_2, text='Control spinbox cu numere prime:').pack()
tk.Spinbox(cadru_2, values=(2, 3, 5, 7, 11)).pack()

tk.Scale(cadru_2, from_=0.0, to=33.0, label='Control scala', orient=tk.HORIZONTAL).pack()

cadruEticheta = tk.LabelFrame(cadru_2, text="Control LabelFrame", padx=5, pady=5)
cadruEticheta.pack(padx=10, pady=10)
tk.Entry(cadruEticheta).pack()

tk.Message(cadru_2, text='Mesaj afisat cu controlul Message').pack()

# CADRUL 3
cadru_3 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
cadru_3.pack()

ctrlText = tk.Text(cadru_3, height=8, width=24)
file_object = open('controale.txt')
file_content = file_object.read()
file_object.close()
ctrlText.insert(tk.END, file_content)
ctrlText.pack(side=tk.LEFT, fill=tk.X, padx=5)

derulare = tk.Scrollbar(cadru_3, orient=tk.VERTICAL, command=ctrlText.yview)
ctrlText.configure(yscrollcommand=derulare.set)
derulare.pack(side=tk.RIGHT, fill=tk.Y)

# CADRUL 4
cadru_4 = tk.Frame(root)
cadru_4.pack()

panza = tk.Canvas(cadru_4, bg='yellow', width=340, height=90)
panza.pack()

panza.create_oval(115, 10, 45, 75, fill='green')
puncte = [10, 10, 80, 30, 5, 65]
panza.create_polygon(puncte, outline='blue', fill='red', width=5)
panza.create_text(220, 50, text='Tablou:\nSuprematism, Kazimir Malevich', font=('Verdana', 10))

# Control fereastra divizata (PanedWindow)
tk.Label(root, text='Control tip PanedWindow:').pack()
tk.Label(root, text='Cadrele se pot dimensiona tragand de ele').pack()

my_paned_window_1 = tk.PanedWindow()
my_paned_window_1.pack(fill=tk.BOTH, expand=2)

left_pane_text = tk.Text(my_paned_window_1, height=6, width=15)
my_paned_window_1.add(left_pane_text)

my_paned_window_2 = tk.PanedWindow(my_paned_window_1, orient=tk.VERTICAL)
my_paned_window_1.add(my_paned_window_2)

top_pane_text = tk.Text(my_paned_window_2, height=3, width=3)
my_paned_window_2.add(top_pane_text)

bottom_pane_text = tk.Text(my_paned_window_2, height=3, width=3)
my_paned_window_2.add(bottom_pane_text)

root.mainloop()
