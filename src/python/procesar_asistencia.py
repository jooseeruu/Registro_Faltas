import json
import os
from datetime import datetime

# Función para leer los datos de asistencia desde un archivo
def leer_asistencia():
    with open('data/asistencia.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

# Función para procesar los datos de asistencia
def procesar_asistencia(data, faltas_asignaturas):
    asistencia_data = []
    for line in data:
        line = line.strip().split(': ')
        date, info = line[0], line[1]
        parts = info.split(' a ')
        status = parts[0]
        details = parts[1].split(' (')[0]
        time_slots = parts[1].split(' (')[1].split(')')[0].split('-')
        start_time = datetime.strptime(time_slots[0], "%H:%M")
        end_time = datetime.strptime(time_slots[1], "%H:%M")
        duration = (end_time - start_time).seconds / 60  
        asistencia_entry = {
            'Fecha': date,
            'Asistencia': status,
            'Clase': details,
            'Hora_inicio': start_time.strftime("%H:%M"),
            'Hora_fin': end_time.strftime("%H:%M"),
            'Duracion': duration
        }
        if status == 'Asistencia NO JUSTIFICADA':
            faltas_asignaturas[details] += 1
        asistencia_data.append(asistencia_entry)
    return asistencia_data

# Función para calcular el porcentaje de faltas
def calcular_porcentaje_faltas(faltas_asignaturas, horas_asignaturas):
    porcentaje_faltas = {asignatura: (faltas / horas) * 100 for asignatura, faltas, horas in zip(faltas_asignaturas.keys(), faltas_asignaturas.values(), horas_asignaturas.values())}
    return porcentaje_faltas

# Función para calcular el número de faltas restantes hasta el 15%
def calcular_faltas_restantes(faltas_asignaturas, horas_asignaturas):
    faltas_restantes = {asignatura: int(horas * 0.15) - faltas for asignatura, faltas, horas in zip(faltas_asignaturas.keys(), faltas_asignaturas.values(), horas_asignaturas.values())}
    return faltas_restantes

# Función para escribir los datos procesados en un archivo JSON
def escribir_json(asistencia_data, faltas_asignaturas, porcentaje_faltas, faltas_restantes):
    os.makedirs('data', exist_ok=True)
    with open('data/asistencia.json', 'w', encoding='utf-8') as json_file:
        json.dump({'Asistencia': asistencia_data, 'Faltas_no_justificadas': faltas_asignaturas, 'Porcentaje_faltas': porcentaje_faltas, 'Faltas_restantes': faltas_restantes}, json_file, ensure_ascii=False, indent=4)

# Función principal que llama a las demás funciones
def main():
    horas_asignaturas = {
        'Desarrollo web en entorno cliente': 125,
        'Desarrollo web en entorno servidor': 160,
        'Despliegue de aplicaciones web': 90,
        'Diseño de interfaces web': 165,
        'Empresa e iniciativa emprendedora': 60,
        'Proyecto de Desarrollo de Aplicaciones Web': 40
    }
    faltas_asignaturas = {asignatura: 0 for asignatura in horas_asignaturas.keys()}
    data = leer_asistencia()
    asistencia_data = procesar_asistencia(data, faltas_asignaturas)
    porcentaje_faltas = calcular_porcentaje_faltas(faltas_asignaturas, horas_asignaturas)
    faltas_restantes = calcular_faltas_restantes(faltas_asignaturas, horas_asignaturas)
    escribir_json(asistencia_data, faltas_asignaturas, porcentaje_faltas, faltas_restantes)
    print("Archivo JSON generado con éxito: 'asistencia.json'")

# Comprueba si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
