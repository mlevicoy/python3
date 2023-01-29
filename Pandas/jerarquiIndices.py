import pandas as pd
import numpy as np

# Ej. [0.10364832 0.5824513  0.64426038 0.41962231 0.46428526 0.95431195]
lista_valores = np.random.rand(6)
lista_indices = [[1, 1, 1, 2, 2, 2], ['a', 'b', 'c', 'a', 'b', 'c']]

# Ej. Generamos la serie con dos indices
# 1  a    0.594231
#    a    0.020913
#    a    0.846184
# 2  b    0.130309
#    b    0.569375
#    b    0.683207
series = pd.Series(lista_valores, index=lista_indices)
print(series)
print(series[1])
print(series[1]['b'])

# Creamos un dataframe a partir de una serie con 2 indices
#          a         b         c
# 1  0.894156  0.086921  0.577181
# 2  0.702503  0.494718  0.908787
dataframe = series.unstack()
print(dataframe)

# Creamos un dataframe
#     a   b   c   d
# 1   0   1   2   3
# 2   4   5   6   7
# 3   8   9  10  11
# 4  12  13  14  15
lista_valores = np.arange(16).reshape(4,4)
lista_indices = list('1234')
lista_columnas = list('abcd')
dataframe2 = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

# Pasamos el dataframe a una Serie con doble indice
# 1  a     0
#    b     1
#    c     2
#    d     3
# 2  a     4
#    b     5
#    c     6
#    d     7
# 3  a     8
#    b     9
#    c    10
#    d    11
# 4  a    12
#    b    13
#    c    14
#    d    15
serie2 = dataframe2.stack()
print(serie2)



