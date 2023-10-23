'''

Nombre: Julian Alexis Cano Cruces
Fecha: 23/10/12
Ejercicio: Obtener Valores

'''



import urllib.parse
import requests


while True:
    orig = input("Origèn: ")
    if orig == "quit" or orig == "q": #Condicion para orig
        print("Hasta Luego")
        break

    dest = input("Destino: ")   
    if orig == "quit" or orig == "q": #Condicion para orig
        print("Hasta Luego") 
        break
    
    #Condicion para Dest
    
    
    #Se generan las variables 
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "uYM8nZJ7wjjjjmauf4aqlBhPaoJoXt6N"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) #Genera la URL en base a las variables que se le dan
    json_data = requests.get(url).json()


    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

    if json_status != 0:
        print("API Status: " + str(json_status) + " = A failure route call.\n")


    
    #Codificar para manejar el error distinto a Cero