import { cargarDatosAsistencia } from './asistencia.js';

// Asigna los manejadores de eventos después de que el DOM esté completamente cargado
window.addEventListener('DOMContentLoaded', (event) => {
    // Ordena por porcentaje por defecto
    cargarDatosAsistencia('porcentaje');

    // Asigna los manejadores de eventos a los botones
    document.querySelector('#porcentajeButton').addEventListener('click', () => cargarDatosAsistencia('porcentaje'));
    document.querySelector('#faltasButton').addEventListener('click', () => cargarDatosAsistencia('faltas'));
    document.querySelector('#faltasRestantesButton').addEventListener('click', () => cargarDatosAsistencia('faltas_restantes'));
});
