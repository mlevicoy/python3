import re

def buscar(texto, palabra_a_buscar):
	resultado = re.search(palabra_a_buscar, texto)
	return resultado

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = "es"

resultado = buscar(texto, palabra_a_buscar)

if(resultado):
	posicion_inicial = resultado.start()
	posicion_final = resultado.end()
	print("Frase encontrada desde la posición {} hasta la {}".format(posicion_inicial, posicion_final))
else:
	print("Frase no encontrada")