import pandas as pd
import numpy as np
# - Crearemos una lista de 50 valores aleatorios enteros entre los 
# valores 0 y 100.
lista_valores = np.random.randint(0,100,50)
print(lista_valores)
# - Convertiremos esta lista en un dataframe con 5 filas y 10 columnas
lista_valores.resize(5,10)
dataframe = pd.DataFrame(lista_valores)
print(dataframe)
# - Filtraremos los datos del dataframe para visualizar solo los valores
# que sean mayores de 50.
print(dataframe[dataframe > 50])

