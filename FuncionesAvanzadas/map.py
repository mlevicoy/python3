# Función multiplicar un número por 2
def multiplicar(numero):
	return numero * 2
# Llamamos a la función
resultado = multiplicar(2)
# Mostramos el resultado
print(resultado)
# Generamos una lista
numeros = [2, 4, 6]
# Usamos la función map, envianole la función y la 
# lista a multiplicar, # devolvera un objeto en 
# este caso llamado mapeo
mapeo = map(multiplicar, numeros)
# Convertimos el objeto en una lista
resultadoMapeo = list(mapeo)
# Mostramos la lista
print(resultadoMapeo)

# Se puede hacer en la misma línea
lista_resultado = list(map(multiplicar, numeros))
print(lista_resultado)

# Se puede usar una función lambda
lista_resultado_dos = list(map(lambda numero: numero * 2, numeros))
print(lista_resultado_dos)