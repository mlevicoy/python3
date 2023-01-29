# Dado el fichero excel en varios formatos.
# Copiar los datos al portapapeles.
import pandas as pd
# Crear un dataframe "datos" con esos datos copiados.
datos = pd.read_clipboard()
# Mostrar por pantalla, todos los datos del dataframe.
print(datos)
# Mostrar por pantalla, todos los nombres de columnas del dataframe.
print(datos.columns)
# Mostrar por pantalla, la primera fila del dataframe.
print(datos.loc[0])
# Mostrar por pantalla, la primera columna del dataframe.
print(datos['Continente'])
# Mostrar por pantalla, todas las filas pero solo las columnas "Continente" y "Población".
print(datos[['Continente', 'Población']])
# Mostrar por pantalla, las primeras 3 filas del dataframe.
print(datos.head(3))
# Mostrar por pantalla, las 2 últimas filas del dataframe.
print(datos.tail(2))

