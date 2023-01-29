# Importamos los modulos
import pandas as pd
import numpy as np

# Mostramos un array(4)
# [0 1 2 3]
print(np.arange(4))

# Generamos la serie
serie = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
print(serie)

# Eliminamos un elemento de una serie usando su índice
print(serie.drop('c'))

# Eliminamos a través de un Dataframe
# [[0 1 2], [3 4 5], [6 7 8]]
lista_valores = np.arange(9).reshape(3, 3)
lista_indices = ['a', 'b', 'c']
lista_columnas = ['c1', 'c2', 'c3']
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
#    c1  c2  c3
# a   0   1   2
# b   3   4   5
# c   6   7   8

# Eliminamos la fila b
print(dataframe.drop('b'))
#    c1  c2  c3
# a   0   1   2
# c   6   7   8

# Eliminamos la c2
print(dataframe.drop('c2', axis=1))
#    c1  c3
# a   0   2
# b   3   5
# c   6   8







