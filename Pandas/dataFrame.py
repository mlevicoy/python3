import pandas as pd

# Extraemos información de una web
import  webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
webbrowser.open(website)

# Copiamos lo del portapapeles (lo que se copio de la web)
dataframe_nba = pd.read_clipboard()
print(dataframe_nba)

# Mostramos el nombre de las columnas
print(dataframe_nba.columns)

# Mostrar una sola columna, con el dataframe indexado
print(dataframe_nba['Campeón del Oeste'])

# Mostrar un datagrame por la indexación
print(dataframe_nba.loc[5])

# Mostrar los primeros elementos
print(dataframe_nba.head())
# Puede ser con el valor de los elementos a mostrar
print(dataframe_nba.head(2))

# Dataframe desde un diccionario
lista_asignaturas = ['matematicas', 'historia', 'fisica']
lista_notas = [8, 7, 9]
diccionario = {'Asignaturas':lista_asignaturas, 'Notas':lista_notas}
print(diccionario)
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)