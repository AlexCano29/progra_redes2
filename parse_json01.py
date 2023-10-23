'''

Nombre: Julian Alexis Cano Cruces
Fecha: 23/10/12
Ejercicio: Obtener Valores

'''



import urllib.parse
import requests

#Se generan las variables 
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San MIguel de Allende"
key = "uYM8nZJ7wjjjjmauf4aqlBhPaoJoXt6N"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) #Genera la URL en base a las variables que se le dan
json_data = requests.get(url).json()

print("JSON ID:",(json_data ['route']['sessionId']))             #Imprime el Session ID
print("Distance:",(json_data ['route']['distance']))             #Imprime la distancia
print("Time:",(json_data ['route']['time']))                     #Imprime el tiempo
print("Formatted Time :",(json_data ['route']['formattedTime'])) #Imprime el Formatted Time




'''print(json_data)
print(url)'''   #Entrega la URL 
