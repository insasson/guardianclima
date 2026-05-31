# estadisticas.py
# Calcular estadísticas globales del historial
# Persona 2: Vicente

import csv
import os

ARCHIVO_HISTORIAL = "datos/historial_global.csv"


def mostrar_estadisticas_globales():
    if not os.path.exists(ARCHIVO_HISTORIAL):
        print("ERROR! Todavía no hay datos registrados en el historial.")
        return

    ciudades = []
    temperaturas = []

    with open(ARCHIVO_HISTORIAL, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            ciudades.append(fila["Ciudad"])
            try:
                temperaturas.append(float(fila["Temperatura_C"]))
            except ValueError:
                pass

    if not ciudades:
        print("ERROR! El historial existe pero todavía no tiene consultas registradas.")
        return

    total_consultas = len(ciudades)

    conteo_ciudades = {}
    for ciudad in ciudades:
        if ciudad in conteo_ciudades:
            conteo_ciudades[ciudad] += 1
        else:
            conteo_ciudades[ciudad] = 1

    ciudad_mas_consultada = max(conteo_ciudades, key=conteo_ciudades.get)
    veces_consultada = conteo_ciudades[ciudad_mas_consultada]

    temp_promedio = sum(temperaturas) / len(temperaturas) if temperaturas else None

    print("\n" + "=" * 50)
    print("        ESTADÍSTICAS GLOBALES DE USO")
    print("=" * 50)
    print(f"    Ciudad más consultada : {ciudad_mas_consultada} ({veces_consultada} veces)")
    print(f"   Total de consultas     : {total_consultas}")
    if temp_promedio is not None:
        print(f"  🌡️  Temperatura promedio   : {temp_promedio:.1f}°C")
    else:
        print(f"  🌡️  Temperatura promedio   : Sin datos")
    print("=" * 50)