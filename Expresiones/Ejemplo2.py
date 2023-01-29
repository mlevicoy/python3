texto = """
El coche de luis es rojo,
el coche de Antonio es blanco,
y el coche de Maria es rojo
"""

import re

print(re.findall("coche.*rojo", texto))
