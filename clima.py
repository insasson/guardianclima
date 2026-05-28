# clima.py
# Conexión con la API de OpenWeatherMap
# Persona 3: Matías

import requests
import os
from dotenv import load_dotenv
from historial import guardar_consulta

load_dotenv()

CLAVE_CLIMA = os.getenv("OPENWEATHER_API_KEY")
CLAVE_GEMINI = os.getenv("GEMINI_API_KEY")
print("KEY CLIMA:", CLAVE_CLIMA)
print("KEY GEMINI:", CLAVE_GEMINI)


def buscar_clima(ciudad, usuario):
    url = "https://api.openweathermap.org/data/2.5/weather"

    datos = {
        "q": ciudad,
        "appid": CLAVE_CLIMA,
        "units": "metric",
        "lang": "es"
    }

    respuesta = requests.get(url, params=datos)

    if respuesta.status_code != 200:
        print("\n⚠️  No se pudo encontrar esa ciudad. Revisá el nombre e intentá de nuevo.")
        return None

    info = respuesta.json()

    temp = info["main"]["temp"]
    clima = info["weather"][0]["description"]
    humedad = info["main"]["humidity"]
    viento = round(info["wind"]["speed"] * 3.6, 1)

    print("\n" + "=" * 50)
    print("          CLIMA ACTUAL")
    print("=" * 50)
    print(f"   Ciudad      : {info['name']}")
    print(f"   Temperatura : {temp}°C")
    print(f"   Clima       : {clima}")
    print(f"   Humedad     : {humedad}%")
    print(f"   Viento      : {viento} km/h")
    print("=" * 50)

    # Guardar en el historial global
    guardar_consulta(usuario, info["name"], temp, clima, humedad, viento)

    return info["name"], temp, clima, humedad, viento


def recomendar_ropa(temp, clima, humedad, viento):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    pedido = (
        "Hace " + str(temp) + " grados, el clima es " + clima +
        ", hay " + str(humedad) + "% de humedad y el viento es de " +
        str(viento) + " km/h. "
        "Decime brevemente qué ropa conviene usar para salir."
    )

    cuerpo = {
        "contents": [
            {
                "parts": [
                    {"text": pedido}
                ]
            }
        ]
    }

    respuesta = requests.post(url, params={"key": CLAVE_GEMINI}, json=cuerpo)

    if respuesta.status_code == 200:
        info = respuesta.json()
        consejo = info["candidates"][0]["content"]["parts"][0]["text"]
        print("\n🤖 Recomendación de vestimenta:")
        print(consejo)
    else:
        print("\n⚠️  No se pudo obtener una recomendación.")
        print("Código de error:", respuesta.status_code)