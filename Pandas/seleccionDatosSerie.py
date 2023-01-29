# Importamos modulo pandas para las series y dataframes
import pandas as pd
# Importamos modulo numpy para los arrays
import numpy as np

# Creamos una serie
lista_Valores = np.arange(3)
lista_indices = ['i1', 'i2', 'i3']
serie = pd.Series(lista_Valores, index=lista_indices)
print(serie)

# Multiplicamos la serie por 2
serie = serie * 2 
print(serie)

# Accedemos al valor a través de su index
print(serie['i2'])

# Accedemos al valor a través de su posición
print(serie[1])

# Accedemos a varios valores de la serie
print(serie[0:2])

# Acceder a todos los valores de la serie
print(serie[:])

# Acceder al valor con una condición
print(serie[serie > 3])

# Cambiamos el valor
serie['i3'] = 6
print(serie)

