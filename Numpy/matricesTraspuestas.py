# importamos el componente numpy
import numpy as np

# generamos un arreglo de 15 elementos
# repartidos entre 3 filas y 5 columnas
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
array = np.arange(15).reshape((3,5))
print(array)

# acceder a la posición 6
print(array[1][1])

# generamos la matriz traspuesta
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]
array_tras = array.T
print(array_tras)
