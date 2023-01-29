import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'
dataframe = pd.io.html.read_html(url)
print(dataframe)

# Copiamos el dataframe
dataframe_futbol = dataframe[0]
print(dataframe_futbol)

# Mostramos una sola fila
print(dataframe_futbol.loc[0])

# Pasamos una fila a diccionario
print(dict(dataframe_futbol.loc[0]))

# Modificamos las columnas por los del diccionario.
diccionario = {'0':'Date', '1':'Champion', '2':'Result', '3':'Runner-Up', '4':'Stadium', '5':'Viewers', '6':'Location', '7':'Note'}
print(diccionario)
dataframe_futbol = dataframe_futbol.rename(columns=diccionario)
print(dataframe_futbol)

# Eliminamos una fila
dataframe_futbol = dataframe_futbol.drop(0)

 # Eliminamos una columna
dataframe_futbol = dataframe_futbol.drop('Notas', axis=1)
print(dataframe_futbol)



