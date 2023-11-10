
# Descripción de la API: Detector idiomas segun la frase que se le de
# Autor: Julián Alexis Cano Cruces
# Fecha de creación: 09/11/23

import http.client
import json
from urllib.parse import quote

def get_translation(text):
    conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

    payload = f"q={quote(text)}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'Accept-Encoding': "application/gzip",
        'X-RapidAPI-Key': "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3",
        'X-RapidAPI-Host': "google-translate1.p.rapidapi.com"
    }

    conn.request("POST", "/language/translate/v2/detect", payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    
    if res.status == 200:
        return json.loads(data)
    else:
        return {"error": f"Request failed with status code {res.status}"}

def user_input():
    text = input("Introduce el texto para detectar el idioma: ")
    return text

def output_translation(translation):
    if "error" in translation:
        print("Error:", translation["error"])
    else:
        print("Idioma Detectado:", translation["data"]["detections"][0][0]["language"])

def main():
    text = user_input()
    translation = get_translation(text)
    output_translation(translation)

if __name__ == "__main__":
    main()
