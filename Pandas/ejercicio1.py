# - Hay 3 clases "clase1", "clase2", "clase3".
# - Generar un número aleatorio de alumnos por clase.
#   Se va a utilizar np.random.randint(minimo, maximo, numero)
# - Crear serie de clases y alumnos
# - Utilizar el índice de la serie para saber el número de alumnnos de la clase2

import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero_aleatorio = 3 # Ya que son 3 clases
alumnos = np.random.randint(minimo, maximo, numero_aleatorio)
# Ejemplo, [34 24 28]
print(alumnos)

clases = ['Clase_1', 'Clase_2', 'Clase_3']

# Clase_1    22
# Clase_2    34
# Clase_3    14
serie = pd.Series(alumnos, index=clases)
print(serie)

print(serie['Clase_2'])





