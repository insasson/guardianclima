# Grupo 53 - GuardiánClima ITBA 

## Intrucciones para configurar el entorno
pip install -r requirements.txt

También necesitás crear un archivo ".env" en la carpeta raíz del proyecto con tus API keys:
- OPENWEATHER_API_KEY=tu_key_de_openweathermap
- GEMINI_API_KEY=tu_key_de_gemini
(más detallado en el apartado "Configuración de API Keys")

## Cómo ejecutar la aplicación
python main.py

## Flujo de menus
#### Menú de acceso
Este menú contiene 3 opciones: 

1: Iniciar sesión -- > Esta función te permite ingresar tu usuario y contraseña. Verifica si lo ingresado pertenece al archivo "usuarios_simulados.csv" y si la información es correcta. Tenés 3 intentos para escribir correctamente la contraseña antes de que te devuelva automáticamente al menú de acceso. Si los datos son correctos, se pasa al menú principal.

2: Registrar un nuevo usuario -- > En esta función te permite crear un nombre de usuario (si no está en uso) y una contraseña. La contraseña debe cumplir ciertos requisitos, vistos en el módulo de ciberseguridad, para que la contraseña del nuevo usuario sea robusta. Algunos de los requisitos son: longitud mínima de 12 caracteres, sin secuencias obvias como "123" o "abc", sin repeticiones de caracteres, sin sustituciones predecibles y sin tu nombre de usuario.
Si algún criterio no se cumple, te indica cuál y te permite volver a intentar. 
Al registrarse correctamente, se pasa al menú principal.

3: Salir -- > Cierra la aplicación.

#### Menú Principal
Este menú cuenta con 6 opciones:

1: Consultar clima actual -- > Al ingresar la opción 1, el programa te pide ingresar el nombre de la ciudad de la cual quieras saber el clima. La aplicación consulta la API de OpenWeatherMap y muestra la temperatura, la condición climática, la humedad y la velocidad del viento. La consulta se guarda automáticamente en el historial global.

2: Ver mi historial personal -- > Al ingresar la opción 2, el programa te pide ingresar el nombre de una ciudad. La aplicación muestra todas tus consultas anteriores para esa ciudad, ordenadas de la más reciente a la más antigua.

3: Estadísticas globales -- > Al ingresar la opción 3, el programa muestra tres métricas calculadas sobre el historial de todos los usuarios: la ciudad más consultada, el total de consultas realizadas y la temperatura promedio global.

4: Consejo IA: ¿cómo me visto hoy? -- > Al ingresar la opción 4, el programa te pide ingresar una ciudad. Luego, la aplicación consulta el clima y envía los datos a Google Gemini, que genera un consejo práctico y personalizado de vestimenta según las condiciones climáticas del momento.

5: Acerca de..  -- > Al ingresar la opción 5, el programa muestra una descripción completa de la aplicación, cómo funciona cada módulo internamente, el equipo de desarrollo y un aviso sobre la naturaleza simulada del sistema de contraseñas.

6: Cerrar sesión -- > Al ingresar la opción 6, se cierra sesión y te devuelve al menú de acceso.

## Configuración de API Keys
Crear un archivo llamado .env en la carpeta raíz del proyecto
con el siguiente contenido:

OPENWEATHER_API_KEY=tu_key_de_openweathermap
GEMINI_API_KEY=tu_key_de_gemini

Cómo obtener las keys:
1: En OpenWeatherMap:
- Registrarse en https://openweathermap.org
- Iniciar sesión en la plataforma.
- Acceder a la sección API Keys desde el panel de usuario.
- Generar o copiar una clave existente.
- Reemplazar tu_key_de_openweathermap por la clave obtenida.
  
2: En Gemini:
- Registrarse o iniciar sesión en https://aistudio.google.com
- Seleccionar la opción Get API Key.
- Generar una nueva clave de acceso.
- Reemplazar tu_key_de_gemini por la clave obtenida.

A tener en cuenta: el archivo ".env" hay que incluirlo en el archivo .gitignore para que no se suba a github por temas de seguridad.

   
