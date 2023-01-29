# Obtener la tabla de paises de la página https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses
# Limpiar los datos lo necesario para que los nombres de las columnas sean correctos.

import pandas as pd

excel = pd.ExcelFile('poblacion.xlsx')
dataframe = excel.parse('Hoja 1')
print(dataframe)
print(dataframe['Ciudad más poblada'][3])

csv = pd.read_csv('poblacion.csv')
print(csv)
print(csv['Ciudad más poblada'][1])





