try:
	numero1 = 5
	numero2 = 0
	division = numero1 / numero2
	print(division)
except ZeroDivisionError:
	print("Error, no se puede dividir por cero.")
except:
	print("Ha habido un error")
else:
	print("La división funciono correctamente.")
finally:
	print("Esta prueba del try se ha acabado")