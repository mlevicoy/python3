# importamos el componente numpy
import numpy as np

# generamos un arreglo de 4 elementos
array1 = np.array([1, 2, 3, 4])
print(array1)

# multiplicamos el array1 por 2 
print(array1 * 2)

# dividimos el array1 por 2
print(array1 / 2)

# sumamos 4 al array1
print(array1 + 4)

# restamos 1 al array1
print(array1 - 1)

# elevamos por 2 el array1
print(array1 ** 2)

# si se quiere mantener el valor se hace
# por ejemplo
array2 = np.array([1, 2, 3, 4])
print(array2)
array2 = array2 + 2
print(array2) 

# se puede hacer con array dobles
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1, lista2)
array_doble = np.array(lista_doble)
print(array_doble)
print(array_doble.dtype)
print(array_doble.shape)
print(array_doble + 2)
print(array_doble - 3)
print(array_doble * 4)
print(array_doble / 3)
print(array_doble ** 3)
array_doble = array_doble + 6
print(array_doble)






