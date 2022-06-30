from tkinter import *
from tkinter import ttk

root = Tk()

marco = ttk.Frame(root, padding=20)
marco.grid()

etiqueta = Label(root, text="Hola Thinker", padx=50, pady=25, bg='white')
etiqueta.grid(row=0, column=0)

otra = Label(root, text="Soy otra etiqueta", fg='yellow', bg='#333333', padx=100)
otra.grid(row=5, column=0, columnspan=4)

vacia = Label(marco, text="", padx=50, pady=50)
vacia.grid(row=3, column=2)

uno = Button(marco, text="click me")
uno.grid(row=2, column=1)

root.mainloop()
