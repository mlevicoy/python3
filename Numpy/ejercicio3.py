import numpy as np

# lista con 30 elementos
lista1 = np.arange(30)
print(lista1)
# primeros 10 elementos
primeros10 = lista1[0:10]
print(primeros10)
print(primeros10.shape)
# últimos 10 elementos
ultimos10 = lista1[-10:]
print(ultimos10)
print(ultimos10.shape)
# recorremos la lista
for numero in ultimos10:
    print(numero)