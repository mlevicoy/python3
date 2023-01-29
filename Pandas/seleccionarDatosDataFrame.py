import pandas as pd
import numpy as np

# Generamos una lista de 25 valores distribuidos
# en 5 filas y 5 columnas
lista_valores = np.arange(25).reshape(5,5)
# Son 5 filas por ende 5 indices
lista_indices = ['i1', 'i2', 'i3', 'i4', 'i5']
# Generamos las columnas
lista_columnas = ['c1', 'c2', 'c3', 'c4', 'c5']
# Generamos el dataframe
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

# Mostramos una columna del dataframe
print(dataframe['c2'])

# Mostramos un elemento es decir columna x fila
print(dataframe['c3']['i1'])

# Mostrar varias columnas
print(dataframe[['c2','c5']])

# Mostramos el dataframe donde la c2 sea mayor a 15
print(dataframe[dataframe['c2'] > 15])

# Muestra True o False cuando los valores son mayores que 20
print(dataframe > 20)

# Seleccionamos por indice
print(dataframe.loc['i5'])




