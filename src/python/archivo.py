import os
import json

# Función para escribir los datos procesados en un archivo JSON
def escribir_json(asistencia_data, faltas_asignaturas, porcentaje_faltas, faltas_restantes, valor_porcentaje_falta):
    # Crea el directorio 'data' si no existe
    os.makedirs('data', exist_ok=True)
    # Abre el archivo 'asistencia.json' en modo escritura
    with open('data/asistencia.json', 'w', encoding='utf-8') as json_file:
        # Escribe los datos en el archivo en formato JSON
        json.dump({'Asistencia': asistencia_data, 'Faltas_no_justificadas': faltas_asignaturas, 'Porcentaje_faltas': porcentaje_faltas, 'Faltas_restantes': faltas_restantes, 'Valor_porcentaje_falta': valor_porcentaje_falta}, json_file, ensure_ascii=False, indent=4)
