import sqlite3

conexion = sqlite3.connect("basededatos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER, nombre TEXT, precio INTEGER)")
conexion.commit()

lista_productos = [
(1,'Impresora',300),
(2,'Ratón',20),
(3,'Ordenador',600)
]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_productos)
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
for producto in productos:
	print(producto)

conexion.close()