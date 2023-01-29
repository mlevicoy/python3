# Función que devuelve True si el
# número es positivo y False si es
# negativo
def positivo(numero):
	if(numero > 0):
		return True
	else:
		return False
# Generamos una lista de número
numeros = [4, -2, 8, -3, -5, -7, 1, 9]
# Filtramos llamando primero a la función 
# condicional enviandole la lista de números
filtro = filter(positivo, numeros)
# Generamos la lista filtrada
resultado = list(filtro)
# Mostramos la lista
print(resultado)

