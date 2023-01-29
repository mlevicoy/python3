import pandas as pd
import numpy as np

# Con series
serie1 = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
print(serie1)

serie2 = pd.Series([3, 4, 5, 6], index=['a', 'b', 'c', 'd'])
print(serie2)

# Sumamos los valores que tienen el mismo indice, si no existe el 
# indice da un valor nulo
# a    3.0
# b    5.0
# c    7.0
# d    NaN
# dtype: float64
print(serie1 + serie2)

# Con DataFrame
lista_valores = np.arange(4).reshape(2,2)
lista_indices = list('ab')
lista_columnas = list('12')
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

lista_valores_2 = np.arange(9).reshape(3,3)
lista_indices_2 = list('abc')
lista_columnas_2 = list('123')
dataframe_2 = pd.DataFrame(lista_valores_2, index=lista_indices_2, columns=lista_columnas_2)
print(dataframe_2)

# Sumar los elementos que coincidan, los demas lo pone nulo
#     1    2   3
# a  0.0  2.0 NaN
# b  5.0  7.0 NaN
# c  NaN  NaN NaN
dataframe_3 = dataframe + dataframe_2

# Para solucionar el problema de los Null
# En el dataframe_2, los valores que no existen los rellenamos con ceros 
dataframe_4 = dataframe.add(dataframe_2, fill_value=0)
print(dataframe_4)
