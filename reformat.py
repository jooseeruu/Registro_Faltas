import json
from datetime import datetime

# Define las horas totales para cada asignatura
horas_asignaturas = {
    'Desarrollo web en entorno cliente': 125,
    'Desarrollo web en entorno servidor': 160,
    'Despliegue de aplicaciones web': 90,
    'Diseño de interfaces web': 165,
    'Empresa e iniciativa emprendedora': 60,
    'Proyecto de Desarrollo de Aplicaciones Web': 40
}

# Inicializa un diccionario para llevar la cuenta de las faltas por asignatura
faltas_asignaturas = {asignatura: 0 for asignatura in horas_asignaturas.keys()}

# Lee el archivo 'asistencia.txt' con la codificación 'utf-8'
with open('asistencia.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

asistencia_data = []

# Procesa cada línea del archivo
for line in data:
    line = line.strip().split(': ')
    date, info = line[0], line[1]

    # Separa la información en elementos
    parts = info.split(' a ')
    status = parts[0]
    details = parts[1].split(' (')[0]
    time_slots = parts[1].split(' (')[1].split(')')[0].split('-')

    # Extrae la información relevante
    start_time = datetime.strptime(time_slots[0], "%H:%M")
    end_time = datetime.strptime(time_slots[1], "%H:%M")

    # Calcula la duración de la clase en horas
    duration = (end_time - start_time).seconds / 3600

    # Crea un diccionario para cada entrada de asistencia
    asistencia_entry = {
        'Fecha': date,
        'Asistencia': status,
        'Clase': details,
        'Hora_inicio': start_time.strftime("%H:%M"),
        'Hora_fin': end_time.strftime("%H:%M"),
        'Duracion': duration
    }

    # Si la asistencia es 'Asistencia NO JUSTIFICADA', suma 1 a las faltas de la asignatura
    if status == 'Asistencia NO JUSTIFICADA':
        faltas_asignaturas[details] += 1

    # Agrega la entrada al conjunto de datos
    asistencia_data.append(asistencia_entry)

# Calcula el porcentaje total de faltas para cada asignatura
porcentaje_faltas = {asignatura: (faltas / horas) * 100 for asignatura, faltas, horas in zip(faltas_asignaturas.keys(), faltas_asignaturas.values(), horas_asignaturas.values())}

# Convierte a formato JSON y escribe en un archivo
with open('asistencia.json', 'w', encoding='utf-8') as json_file:
    json.dump({'Asistencia': asistencia_data, 'Faltas_no_justificadas': faltas_asignaturas, 'Porcentaje_faltas': porcentaje_faltas}, json_file, ensure_ascii=False, indent=4)

print("Archivo JSON generado con éxito: 'asistencia.json'")
