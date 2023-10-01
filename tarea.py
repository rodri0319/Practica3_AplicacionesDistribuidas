#Pedroza Velarde Luis Rodrigo Aplicaciones Distribuidas
#Practica 3
#01/10/2023
import requests
def obtener_informacion_ubicacion(geonames_username, lugar): #La funcion principal solo obtiene el nombre de usuario de geonames, y el lugar
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"
    try:
        response = requests.get(url)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            print(f"Ubicación obtenida de GeoNames: {ubicacion['name']}")
            #Este dato se obtuvo de GeoNames y se va a pasar a la peticion de OpenWather
            api_key = "afe6244129ebe84657cbc82062d08959" #api key openweathermap
            url2 = f"http://api.openweathermap.org/data/2.5/weather?q={ubicacion['name']}&appid={api_key}" 
            #en esta segunda url se manda el dato de la ubicacion obtenido de geonames y el api key
            response2 = requests.get(url2)
            data = response2.json()
            if "main" in data and "weather" in data:
                print(f"Información obtenida de OpenWeatherMap")
                temperatura = data["main"]["temp"]-273.15 #convertir de kelvin a celsius
                condiciones_climaticas=data["weather"][0]["description"]
                print(f"Temperatura en {ubicacion['name']}: {temperatura:.2f} °C") #imprime en consola
                print(f"Condiciones Climaticas en {ubicacion['name']}: {condiciones_climaticas}")
            else:
                print("Datos metereológicos no disponibles.")
        else:
            print("Ubicación no encontrada.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    geonames_username = "rodri" #Coloca tu usuario de geonames
    lugar = "Mexico City"  # Cambia esto a la ubicación que desees consultar
    obtener_informacion_ubicacion(geonames_username, lugar)