# menu_acceso.py
# Menú de acceso: opciones de login, registro y salir
# Persona 1: Indiana

from auth import iniciar_sesion, registrar_usuario

def mostrar_menu_acceso():
    while True:
        print("¿Qué querés hacer?")
        print("  1. Iniciar sesión")
        print("  2. Registrar nuevo usuario")
        print("  3. Salir")

        opcion = input("Elegí una opción (1-3): ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                # Login exitoso — va al menú principal
                from menu_principal import mostrar_menu_principal
                mostrar_menu_principal(usuario)

        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                # Registro exitoso — va directo al menú principal
                from menu_principal import mostrar_menu_principal
                mostrar_menu_principal(usuario)

        elif opcion == "3":
            print("Hasta luego 👋")
            break

        else:
            print("Opción inválida. Escribí 1, 2 o 3.")