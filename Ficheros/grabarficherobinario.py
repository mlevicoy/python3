import pickle

lista_colores = ["azul", "verde", "rojo", "amarillo"]

fichero = open("ficherocolores.pckl", "wb")

pickle.dump(lista_colores, fichero)

fichero.close()

