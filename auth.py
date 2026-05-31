# auth.py
# Registro e inicio de sesión con validación de contraseña
# Persona 1: Indiana

import csv
import os

import re
# ACLARACIÓN: 're' es el módulo de Python que te permite colocar carcteres especiales
# re.search(patron, texto) devuelve un resultado si encuentra el patrón, o none si no lo encuentra.

ARCHIVO_USUARIOS = "datos/usuarios_simulados.csv"
ENCABEZADOS = ["username", "password_simulada"]

# os.makedirs() crea la carpeta 'datos/' si no existe todavía.
# exist_ok=True hace que no tire error si la carpeta ya estaba creada.
os.makedirs("datos", exist_ok=True)


def validar_contrasena(contrasena, usuario):
    errores = []

    # Criterio 1: longitud mínima de 12 caracteres
    if len(contrasena) < 12:
        errores.append("Tener al menos 12 caracteres")

    # Criterio 2: al menos una mayúscula
    if not any(c.isupper() for c in contrasena):
        errores.append("Tener al menos una letra mayúscula")

    # Criterio 3: al menos un carácter especial
    if not re.search(r"[!@#$%&*]", contrasena):
        errores.append("Tener al menos un carácter especial (! @ # $ % & *)")

    # Criterio 4: no puede tener secuencias obvias
    secuencias = ["123", "234", "345", "456", "567", "678", "789",
                  "abc", "bcd", "cde", "def", "efg",
                  "qwerty", "asdf", "zxcv"]
    contrasena_lower = contrasena.lower()
    for secuencia in secuencias:
        if secuencia in contrasena_lower:
            errores.append("No puede contener secuencias obvias como '123' o 'abc'")
            break

    # Criterio 5: no puede tener repeticiones de caracteres
    for i in range(len(contrasena) - 2):
        if contrasena[i] == contrasena[i+1] == contrasena[i+2]:
            errores.append("No puede tener tres caracteres iguales seguidos (ej: 'aaa', '111')")
            break

    # Criterio 6: no puede contener partes del nombre de usuario.
    # Extrae solo las letras del usuario (sin números ni símbolos) para detectar si aparecen en la contraseña.
    # Ej: si el usuario es "anonimo123", detecta "anonimo" en la contraseña.
    parte_letras = re.sub(r"[^a-zA-Z]", "", usuario)
    if len(parte_letras) >= 4 and parte_letras.lower() in contrasena.lower():
        errores.append(f"No puede contener tu nombre de usuario o partes de él")

    if len(errores) == 0:
        return True, []
    else:
        return False, errores

def registrar_usuario():

    print("\n" + "=" * 50)
    print("         REGISTRAR NUEVO USUARIO")
    print("=" * 50)

    # PASO 1: Pedir nombre de usuario
    while True:
        usuario = input("Elegí un nombre de usuario: ").strip()

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

    # PASO 2: Pedir y validar contraseña
    while True:
        contrasena = input("Elegí una contraseña: ").strip()

        if contrasena == "":
            print(" ERROR! La contraseña no puede estar vacía.")
            continue

        valida, errores = validar_contrasena(contrasena, usuario)

        if not valida:
            print("Tu contraseña no cumple con los siguientes criterios:")
            for error in errores:
                print(f"   • {error}")
            print("RECMENDACIÓN: Para una contraseña más segura considerá algo como: Cielo!Lluvia#47")
            print("   Una combinación de palabras sin relación, números y símbolos.")
        else:
            break

    # PASO 3: Guardar en el csv 
    archivo_existe = os.path.exists(ARCHIVO_USUARIOS)
    with open(ARCHIVO_USUARIOS, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if not archivo_existe:
            escritor.writerow(ENCABEZADOS)
        escritor.writerow([usuario, contrasena])

    print(f"Usuario '{usuario}' registrado correctamente.")
    

    return usuario


def iniciar_sesion():

    print("\n" + "=" * 50)
    print("            INICIAR SESIÓN")
    print("=" * 50)

    if not os.path.exists(ARCHIVO_USUARIOS):
        print("ERROR! Todavía no hay usuarios registrados.")
        print("   Volvé al menú y registrate primero.")
        return None

    intentos = 0

    while intentos < 3:

        usuario = input("Nombre de usuario: ").strip()

        # Primero verificar si el usuario existe
        usuario_existe = False
        with open(ARCHIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["username"].lower() == usuario.lower():
                    usuario_existe = True
                    break

        if not usuario_existe:
            print(f"ERROR! El usuario '{usuario}' no existe.")
            print("   Podés registrarte desde el menú de acceso.")
            return None

        # Si el usuario existe, ahí pedimos la contraseña
        contrasena = input("Contraseña: ").strip()

        with open(ARCHIVO_USUARIOS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["username"].lower() == usuario.lower() and \
                   fila["password_simulada"] == contrasena:
                    print(f"Bienvenido/a, {usuario}!")
                    return usuario

        # Si llegó hasta acá es porque la contraseña era incorrecta
        intentos += 1
        intentos_restantes = 3 - intentos

        if intentos_restantes > 0:
            print(f"ERROR! Contraseña incorrecta.")
            print(f"   Te quedan {intentos_restantes} intento/s.")
        else:
            print("Demasiados intentos fallidos.")
            print("Volvé al menú de acceso e intentá de nuevo.")

    return None