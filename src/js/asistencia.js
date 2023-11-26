// Importamos la función 'ordenarDatos' del archivo './ordenar.js'
// Importamos la función 'crearTabla' del archivo './tabla.js'
import { ordenarDatos } from './ordenar.js';
import { crearTabla } from './tabla.js';

// Definimos la función 'cargarDatosAsistencia' que recibe un parámetro 'orden'
export function cargarDatosAsistencia(orden) {
    // Realizamos una petición fetch para obtener los datos del archivo 'asistencia.json'
    fetch('data/asistencia.json')
        .then(respuesta => respuesta.json()) // Convertimos la respuesta a formato JSON
        .then(datos => {
            // Ordenamos los datos utilizando la función 'ordenarDatos' y el parámetro 'orden'
            let datosOrdenados = ordenarDatos(datos, orden);
            // Creamos una tabla utilizando la función 'crearTabla' y los datos ordenados y sin ordenar
            crearTabla(datosOrdenados, datos);
        });
}





