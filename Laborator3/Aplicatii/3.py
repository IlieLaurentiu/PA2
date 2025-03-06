import tkinter as tk

root = tk.Tk()
root.title("Aplicație 1")

tk.Label(root, text="Etichetă deasupra cadrelor").pack()

# Cadrul butoanelor 1 și 2
cadru_1 = tk.Frame(root, bd=3, relief=tk.SUNKEN, height=100, width=100)
cadru_1.pack(fill=tk.X)

tk.Button(cadru_1, text="Click1", font="Helvetica 16 bold", fg="blue", bg="yellow").pack(side="top")
tk.Button(cadru_1, text="Click2", font="Helvetica 16 bold", fg="black", bg="pink").pack()

tk.Label(root, text="Etichetă separatoare a cadrelor 1").pack()

# Cadrul butoanelor 3, 4 și 5
cadru_2 = tk.Frame(root, bd=3, relief=tk.RAISED, height=200, width=400)
cadru_2.pack(fill=tk.Y, padx=5, pady=5, ipady=5)

tk.Button(cadru_2, text="Click3", font="Helvetica 16 bold", fg="brown", bg="white").pack(
    side="left", padx=5, pady=5, ipadx=15, ipady=5)
tk.Button(cadru_2, text="Click4", font="Helvetica 16 bold", fg="green", bg="light gray").pack(
    side="left", padx=5, pady=5, ipadx=15, ipady=5)
tk.Button(cadru_2, text="Click5", font="Helvetica 16 bold", fg="dark blue", bg="light yellow").pack(
    side="right", padx=5, pady=5, ipadx=15, ipady=5)

tk.Label(root, text="Etichetă separatoare a cadrelor 2").pack()

# Cadrul butoanelor radio
cadru_3 = tk.Frame(root, bd=3, relief=tk.GROOVE, height=200, width=200)
cadru_3.pack(fill=tk.Y, padx=5, pady=5, ipady=5)

tk.Radiobutton(cadru_3, text='Roșu', value=1).pack(side="left")
tk.Radiobutton(cadru_3, text='Galben', value=2).pack(side="left")
tk.Radiobutton(cadru_3, text='Albastru', value=3).pack(side="right")

root.mainloop()