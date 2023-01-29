#Se importan todas las librerias de tkinter
from tkinter import *

#Generamos el elemento raiz (ventana)
ventana = Tk()
ventana.title("Calculadora")
#Indicamos el tamaño
ventana.geometry("350x600")
#Que no se pueda redimensionar
ventana.resizable(False,False)
#Color de la ventana
ventana.configure(background="gray")

#Variables
operacion = ""
resultado = StringVar()

#Funciones
def borrar():
	global operacion #Variable global
	global resultado #Variable global
	operacion = "" #Vacia variable
	pantalla.delete(0, END) #Borra el Entry
def pulsar(valor):
	global operacion #Variable global
	global resultado #Variable global
	operacion = operacion + str(valor) #Concatena	
	pantalla.delete(0, END) #Borra la pantalla
	pantalla.insert(0, operacion) #Muestra lo concatenado
def calcular():
	global operacion #Variable global
	global resultado #Variable global
	try:
		#Evalua lo concatenado
		resultado = str(eval(operacion))
	except:
		resultado = "Error"
	finally:
		pantalla.delete(0, END)
		pantalla.insert(0, resultado)

#Display de los resultados
pantalla = Entry(ventana, font=("Arial", 20, "bold"), width=17, borderwidth=2)
#Cantidad de filas y columnas que ocupa el display junto
#con el espaciado en X e Y
pantalla.grid(row=0, column=0, columnspan=3, pady=10, padx=5)
#Botón de reiniciar operación
boton_reset = Button(ventana, text="AC", width=8, height=2, command=lambda:borrar())
#Posición del botón
boton_reset.grid(row=0, column=3, pady=10, padx=5)

#Botones de la primera fila
ancho = 8
alto = 3

boton1 = Button(ventana, text="1", width=ancho, height=alto, command=lambda:pulsar("1"))
boton1.grid(row=1, column=0, padx=5, pady=5)

boton2 = Button(ventana, text="2", width=ancho, height=alto, command=lambda:pulsar("2"))
boton2.grid(row=1, column=1, padx=5, pady=5)

boton3 = Button(ventana, text="3", width=ancho, height=alto, command=lambda:pulsar("3"))
boton3.grid(row=1, column=2, padx=5, pady=5)

boton4 = Button(ventana, text="4", width=ancho, height=alto, command=lambda:pulsar("4"))
boton4.grid(row=1, column=3, padx=5, pady=5)

#Botones de la segunda fila
boton5 = Button(ventana, text="5", width=ancho, height=alto, command=lambda:pulsar("5"))
boton5.grid(row=2, column=0, padx=5, pady=5)

boton6 = Button(ventana, text="6", width=ancho, height=alto, command=lambda:pulsar("6"))
boton6.grid(row=2, column=1, padx=5, pady=5)

boton7 = Button(ventana, text="7", width=ancho, height=alto, command=lambda:pulsar("7"))
boton7.grid(row=2, column=2, padx=5, pady=5)

boton8 = Button(ventana, text="8", width=ancho, height=alto, command=lambda:pulsar("8"))
boton8.grid(row=2, column=3, padx=5, pady=5)

#Botones de la tercera fila
boton9 = Button(ventana, text="9", width=ancho, height=alto, command=lambda:pulsar("9"))
boton9.grid(row=3, column=0, padx=5, pady=5)

boton0 = Button(ventana, text="0", width=ancho, height=alto, command=lambda:pulsar("0"))
boton0.grid(row=3, column=1, padx=5, pady=5)

boton_punto = Button(ventana, text=".", width=ancho, height=alto, command=lambda:pulsar("."))
boton_punto.grid(row=3, column=2, padx=5, pady=5)

boton_suma = Button(ventana, text="+", width=ancho, height=alto, command=lambda:pulsar("+"))
boton_suma.grid(row=3, column=3, padx=5, pady=5)

#Botones de la cuarta fila
boton_resta = Button(ventana, text="-", width=ancho, height=alto, command=lambda:pulsar("-"))
boton_resta.grid(row=4, column=0, padx=5, pady=5)

boton_multi = Button(ventana, text="*", width=ancho, height=alto, command=lambda:pulsar("*"))
boton_multi.grid(row=4, column=1, padx=5, pady=5)

boton_divi = Button(ventana, text="/", width=ancho, height=alto, command=lambda:pulsar("/"))
boton_divi.grid(row=4, column=2, padx=5, pady=5)

boton_igual = Button(ventana, text="=", width=ancho, height=alto, command=lambda:calcular())
boton_igual.grid(row=4, column=3, padx=5, pady=5)

#Que el programa siempre se ejecute
ventana.mainloop()
