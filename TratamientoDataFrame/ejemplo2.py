import pandas as pd
import numpy as np

# Crear 2 array con 9 números aleatorios enteros entre los valores 0 y 100
array1 = np.random.randint(0,100,9)
array2 = np.random.randint(0,100,9)
# Cambiar el formato de los arrays en una estructura de 3 filas x 3 columnas
array1 = array1.reshape(3,3)
array2 = array2.reshape(3,3)
# Crear 2 fataframe con esos arrays
dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)
# Concatenar esos 2 dataframes
dataframe_concatenado = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframe_concatenado)

