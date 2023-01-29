import sqlite3

conexion = sqlite3.connect("../basedatos1.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('Antonio','Perez','Gomez',35)")
conexion.commit()
conexion.close()