# 🌦️ GuardiánClima ITBA

Aplicación de consola en Python para consultar el clima en tiempo real,
guardar un historial global de consultas y obtener consejos de vestimenta
con inteligencia artificial.

## Instalación

pip install -r requirements.txt

## Configuración de API Keys

Crear un archivo llamado .env en la carpeta raíz del proyecto
con el siguiente contenido:

OPENWEATHER_API_KEY=tu_key_de_openweathermap
GEMINI_API_KEY=tu_key_de_gemini

Cómo obtener las keys:
- OpenWeatherMap: registrarse en https://openweathermap.org → API keys
- Gemini: registrarse en https://aistudio.google.com → Get API key

⚠️ Nunca compartas ni subas el archivo .env a GitHub.
   Está incluido en .gitignore para que no se suba automáticamente.

## Cómo correr la app

python main.py

## Estructura del proyecto

guardianclima/
├── main.py              Punto de entrada
├── menu_acceso.py       Menú de login y registro
├── menu_principal.py    Menú principal con las 6 opciones
├── auth.py              Sistema de usuarios y validación de contraseña
├── clima.py             API OpenWeatherMap y API Gemini
├── historial.py         Guardar y leer historial_global.csv
├── estadisticas.py      Estadísticas globales
├── datos/               Carpeta con los archivos CSV
├── .env                 API keys (no se sube a GitHub)
├── .gitignore
├── requirements.txt
└── README.md

## Equipo — Grupo 53

- Indiana Sasson
- Vicente Gallegos
- [Persona 3]
- [Persona 4]