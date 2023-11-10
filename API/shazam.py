# Descripción de la API: Entrega canciones de un artista segun los parametros otorgados
# Autor: Julián Alexis Cano Cruces
# Fecha de creación: 09/11/23 

import http.client
import json

def hacer_solicitud_api(artist_id, idioma='es-ES', desde_fecha='2022-12-31', limite=50, offset=0):
    conn = http.client.HTTPSConnection("shazam.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3",
        'X-RapidAPI-Host': "shazam.p.rapidapi.com"
    }

    endpoint = f"/shazam-events/list?artistId={artist_id}&l={idioma}&from={desde_fecha}&limit={limite}&offset={offset}"

    conn.request("GET", endpoint, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    if response.status == 200:
        return json.loads(data)
    else:
        return None

def entrada_usuario():
    artist_id = input("Ingresa el ID del artista: ")
    idioma = input("Ingresa el idioma (por ejemplo, es-ES): ")
    desde_fecha = input("Ingresa la fecha desde la cual buscar (formato: AAAA-MM-DD): ")
    limite = input("Ingresa el límite de eventos a mostrar: ")
    offset = input("Ingresa el desplazamiento (offset): ")
    return artist_id, idioma, desde_fecha, int(limite), int(offset)

def mostrar_instrucciones(data):
    if data and 'events' in data:
        print("Instrucciones:")
        for evento in data['events']:
            print(evento)  # Imprime la información específica del evento
    else:
        print("No se encontraron eventos para este artista o con los parámetros indicados.")

def principal():
    artist_id_usuario, idioma_usuario, fecha_usuario, limite_usuario, offset_usuario = entrada_usuario()
    datos_api = hacer_solicitud_api(artist_id_usuario, idioma_usuario, fecha_usuario, limite_usuario, offset_usuario)
    mostrar_instrucciones(datos_api)

if __name__ == "__main__":
    principal()




