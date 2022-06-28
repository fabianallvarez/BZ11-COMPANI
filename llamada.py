import requests

apikey = "10352093-DC90-44AE-A3C8-C01441A3AD7B"
cabeceras = {
    "X-CoinAPI-Key": apikey
}
api_url ="https://rest-sandbox.coinapi.io"
endpoint = "/v1/assets"

url = api_url + endpoint

respuesta =requests.get(url, headers = cabeceras)
codigo = respuesta.status_code

if codigo == 200:
    print("el resultado de la consulta es:")
    respuesta_json = respuesta.json()
    print(respuesta.text)

    for moneda in respuesta_json:
        if moneda["asset_id"].startswith("EUR"):
        print(moneda["asset_id"], moneda["name"])

else:
    print("La peticio de la api ha fallado")    
    print(f"codigo del error {codigo}")    
    print(f"razon del error{respuesta.reason}")    
    print(respuesta.text)    
