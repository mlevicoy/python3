import sqlite3
conexion = sqlite3.connect("../basedatos1.db")
cursor = conexion.cursor()
cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Luis'")
conexion.commit()
conexion.close()