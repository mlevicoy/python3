import pandas as pd
import numpy as np

lista_valores  = np.arange(9).reshape(3,3)
print(lista_valores)
lista_indices = list('abc')
print(lista_indices)

dataframe = pd.DataFrame(lista_valores, index=lista_indices)
print(dataframe)

# Pasamos el indice a mayuscula
nuevos_indices = dataframe.index.map(str.upper)
dataframe.index = nuevos_indices
print(dataframe)

# Otra forma es
dataframe = dataframe.rename(index=str.lower)
print(dataframe)

# Cambiamos el índice
nuevos_indices = {'a':'f', 'b':'g', 'c':'h'} 
print(dataframe.rename(index=nuevos_indices))



