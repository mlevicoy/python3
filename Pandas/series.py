import pandas as pd

# se genera una lista de valores indexados
# 0    3
# 1    5
# 2    7
# 3    9
# dtype: int64
serie1 = pd.Series([3, 5, 7, 9])
print(serie1)
# Ejemplo si quisiera acceder al número 7
print(serie1[2])

# Se puede generar la indexación
asignaturas = ['matematicas', 'historia', 'fisica', 'literatura']
notas = [8, 6, 9, 7]
serie_notas_daniel = pd.Series(notas, index=asignaturas)
print(serie_notas_daniel)
print(serie_notas_daniel['fisica'])

# Se pueden hacer condiciones dentro e la serie
print(serie_notas_daniel[serie_notas_daniel >= 8])

# Se le puede poner un nombre a la serie
serie_notas_daniel.name = 'Notas de Daniel'
print(serie_notas_daniel)

# Se le puede poner un nombre a los indices
# Asignaturas de Daniel
# matematicas    8
# historia       6
# fisica         9
# literatura     7
# Name: Notas de Daniel, dtype: int64
serie_notas_daniel.index.name = 'Asignaturas de Daniel'
print(serie_notas_daniel)

# Convertir la serie en un diccionario
# {'matematicas': 8, 'historia': 6, 'fisica': 9, 'literatura': 7}
diccionario = serie_notas_daniel.to_dict()
print(diccionario)

# Convertir un diccionario en una serie
serie = pd.Series(diccionario)
print(serie)

# Otra serie, para ana
asignaturas = ['matematicas', 'historia', 'fisica', 'literatura']
notas_ana = [7, 8, 5, 9]
serie_notas_ana = pd.Series(notas_ana, index=asignaturas)
print(serie_notas_ana)

# Serie con la media de la clase
# matematicas    7.5
# historia       7.0
# fisica         7.0
# literatura     8.0
# dtype: float64
serie_notas_clase = (serie_notas_daniel + serie_notas_ana) / 2
print(serie_notas_clase)
