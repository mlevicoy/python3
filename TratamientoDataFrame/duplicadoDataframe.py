import pandas as pd

lista_valores = [[1,2], [1,2], [5,6], [5,8]]
lista_indices = list('nmop')
lista_columnas = ['valor1', 'valor2']
print(lista_valores)
print(lista_indices)
print(lista_columnas)
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

# Eliminamos los duplicados
print(dataframe.drop_duplicates())
# Eliminamos duplicados dentro de una columna
print(dataframe.drop_duplicates(['valor1']))






