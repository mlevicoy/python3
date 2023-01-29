import numpy as np


# funcion que retorna array con numeros pares
def pares(inicio, fin):
    if(inicio % 2 == 0):
        # de 2 en 2
        arreglo = np.arange(inicio, fin, 2)
    else:
        inicio = inicio + 1
        arreglo = np.arange(inicio, fin, 2)
    return arreglo


array = pares(1, 30)
array2 = pares(2,40)
print(array)
print(array2)
