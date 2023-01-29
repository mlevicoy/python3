# importamos el modulo numpy y la llamamos np
import numpy as np

# se genera un array de 4 elementos con ceros
np.zeros(4)
print(np.zeros(4))
# se genera un array de 4 elementos con unos
np.ones(4)
print(np.ones(4))
# se genera un arra de 4 elementos que va del 0 al 4
np.arange(5)
print(np.arange(5))
# similar al anterior pero del 0 al 9
np.arange(10)
print(np.arange(10))
# en este caso se pide un arreglo que comience desde el 
# 2 hasta el 20 de 3 en 3
np.arange(2,20,3)
print(np.arange(2,20,3))

# se puede crear un array a partir de una lista
lista1 = [1, 2, 3, 4]
array1 = np.array(lista1)
print(array1)

# se puede crear una array doble (dos dimensiones)
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista_doble = (lista1, lista2)
print(lista_doble)
array_doble = np.array(lista_doble)
print(array_doble)

# verificamos la forma del array, en este caso 2,
# 4 columnas
print(array_doble.shape)
# Verificar el tipo de dato del arreglo, en este caso
# int64
print(array_doble.dtype)





