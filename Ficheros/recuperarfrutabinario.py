import pickle

fichero = open("fichero.pckl", "rb")

diccionario_frutas_leido = pickle.load(fichero)
print(diccionario_frutas_leido)

print(diccionario_frutas_leido.values())
