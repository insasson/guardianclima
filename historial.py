# historial.py
# Guardar y leer historial_global.csv
# Persona 2: Vicente

import csv
import os
from datetime import datetime

ARCHIVO_HISTORIAL = "datos/historial_global.csv"
ENCABEZADOS = ["NombreDeUsuario", "Ciudad", "FechaHora", "Temperatura_C", "Condicion_Clima", "Humedad_Porcentaje", "Viento_kmh"]


def guardar_consulta(usuario, ciudad, temperatura, condicion, humedad, viento):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nueva_fila = [usuario, ciudad, fecha_hora, temperatura, condicion, humedad, viento]
    archivo_existe = os.path.exists(ARCHIVO_HISTORIAL)

    with open(ARCHIVO_HISTORIAL, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if not archivo_existe:
            escritor.writerow(ENCABEZADOS)
        escritor.writerow(nueva_fila)

    print(f"\n✅ Consulta guardada correctamente en el historial.")


def ver_historial_personal(usuario, ciudad):
    if not os.path.exists(ARCHIVO_HISTORIAL):
        print("\n⚠️  Todavía no hay consultas registradas.")
        return

    registros_encontrados = []

    with open(ARCHIVO_HISTORIAL, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["NombreDeUsuario"].lower() == usuario.lower() and \
               fila["Ciudad"].lower() == ciudad.lower():
                registros_encontrados.append(fila)

    if not registros_encontrados:
        print(f"\n⚠️  No se encontraron consultas para '{usuario}' en '{ciudad}'.")
        return

    registros_encontrados.sort(key=lambda x: x["FechaHora"], reverse=True)

    print(f"\n📋 Historial de {usuario} para {ciudad} ({len(registros_encontrados)} consultas):")
    print("-" * 60)
    for registro in registros_encontrados:
        print(f"   Fecha/Hora : {registro['FechaHora']}")
        print(f"   Temperatura: {registro['Temperatura_C']}°C")
        print(f"   Condición  : {registro['Condicion_Clima']}")
        print(f"   Humedad    : {registro['Humedad_Porcentaje']}%")
        print(f"   Viento     : {registro['Viento_kmh']} km/h")
        print("-" * 60)