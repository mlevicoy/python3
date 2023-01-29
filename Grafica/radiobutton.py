import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos los radiobutton

def seleccionar():
	print("La opción seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

botonradio1 = tkinter.Radiobutton(raiz, text="Opción 1", variable=opcion, value=1, command=seleccionar)
botonradio1.pack()

botonradio2 = tkinter.Radiobutton(raiz, text="Opción 2", variable=opcion, value=2, command=seleccionar)
botonradio2.pack()

botonradio3 = tkinter.Radiobutton(raiz, text="Opción 3", variable=opcion, value=3, command=seleccionar)
botonradio3.pack()

raiz.mainloop()