import { ordenarDatos } from './ordenar.js';
import { crearTabla } from './tabla.js';
export function cargarDatosAsistencia(orden) {
    fetch('data/asistencia.json')
        .then(respuesta => respuesta.json())
        .then(datos => {
            let datosOrdenados = ordenarDatos(datos, orden);
            crearTabla(datosOrdenados, datos);
        });
}





