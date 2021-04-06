from tkinter import *

root=Tk()
root.title("HOLA")

def prueba():
    top = Tk()
    top.title("Seee")
    l=Label(top, text= "Jaaaa")
    l.place(x=100, y=50)
  

boton = Button(root, text="Pruebaaa", command=prueba)
boton.place(x=10, y=10)

root.mainloop()