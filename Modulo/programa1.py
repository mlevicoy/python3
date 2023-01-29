import modulo1

coche1 = modulo1.Coche('Opel', 'Rojo', 'Gasolina', '1.6')
coche1.mostrar_caracteristicas()

nota1 = 5.0
nota2 = 6.1
nota3 = 4.5
promedioNotas = modulo1.media(nota1, nota2, nota3)
print("El promedio entre las nota1 = {}, nota2 = {} y nota3 = {} es {}".format(nota1, nota2, nota3, promedioNotas))