# clima.py
# Conexión con la API de OpenWeatherMap y Google Gemini
# Persona 3: Matías

import requests
import os
from dotenv import load_dotenv
from historial import guardar_consulta

load_dotenv()

CLAVE_CLIMA = os.getenv("OPENWEATHER_API_KEY")
CLAVE_GEMINI = os.getenv("GEMINI_API_KEY")


def buscar_clima(ciudad, usuario):
    url = "https://api.openweathermap.org/data/2.5/weather"

    datos = {
        "q": ciudad,
        "appid": CLAVE_CLIMA,
        "units": "metric",
        "lang": "es"
    }

    # try/except no lo vimos en clase, lo investigamos.
    # Intenta hacer la consulta y si algo falla muestra un mensaje
    # en lugar de romper el programa.
    try:
        respuesta = requests.get(url, params=datos, timeout=10)
    except Exception as e:
        print(f"\n⚠️  No se pudo conectar con el servicio de clima: {e}")
        return None

    if respuesta.status_code == 401:
        print("\n⚠️  Error de autenticación. API key inválida.")
        return None
    elif respuesta.status_code == 404:
        print(f"\n⚠️  Ciudad '{ciudad}' no encontrada. Revisá el nombre e intentá de nuevo.")
        return None
    elif respuesta.status_code != 200:
        print(f"\n⚠️  Error al consultar el clima. Código: {respuesta.status_code}")
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

    guardar_consulta(usuario, info["name"], temp, clima, humedad, viento)

    return info["name"], temp, clima, humedad, viento


def recomendar_ropa(temp, clima, humedad, viento):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    pedido = (
        "Sos un asistente experto en moda y clima. "
        "Tu tarea es recomendar qué ropa usar según las condiciones climáticas actuales. "

        "Condiciones climáticas: "
        "Temperatura: " + str(temp) + "°C, "
        "Clima: " + clima + ", "
        "Humedad: " + str(humedad) + "%, "
        "Viento: " + str(viento) + " km/h. "

        "Antes de responder, considerá: ¿hace frío o calor? ¿Hay viento o lluvia? "
        "¿La humedad hace que se sienta más pesado el clima? "

        "Luego respondé con una recomendación práctica que incluya: "
        "1) Ropa superior (remera, buzo, campera, etc.), "
        "2) Ropa inferior (pantalón, short, falda, etc.), "
        "3) Calzado recomendado, "
        "4) Accesorios importantes (paraguas, gorro, lentes, protector solar). "

        "No menciones marcas. No uses listas con viñetas. "
        "Respondé en español, en tono amigable y en no más de 6 oraciones seguidas."
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

    # try/except no lo vimos en clase, lo investigamos.
    # Intenta hacer la consulta y si algo falla muestra un mensaje
    # en lugar de romper el programa.
    try:
        respuesta = requests.post(url, params={"key": CLAVE_GEMINI}, json=cuerpo, timeout=10)
    except Exception as e:
        print(f"\n⚠️  No se pudo obtener el consejo de la IA: {e}")
        return

    if respuesta.status_code == 200:
        info = respuesta.json()
        try:
            consejo = info["candidates"][0]["content"]["parts"][0]["text"]
            print("\n🤖 Recomendación de vestimenta:")
            print(consejo)
        except (KeyError, IndexError):
            print("\n⚠️  La IA no pudo generar un consejo en este momento.")
    else:
        print(f"\n⚠️  No se pudo obtener una recomendación. Código: {respuesta.status_code}")