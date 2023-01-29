import moduloficherosdos

nombre_fichero = "ficherin.txt"

fichero = moduloficherosdos.Fichero(nombre_fichero)

texto = 'Esta es la primera fila del fichero.\nEsta es la segunda fila del fichero.'
fichero.grabar_fichero(texto)

texto = '\nEsta es la tercera fila del fichero'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)	