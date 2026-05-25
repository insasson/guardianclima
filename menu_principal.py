# menu_principal.py
# Menú principal (post-login): las 6 opciones de la app
# Persona 1: Indiana

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
            # Llamar función clima.py
            consultar_clima(usuario)

        elif opcion == "2":
            # Llamar función historial.py
            ver_historial_personal(usuario)

        elif opcion == "3":
            # Llamar función estadisticas.py
            ver_estadisticas()

        elif opcion == "4":
            # Llamar función ia_gemini.py
            consejo_vestimenta(usuario)

        elif opcion == "5":
            mostrar_acerca_de()

        elif opcion == "6":
            print(f"\n👋 Cerraste sesión. ¡Hasta luego, {usuario}!")
            break

        else:
            print("\n⚠️  Opción inválida. Escribí un número del 1 al 6.")


# ─── FUNCIONES PROVISORIAS ───────────────────────────────────
# Estas funciones son placeholders — cuando los demás te pasen
# su código, reemplazás el contenido de cada una.

def consultar_clima(usuario):
    # ACA VA EL CODIGO DE PERSONA 3 (clima.py + historial.py)
    print("\n🌡️  [Módulo de clima — en desarrollo]")

def ver_historial_personal(usuario):
    # ACA VA EL CODIGO DE PERSONA 3 (historial personal)
    print("\n📋  [Historial personal — en desarrollo]")

def ver_estadisticas():
    # ACA VA EL CODIGO DE PERSONA 2 (estadisticas.py)
    print("\n📊  [Estadísticas — en desarrollo]")

def consejo_vestimenta(usuario):
    # ACA VA EL CODIGO DE PERSONA 3 (ia_gemini.py)
    print("\n🤖  [Consejo IA — en desarrollo]")

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

  Equipo: [nombre del grupo]
  Integrantes:
  • [Persona 1]
  • [Persona 2]
  • [Persona 3]
  • [Persona 4]
    """)