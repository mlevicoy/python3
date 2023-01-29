class Fichero:
	#def __init__(self, nombre_fichero, texto_agregar):
	#	self.nombre_fichero = nombre_fichero
	#	self.texto_agregar = texto_agregar
	def leer_fichero(self, nombre_fichero):
		self.nombre_fichero = nombre_fichero
		fichero = open(self.nombre_fichero, "rt")
		datos_fichero = fichero.read()
		print(datos_fichero)

	def grabar_fichero(self, nombre_fichero):
		self.nombre_fichero = nombre_fichero
		fichero = open(self.nombre_fichero, "wt")
		fichero.write("")
		fichero.close()

	def incluir_fichero(self, nombre_fichero, texto_agregar):
		self.nombre_fichero = nombre_fichero
		self.texto_agregar = texto_agregar
		fichero = open(self.nombre_fichero, "at")
		cadena_incluir = "\n" + self.texto_agregar
		fichero.write(cadena_incluir)
		fichero.close()