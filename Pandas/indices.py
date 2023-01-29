import pandas as pd

# Generamos una serie
lista_valores = [1, 2, 3]
lista_indices = ['a', 'b', 'c']
serie = pd.Series(lista_valores, index=lista_indices)
# Mostramos la serie
print(serie)
# Mostramos los indices
print(serie.index)
# Mostramos el primer indice
# Los indices no se pueden cambiar
print(serie.index[0])

# Indices a través de un dataframe
lista_valores = [[6,7,8], [8,9,5], [6,9,7]]
lista_indices = ['matematicas', 'historia', 'fisica']
lista_nombres = ['Antonio', 'Maria', 'Pedro']
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_nombres)
# Mostramos el dataframe
print(dataframe)
# Mostramos los indices
print(dataframe.index)
# Mostramos un elemento del indice
print(dataframe.index[2])

