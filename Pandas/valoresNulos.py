import pandas as pd
import numpy as np

# Para agregar un valor nulo se usa pn.nan
# ['1', '2', nan, '4']
lista_valores = ['1', '2', np.nan, '4']
print(lista_valores)

# a      1
# b      2
# c    NaN
# d      4
serie = pd.Series(lista_valores, index=list('abcd'))
print(serie)

# Verificamos los null
# a    False
# b    False
# c     True
# d    False
print(serie.isnull())

# Eliminar los valores null
# a    1
# b    2
# d    4
print(serie.dropna())

# Borrarlos definitivos
# a    1
# b    2
# d    4
serie = serie.dropna()
print(serie)

# Generamos un dataframe
#    a    b    c
# 1  1  2.0  3.0
# 2  4  NaN  5.0
# 3  6  7.0  NaN
lista_valores = [[1, 2, 3], [4, np.nan, 5], [6, 7, np.nan]]
lista_indices = list('123')
lista_columnas = list('abc')
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

# Verificamos los nulos
#       a      b      c
# 1  False  False  False
# 2  False   True  False
# 3  False  False   True
print(dataframe.isnull())

# Eliminar filas con datos nulos
#   a    b    c
# 1  1  2.0  3.0
print(dataframe.dropna())

# Para poder operar sobre el dataframe, rellenamos los nulos con ceros
#    a    b    c
# 1  1  2.0  3.0
# 2  4  0.0  5.0
# 3  6  7.0  0.0
print(dataframe.fillna(0))

# Mantener los cambios
#    a    b    c
# 1  1  2.0  3.0
# 2  4  0.0  5.0
# 3  6  7.0  0.0
dataframe = dataframe.fillna(0)
print(dataframe)



