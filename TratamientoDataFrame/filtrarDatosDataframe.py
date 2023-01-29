import pandas as pd
import numpy as np

# Generamos una lista de 10 filas x 3 columnas
lista_valores = np.random.rand(10,3)
print(lista_valores)

# DataFrame
dataframe = pd.DataFrame(lista_valores)
print(dataframe)

# Columna 0
columna = dataframe[0]
print(columna)
print(columna[columna > 0.40])



