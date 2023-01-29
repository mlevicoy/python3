import pandas as pd
import numpy as np

lista_valores = ([1,2,3], [4,5,6], [7,8,9], [np.nan, np.nan, np.nan])
lista_columnas = list('abc')
dataframe = pd.DataFrame(lista_valores, columns=lista_columnas)
print(dataframe)

# Operaciones por columnas
#        a     b     c
# sum  12.0  15.0  18.0
# min   1.0   2.0   3.0
# max   7.0   8.0   9.0
print(dataframe.agg(['sum', 'min', 'max']))

# Operaciones por fila
# 0     6.0
# 1    15.0
# 2    24.0
# 3     0.0
print(dataframe.agg('sum', axis=1))

