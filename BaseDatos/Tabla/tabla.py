import sqlite3

conexion = sqlite3.connect("basedatos1.db")

conexion.cursor()

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

conexion.commit()

conexion.close()