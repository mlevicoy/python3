from datetime import datetime

fechayhora = datetime.now()

print(fechayhora)

ano = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print("La hora es {}:{}:{}".format(hora,minutos,segundos))
print("La fecha es {}/{}/{}".format(dia,mes,ano))