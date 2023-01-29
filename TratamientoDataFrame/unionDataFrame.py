
import pandas as pd

dataframe1 = pd.DataFrame({'c1':['1', '2', '3'], 'clave':['a', 'b', 'c']})
print(dataframe1)

dataframe2 = pd.DataFrame({'c2':['4', '5', '6'], 'clave':['c', 'b', 'e']})
print(dataframe2)

# Unimos los 2 dataframe
dataframe3 = pd.DataFrame.merge(dataframe1, dataframe2)
print(dataframe3)

# Unimos los 2 dataframe indicando la clave
dataframe3 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave')
print(dataframe3)

# Unimos los 2 dataframe indicando la clave y que mantenga el izquierdo, derecho y ambos
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='left')
print(dataframe4)
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='right')
print(dataframe4)
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='outer')
print(dataframe4)




