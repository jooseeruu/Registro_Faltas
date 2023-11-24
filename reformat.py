import json

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
    start_time = time_slots[0]
    end_time = time_slots[1]

    # Crea un diccionario para cada entrada de asistencia
    asistencia_entry = {
        'Fecha': date,
        'Asistencia': status,
        'Clase': details,
        'Hora_inicio': start_time,
        'Hora_fin': end_time
    }

    # Agrega la entrada al conjunto de datos
    asistencia_data.append(asistencia_entry)

# Convierte a formato JSON y escribe en un archivo
with open('asistencia.json', 'w', encoding='utf-8') as json_file:
    json.dump(asistencia_data, json_file, ensure_ascii=False, indent=4)

print("Archivo JSON generado con éxito: 'asistencia.json'")

