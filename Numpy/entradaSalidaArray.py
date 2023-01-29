import numpy as np

# [0 1 2 3 4 5]
array1 = np.arange(6)
print(array1)

# salvamos el array y lo renombramos
np.save('array1s', array1)
# rescatamos el array
np.load('array1s.npy')
print(np.load('array1s.npy'))

# otro 2 array
# array2 = [0 1 2 3 4 5]
# array3 = [0 1 2 3 4 5 6 7]
array2 = np.arange(6)
array3 = np.arange(8)
print(array2)
print(array3)

# salvar ambos arrays con la misma variable
# en la coordenada x le pasamos array2 y en
# la coordenada y le pasamos array3.
np.savez('arrays', x=array2, y=array3)
# rescatamos el array, npz porque son varios array
array_recuperado = np.load('arrays.npz')
# si queremos recuperar el arreglo en x
# x = [0 1 2 3 4 5]
print(array_recuperado['x'])
# si queremos recuperar el arreglo en y
# y = [0 1 2 3 4 5 6 7]
print(array_recuperado['y'])

# guardar en un archivo de texto
np.savetxt('mificheroarray.txt', array2, delimiter=',')
# recuperamos el fichero de texto
# [0. 1. 2. 3. 4. 5.]
print(np.loadtxt('mificheroarray.txt', delimiter=','))
 














