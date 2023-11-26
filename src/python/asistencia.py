from datetime import datetime

# Función para leer los datos de asistencia desde un archivo
def leer_asistencia():
    # Abre el archivo en modo lectura y lee todas las líneas
    with open('data/asistencia.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

# Función para procesar los datos de asistencia
def procesar_asistencia(data, faltas_asignaturas):
    # Inicializa una lista vacía para almacenar los datos de asistencia procesados
    asistencia_data = []
    # Recorre cada línea de los datos
    for line in data:
        # Divide la línea en fecha e información de asistencia
        line = line.strip().split(': ')
        date, info = line[0], line[1]
        # Divide la información de asistencia en estado y detalles
        parts = info.split(' a ')
        status = parts[0]
        # Extrae los detalles de la asistencia y los intervalos de tiempo
        details = parts[1].split(' (')[0]
        time_slots = parts[1].split(' (')[1].split(')')[0].split('-')
        # Convierte los intervalos de tiempo a objetos datetime
        start_time = datetime.strptime(time_slots[0], "%H:%M")
        end_time = datetime.strptime(time_slots[1], "%H:%M")
        # Calcula la duración en minutos
        duration = (end_time - start_time).seconds / 60  
        # Crea un diccionario con los datos de asistencia
        asistencia_entry = {
            'Fecha': date,
            'Asistencia': status,
            'Clase': details,
            'Hora_inicio': start_time.strftime("%H:%M"),
            'Hora_fin': end_time.strftime("%H:%M"),
            'Duracion': duration
        }
        # Si la asistencia no está justificada, incrementa el conteo de faltas
        if status == 'Asistencia NO JUSTIFICADA':
            faltas_asignaturas[details] += 1
        # Añade el diccionario a la lista de datos de asistencia
        asistencia_data.append(asistencia_entry)
    return asistencia_data
