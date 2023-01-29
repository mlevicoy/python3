texto = "Hola, mi nombre es Antonio"

import re

resultado = re.search("mi.*es", texto)

if(resultado):
	print("Cadena encontrada: {}".format(resultado))
else:
	print("Cadena NO encontrada")