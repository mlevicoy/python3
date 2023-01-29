producto1 = {"nombre":"silla", "color":"blanco", "precio":80}

import json

#Genera el JSON
estructura_json = json.dumps(producto1)

print(estructura_json)

#Pasa a JSON a una estructura normal
productos2 = json.loads(estructura_json)

print(productos2)