import pandas as pd
import numpy as np

# Creamos un dataframe
#    1  2  3
# a  1  8  3
# b  5  6  7
array = np.array([[1, 8, 3], [5, 6, 7]])
dataframe = pd.DataFrame(array, index=['a', 'b'], columns=list('123'))
print(dataframe)

# Suma por columnas
# 1     6
# 2    14
# 3    10
print(dataframe.sum())

# suma por filas
# a    12
# b    18
print(dataframe.sum(axis=1))

# Valor mínimo por columna
# 1    1
# 2    6
# 3    3
print(dataframe.min())

# Valor mínimo por fila
# a    1
# b    5
print(dataframe.min(axis=1))

# Valor máximo por columna
# 1    5
# 2    8
# 3    7
print(dataframe.max())

# Valor máximo por fila
# a    8
# b    7
print(dataframe.max(axis=1))

# Valor mínimo, pero indicando el índice
# 1    a
# 2    b
# 3    a
print(dataframe.idxmin())

# Valor máximo, pero indicando el índice
# 1    b
# 2    a
# 3    b
print(dataframe.idxmax())

# Estadistica
#              1         2         3
# count  2.000000  2.000000  2.000000 (Número de elementos)
# mean   3.000000  7.000000  5.000000 (Media)
# std    2.828427  1.414214  2.828427 (Desviación)
# min    1.000000  6.000000  3.000000 (Mínimo)
# 25%    2.000000  6.500000  4.000000 (25% del total)
# 50%    3.000000  7.000000  5.000000 (50% del total)
# 75%    4.000000  7.500000  6.000000 (75% del total)
# max    5.000000  8.000000  7.000000 (Máximo)
print(dataframe.describe())






