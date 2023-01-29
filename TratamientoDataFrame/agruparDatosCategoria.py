import pandas as pd
import numpy as np

precios = [42, 55, 48, 23, 5, 21, 88, 34, 26]
rango = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# [(40, 50], (50, 60], (40, 50], (20, 30], (0, 10], (20, 30], 
# (80, 90], (30, 40], (20, 30]]
# Categories (10, interval[int64]): [(0, 10] < (10, 20] < 
# (20, 30] < (30, 40] ... (60, 70] < (70, 80] < (80, 90] < 
# (90, 100]]
precios_con_rango = pd.cut(precios, rango)
print(precios_con_rango)

# Contamos cuantos precios hay en cada categoria
# (20, 30]     3
# (40, 50]     2
# (0, 10]      1
# (30, 40]     1
# (50, 60]     1
# (80, 90]     1
# (10, 20]     0
# (60, 70]     0
# (70, 80]     0
# (90, 100]    0
# dtype: int64
print(pd.value_counts(precios_con_rango))

