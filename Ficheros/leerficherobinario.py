import pickle

fichero = open("ficherocolores.pckl", "rb")

lista_leida_fichero = pickle.load(fichero)

print(lista_leida_fichero)