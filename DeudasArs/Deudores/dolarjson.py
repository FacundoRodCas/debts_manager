from urllib.request import urlopen, Request
import json


req = Request('https://api.bluelytics.com.ar/v2/latest', headers={'User-Agent': 'Google Chrome/12.0'})
cuerpo_respuesta = urlopen(req).read()

json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
dolar_blue = float(json_respuesta['blue']['value_avg'])

