# Descripción de la API: Entrega el rango actual segun el ID del jugador de Rocket League
# Autor: Julián Alexis Cano Cruces
# Fecha de creación: 09/11/23

import http.client
import json

def make_api_request(player_id):
    conn = http.client.HTTPSConnection("rocket-league1.p.rapidapi.com")

    headers = {
        'User-Agent': "RapidAPI Playground",
        'Accept-Encoding': "identity",
        'X-RapidAPI-Key': "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3",
        'X-RapidAPI-Host': "rocket-league1.p.rapidapi.com"
    }

    conn.request("GET", f"/ranks/{player_id}", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def extract_info(data):
    try:
        json_data = json.loads(data)
        # Extracción de la información
    
        time = json_data['time']
        distance = json_data['distance']
        fuel_usage = json_data['fuel_usage']

        return time, distance, fuel_usage
    except json.JSONDecodeError:
        return None

def display_trip_information(time, distance, fuel_usage):
    print(f"Información del viaje:")
    print(f"Tiempo: {time}")
    print(f"Distancia: {distance}")
    print(f"Uso de combustible: {fuel_usage}")

def get_user_input():
    player_id = input("Ingresa el ID del jugador para obtener información de rango: ")
    return player_id

def main():
    while True:
        player_id = get_user_input()

        if player_id.lower() == "exit":
            print("Saliendo de la aplicación.")
            break

        api_data = make_api_request(player_id)
        if api_data:
            trip_info = extract_info(api_data)
            if trip_info:
                time, distance, fuel_usage = trip_info
                display_trip_information(time, distance, fuel_usage)
            else:
                print("Error: No se pudo extraer la información del viaje.")
        else:
            print("Error: No se pudo obtener datos de la API.")

if __name__ == "__main__":
    main()
