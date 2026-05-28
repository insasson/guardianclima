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
    print("   📖  Acerca de GuardiánClima ITBA")
    print("=" * 50)
    print("""
  Aplicación desarrollada como challenge final
  del ingreso a ITBA — 2026.

  Funcionalidades:
  • Consulta de clima en tiempo real (OpenWeatherMap)
  • Historial global de consultas en CSV
  • Estadísticas globales de uso
  • Consejos de vestimenta con IA (Google Gemini)
  • Sistema de login con validación de contraseña

  ⚠️  Aviso: el sistema de usuarios es una simulación
  educativa. En una app real, las contraseñas se
  almacenan con hashing (ej: SHA-256), nunca en
  texto plano.

  Equipo: [53]
  Integrantes:
  • [Persona 1]
  • [Persona 2]
  • [Persona 3]
  • [Persona 4]
    """)


def mostrar_menu_principal(usuario):
    while True:
        print(f"\n{'=' * 50}")
        print(f"   🌦️  GuardiánClima — Hola, {usuario}!")
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
            print(f"\n👋 Cerraste sesión. ¡Hasta luego, {usuario}!")
            break

        else:
            print("\n⚠️  Opción inválida. Escribí un número del 1 al 6.")