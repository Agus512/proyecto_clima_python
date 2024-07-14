import requests


#----------INICIO_CLIMA----------

OWM_API_KEY = #PONER URL DE API OPENWEATHER

urls = {
    "Berazategui": f"http://api.openweathermap.org/data/2.5/weather?q=Berazategui,AR&appid={OWM_API_KEY}&units=metric&lang=es",
    "Montevideo": f"http://api.openweathermap.org/data/2.5/weather?q=Montevideo,UY&appid={OWM_API_KEY}&units=metric&lang=es",
    "Mar del Plata": f"http://api.openweathermap.org/data/2.5/weather?q=Mar del Plata,AR&appid={OWM_API_KEY}&units=metric&lang=es"
}

def obtener_clima(ciudad):
    url = urls.get(ciudad)
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura = data['main']['temp']
            descripcion = data['weather'][0]['description']
            return f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C."
        else:
            return f"No se pudo obtener el clima de {ciudad}."
    else:
        return f"No se encontró la información para {ciudad}."

# Menú para seleccionar la ciudad
print("Elige el lugar donde deseas ver el clima:")
print("1. Berazategui")
print("2. Montevideo, Uruguay")
print("3. Mar del Plata")
opcion = int(input("Opción: "))

# Mostrar_el_clima_según_la_opción
if opcion == 1:
    print(obtener_clima("Berazategui"))
elif opcion == 2:
    print(obtener_clima("Montevideo"))
elif opcion == 3:
    print(obtener_clima("Mar del Plata"))
else:
    print("Opción no válida.")



#----------FIN CLIMA----------