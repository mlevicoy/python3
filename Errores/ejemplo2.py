def operaciones(numero1, numero2, numero3):
	try:
		resultado = numero1 / (numero2-numero3)
		print(resultado)
	except ZeroDivisionError:
		print("Error, no se puede dividir por cero. Los últimos dos número debe ser diferentes")
	else:
		print("El resultado obtenido es correcto.")
	finally:
		print("Ejercicio finalizado.")

numero1 = 5
numero2 = 3
numero3 = 3
resultado = operaciones(numero1,numero2,numero3)
print(resultado)