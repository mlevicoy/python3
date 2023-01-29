import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def accion():
	print("Hola mundo")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="white", bg="green")
boton.pack()

raiz.mainloop()