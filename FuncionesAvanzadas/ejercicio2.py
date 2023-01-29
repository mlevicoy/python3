numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def funcion_pares(numero):
	if(numero % 2 == 0):
		return True
	else:
		return False

pares = list(filter(funcion_pares, numeros))
print(pares)
