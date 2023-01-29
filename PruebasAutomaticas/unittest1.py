def multiplicar(numero1, numero2):
	"""
	Función que multiplica dos número
	que ayudara a realizar la prueba automática
	"""
	return numero1 * numero2

# Llamamos a la función multiplicar
resultado = multiplicar(2,4)
# Imprimimos el resultado
print(resultado)

# Importamos la libreria unittest
import unittest
# Creamos la clase que realiza la prueba
class pruebas(unittest.TestCase):
	# Esta función debe ir
	def test(self):
		# Con el método assertEqual se llama a la 
		# función multiplicar, y verifica si el resultado
		# es correcto
		self.assertEqual(multiplicar(2,4),8)
		self.assertEqual(multiplicar(2,4),9)
# Llamamos a la clase
if __name__ == '__main__':
	unittest.main()