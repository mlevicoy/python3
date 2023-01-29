import sqlite3
conexion = sqlite3.connect("../basedatos1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS WHERE edad > 40")
personas_seleccionadas = cursor.fetchall()
for persona in personas_seleccionadas:
	print(persona)
conexion.close()