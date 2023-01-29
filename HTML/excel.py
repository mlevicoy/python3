import pandas as pd
ficheroExcel = pd.ExcelFile('Libro1.xlsx')
misDatosExcel = ficheroExcel.parse('Hoja1')
print(misDatosExcel)

