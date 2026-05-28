# auth.py
# Registro e inicio de sesión con validación de contraseña
# Persona 4: x

import csv
import os
import re

ARCHIVO_USUARIOS = "datos/usuarios_simulados.csv"
ENCABEZADOS = ["username", "password_simulada"]

# Crear la carpeta datos/ si no existe
os.makedirs("datos", exist_ok=True)


def validar_contrasena(contrasena, usuario):
    errores = []

    # Criterio 1: longitud mínima de 12 caracteres
    if len(contrasena) < 12:
        errores.append("Tener al menos 12 caracteres")

    # Criterio 2: no puede tener secuencias obvias
    secuencias = ["123", "234", "345", "456", "567", "678", "789",
                  "abc", "bcd", "cde", "def", "efg",
                  "qwerty", "asdf", "zxcv"]
    contrasena_lower = contrasena.lower()
    for secuencia in secuencias:
        if secuencia in contrasena_lower:
            errores.append("No puede contener secuencias obvias como '123' o 'abc'")
            break

    # Criterio 3: no puede tener repeticiones de caracteres
    for i in range(len(contrasena) - 2):
        if contrasena[i] == contrasena[i+1] == contrasena[i+2]:
            errores.append("No puede tener tres caracteres iguales seguidos (ej: 'aaa', '111')")
            break

    # Criterio 4: no puede tener sustituciones comunes predecibles
    sustituciones = {
        "4": "a", "@": "a", "3": "e", "1": "i",
        "!": "i", "0": "o", "$": "s", "5": "s"
    }
    contrasena_normalizada = contrasena.lower()
    for simbolo, letra in sustituciones.items():
        contrasena_normalizada = contrasena_normalizada.replace(simbolo, letra)

    palabras_comunes = ["password", "contrasena",
                        "guardianclima", "clima", "admin", "usuario"]
    for palabra in palabras_comunes:
        if palabra in contrasena_normalizada:
            errores.append(f"No puede contener palabras comunes o predecibles como '{palabra}'")
            break

    # Criterio 5: No poner tu usuario en la contraseña
    if usuario.lower() in contrasena.lower():
        errores.append(f"No puede contener tu nombre de usuario '{usuario}'")

    # Resultado
    if len(errores) == 0:
        return True, []
    else:
        return False, errores

def registrar_usuario():

    print("\n" + "=" * 50)
    print("         REGISTRAR NUEVO USUARIO")
    print("=" * 50)

    # ── PASO 1: PEDIR NOMBRE DE USUARIO ──────────────
    while True:
        usuario = input("\nElegí un nombre de usuario: ").strip()

        if usuario == "":
            print("⚠️  El nombre de usuario no puede estar vacío.")
            continue

        # Verificar que el usuario no exista ya en el CSV
        usuarios_existentes = []
        if os.path.exists(ARCHIVO_USUARIOS):
            with open(ARCHIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    usuarios_existentes.append(fila["username"].lower())

        if usuario.lower() in usuarios_existentes:
            print(f"⚠️  El usuario '{usuario}' ya existe. Elegí otro.")
        else:
            break

    # ── PASO 2: PEDIR Y VALIDAR CONTRASEÑA ───────────
    while True:
        contrasena = input("\nElegí una contraseña: ").strip()

        if contrasena == "":
            print("⚠️  La contraseña no puede estar vacía.")
            continue

        valida, errores = validar_contrasena(contrasena, usuario)

        if not valida:
            print("\n❌ Tu contraseña no cumple con los siguientes criterios:")
            for error in errores:
                print(f"   • {error}")
            print("\n💡 Para una contraseña más segura considerá algo como: Cielo!Lluvia#47")
            print("   Una combinación de palabras sin relación, números y símbolos.")
        else:
            break

    # ── PASO 3: GUARDAR EN EL CSV ─────────────────────
    archivo_existe = os.path.exists(ARCHIVO_USUARIOS)
    with open(ARCHIVO_USUARIOS, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if not archivo_existe:
            escritor.writerow(ENCABEZADOS)
        escritor.writerow([usuario, contrasena])

    print(f"\n✅ Usuario '{usuario}' registrado correctamente.")
    print("   Iniciando sesión automáticamente...")

    return usuario


def iniciar_sesion():

    print("\n" + "=" * 50)
    print("            INICIAR SESIÓN")
    print("=" * 50)

    if not os.path.exists(ARCHIVO_USUARIOS):
        print("\n⚠️  Todavía no hay usuarios registrados.")
        print("   Volvé al menú y registrate primero.")
        return None

    intentos = 0

    while intentos < 3:

        usuario = input("\nNombre de usuario: ").strip()

        # Primero verificar si el usuario existe
        usuario_existe = False
        with open(ARCHIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["username"].lower() == usuario.lower():
                    usuario_existe = True
                    break

        if not usuario_existe:
            print(f"\n❌ El usuario '{usuario}' no existe.")
            print("   Podés registrarte desde el menú de acceso.")
            return None

        # Si el usuario existe, ahí pedimos la contraseña
        contrasena = input("Contraseña: ").strip()

        with open(ARCHIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["username"].lower() == usuario.lower() and \
                   fila["password_simulada"] == contrasena:
                    print(f"\n✅ Bienvenido/a, {usuario}!")
                    return usuario

        # Si llegó hasta acá es porque la contraseña era incorrecta
        intentos += 1
        intentos_restantes = 3 - intentos

        if intentos_restantes > 0:
            print(f"\n❌ Contraseña incorrecta.")
            print(f"   Te quedan {intentos_restantes} intento/s.")
        else:
            print("\n❌ Demasiados intentos fallidos.")
            print("   Volvé al menú de acceso e intentá de nuevo.")

    return None