import json
from datetime import datetime

def leer_asistencia():
    with open('asistencia.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

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
        duration = (end_time - start_time).seconds / 3600
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

def calcular_porcentaje_faltas(faltas_asignaturas, horas_asignaturas):
    porcentaje_faltas = {asignatura: (faltas / horas) * 100 for asignatura, faltas, horas in zip(faltas_asignaturas.keys(), faltas_asignaturas.values(), horas_asignaturas.values())}
    return porcentaje_faltas

def escribir_json(asistencia_data, faltas_asignaturas, porcentaje_faltas):
    with open('asistencia.json', 'w', encoding='utf-8') as json_file:
        json.dump({'Asistencia': asistencia_data, 'Faltas_no_justificadas': faltas_asignaturas, 'Porcentaje_faltas': porcentaje_faltas}, json_file, ensure_ascii=False, indent=4)

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
    escribir_json(asistencia_data, faltas_asignaturas, porcentaje_faltas)
    print("Archivo JSON generado con éxito: 'asistencia.json'")

if __name__ == "__main__":
    main()

