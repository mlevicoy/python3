# importamos el modulo
import numpy as np

# generamos un array que va del 0 al 10
# array([0,1,2,3,4,5,6,7,8,9,10])
array = np.arange(0,11)
print(array)

# toma elementos del 0 al 3
# array([0,1,2])
array[0:3]
print(array[0:3])

# toma elementos del 2 al 5
# array([2,3,4])
array[2:5]
print(array[2:5])

# tomar todos los elementos
array[:]
print(array[:])

# genera una copia
array_copia = array.copy()

# cambiar valores
# array_copia([20 20 20  3  4  5  6  7  8  9 10])
array_copia[0:3] = 20
print(array_copia[:])

# array de varias dimensiones 3 filas x 3 columnas
array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2)

# acceder a las filas
print(array2[0])
print(array2[1])
print(array2[2])

# acceder a un elemento de la columna
# se coloca la fila y la columna
# ejemplo el array2[1][0] = 4
print(array2[1][0])





















