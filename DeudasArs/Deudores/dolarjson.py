from urllib.request import urlopen
import json


with urlopen('https://dolarapi.com/v1/dolares/oficial') as respuesta:
    cuerpo_respuesta = respuesta.read()


json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
dolar_compra = float(json_respuesta['compra'])
dolar_venta = float(json_respuesta['venta'])
dolar_oficial = (dolar_venta + dolar_compra) / 2
print(dolar_oficial)
