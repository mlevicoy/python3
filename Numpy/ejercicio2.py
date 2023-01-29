import numpy as np
# lista que va del 10 al 19
lista_uno = np.arange(10,20)
print(lista_uno)

# lista que va del 50 al 59
lista_dos = np.arange(50,60)
print(lista_dos)

# lista doble
lista_Doble = (lista_uno, lista_dos)
print(lista_Doble)

# matriz 2X10
matriz = np.array(lista_Doble)
print(matriz)
print(matriz.shape)

# multiplicamos cada elemento por 2
matriz_multi = matriz * 2
print(matriz_multi)