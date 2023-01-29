import pandas as pd
import numpy as np

# Generamos 1 array
array1 = np.arange(9).reshape(3,3)
print(array1)
# Concatenamos el array
array_concatenado = np.concatenate([array1, array1])
print(array_concatenado)
# Concatenamos el array por columna
array_concatenado2 = np.concatenate([array1, array1], axis=1)
print(array_concatenado2)

# Generamos 2 series
serie1 = pd.Series([1,2,3], index=['a', 'b', 'c'])
serie2 = pd.Series([4,5,6], index=['d', 'e', 'f'])
# Concatenamos la serie
serie_concatenada = pd.concat([serie1, serie2])
print(serie_concatenada)
# concatenamos colocandole una llave extra
serie_concatenadaLlave = pd.concat([serie1, serie2], keys=['Serie_1', 'Serie_2'])
print(serie_concatenadaLlave)


# Generamos 2 dataframe
dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=['a', 'b', 'c'])
dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=['a', 'b', 'c'])
print(dataframe1)
print(dataframe2)
# Concatenamos los dataframe
dataframeConcatenado = pd.concat([dataframe1, dataframe2])
print(dataframeConcatenado)
# Reorganizamos el índice para que se muestre correctamente
dataframeConcatenadoReorg = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframeConcatenadoReorg)







