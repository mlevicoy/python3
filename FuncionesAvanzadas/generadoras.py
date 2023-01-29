# range es una función generadora
# tambien puede ser range(11)
range(0,11)
for numero in range(0,11):
	print(numero)
# Crearemos una función generadora personalizada
def pares(maximo):
	for numero in range(maximo):
		if(numero % 2 == 0):
			# Yiend es un objeto que devuelve un
			# número a la vez
			yield(numero)
# Probamos la función pares
maximo = 11
for numero in pares(maximo):
	print(numero)