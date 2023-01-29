import numpy as np

array = np.arange(5)
print(array)

# raiz cuadrada de cada elemento
# [0.         1.         1.41421356 1.73205081 2.        ]
print(np.sqrt(array))

# crear array de forma aleatoria
# [0.37149848 0.77784299 0.49200287 0.37921762 0.00463392]
print(np.random.rand(5))

# array a partir de una lista
# [5 6 7 8]
lista = [5, 6, 7, 8]
array2 = np.array(lista)
print(array2)

# [6 6 6 6 6] suma los elementos de los array
array = [1, 2, 3, 4, 5]
array2 = [5, 4, 3 ,2 ,1]
print(np.add(array, array2))

# [5 4 3 4 5] maximo de cada elemento de los array
print(np.maximum(array, array2))


