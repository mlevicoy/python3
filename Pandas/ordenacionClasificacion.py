import pandas as pd
import numpy as np

# Lista de valores
lista_valores = range(4)
print(lista_valores)
# Lista de indices
lista_indices = list('CABD')
print(lista_indices)
# Creamos la serie
serie = pd.Series(lista_valores, index=lista_indices)
print(serie)

# Ordenamos alfabeticamente los indices
print(serie.sort_index())

# Ordenamos por los valores
print(serie.sort_values())

# Generamos un ranking
print(serie.rank())

# Creamos una serie de 10 números aleatorios
# 0    0.677689
# 1    0.361784
# 2    0.052587
# 3    0.901053
# 4    0.621043
# 5    0.221795
# 6    0.170423
# 7    0.629015
# 8    0.193603
# 9    0.788448
# dtype: float64
serie2 = pd.Series(np.random.rand(10))
print(serie2)

# Generamos un ranking de la serie2
print(serie2.rank())

# Ordenamos la serie 2 por valores
print(serie2.sort_values())

