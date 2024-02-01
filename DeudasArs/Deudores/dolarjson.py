from urllib.request import urlopen
import json


with urlopen('https://www.dolarsi.com/api/api.php?type=valoresprincipales') as respuesta:
    cuerpo_respuesta = respuesta.read()


json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
dolar_compra = float(json_respuesta[1]['casa']['compra'].replace(".", "").replace(",", "."))
dolar_venta = float(json_respuesta[1]['casa']['venta'].replace(".", "").replace(",", "."))
dolar_blue = (dolar_venta + dolar_compra) / 2
print(dolar_blue)
