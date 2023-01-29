def sumar(numero1, numero2):
	"""
	Esta es la documentación de esta función
	Recibe dos números como parámetros y devuelve la suma
	>>> sumar(4,3)
	7
	>>> sumar(5,4)
	9
	>>> sumar(1,3)
	7
	"""
	return numero1+numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()

