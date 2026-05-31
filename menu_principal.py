# menu_principal.py
# Menú principal (post-login): las 6 opciones de la app
# Persona 1: Indiana


def consultar_clima(usuario):
    from clima import buscar_clima
    ciudad = input("\n¿Qué ciudad querés consultar? ").strip()
    buscar_clima(ciudad, usuario)


def ver_historial_personal(usuario):
    from historial import ver_historial_personal as historial_personal
    ciudad = input("\n¿Para qué ciudad querés ver el historial? ").strip()
    historial_personal(usuario, ciudad)


def ver_estadisticas():
    from estadisticas import mostrar_estadisticas_globales
    mostrar_estadisticas_globales()


def consejo_vestimenta(usuario):
    from clima import buscar_clima, recomendar_ropa
    ciudad = input("\n¿Para qué ciudad querés el consejo? ").strip()
    resultado = buscar_clima(ciudad, usuario)
    if resultado is not None:
        recomendar_ropa(resultado[1], resultado[2], resultado[3], resultado[4])


def mostrar_acerca_de():
    print("\n" + "=" * 50)
    print("   Acerca de GuardiánClima ITBA")
    print("=" * 50)
    print("""
  Aplicación desarrollada como challenge final
  del ingreso a ITBA — 2026.
  Equipo: Grupo 53
  Integrantes: Indiana Sasson, Vicente Gallegos, Matías Etchegaray

  ── FUNCIONALIDADES ──────────────────────────────

  1. Consultar clima actual
     Conecta con la API de OpenWeatherMap para obtener
     temperatura, humedad, viento y condición climática
     en tiempo real. Cada consulta se guarda en historial_global.csv.

  2. Ver historial personal
     Filtra el historial global por usuario y ciudad,
     mostrando todas las consultas anteriores ordenadas por fecha.

  3. Estadísticas globales
     Calcula la ciudad más consultada, el total de consultas
     y la temperatura promedio de todos los usuarios.

  4. Consejo IA
     Usa la API de Google Gemini para generar un consejo
     personalizado de vestimenta según los datos climáticos actuales.

  5. Sistema de usuarios
     El registro verifica duplicados y valida que la contraseña
     cumpla criterios de seguridad: longitud mínima, sin secuencias
     obvias, sin repeticiones y sin sustituciones predecibles.

    AVISO DE SEGURIDAD: El almacenamiento de contraseñas en este proyecto es una
    simulación educativa. Las contraseñas se guardan en texto plano
    en usuarios_simulados.csv, lo cual NO es seguro para aplicaciones
    reales. En un sistema real se usaría hashing (por ejemplo SHA-256),
    de forma que nunca se guarde la contraseña original sino una
    representación irreversible de la misma.

    """)

def mostrar_menu_principal(usuario):
    while True:
        print(f"\n{'=' * 50}")
        print(f"   GuardiánClima — Hola, {usuario}!")
        print(f"{'=' * 50}")
        print("  1. Consultar clima actual")
        print("  2. Ver mi historial personal")
        print("  3. Estadísticas globales")
        print("  4. Consejo IA: ¿cómo me visto hoy?")
        print("  5. Acerca de...")
        print("  6. Cerrar sesión")

        opcion = input("\nElegí una opción (1-6): ").strip()

        if opcion == "1":
            consultar_clima(usuario)

        elif opcion == "2":
            ver_historial_personal(usuario)

        elif opcion == "3":
            ver_estadisticas()

        elif opcion == "4":
            consejo_vestimenta(usuario)

        elif opcion == "5":
            mostrar_acerca_de()

        elif opcion == "6":
            print(f"Cerraste sesión. ¡Nos vemos, {usuario}!")
            break

        else:
            print("opción inválida. Escribí un número del 1 al 6.")