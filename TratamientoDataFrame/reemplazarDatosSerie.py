import pandas as pd

serie = pd.Series([1,2,3,4,5], index=list('abcde'))
print(serie)

# reeplazamos el 1 por el 6
print(serie.replace(1,6))

# reemplazamos por una serie
print(serie.replace({2:8, 3:9}))

