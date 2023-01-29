import moduloficheros

fichero = moduloficheros.Fichero()

fichero.grabar_fichero("ficheroPrograma1.txt")

datos = "Información para el fichero."

fichero.incluir_fichero("ficheroPrograma1.txt", datos)

fichero.leer_fichero("ficheroPrograma1.txt")