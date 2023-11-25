let faltas;
let porcentaje;

// Función para cargar los datos de asistencia
function cargarDatosAsistencia() {
    // Realiza una solicitud a la API para obtener los datos de asistencia
    fetch('data/asistencia.json')
        .then(respuesta => respuesta.json())  // Convierte la respuesta en un objeto JSON
        .then(datos => {
            const tabla = document.getElementById('asistenciaTable');  // Obtiene la tabla del DOM
            faltas = datos['Faltas_no_justificadas'];  // Obtiene las faltas de los datos
            porcentaje = datos['Porcentaje_faltas'];  // Obtiene el porcentaje de faltas de los datos

            // Ordena las faltas y el porcentaje de faltas de mayor a menor
            faltas = Object.entries(faltas).sort((a, b) => b[1] - a[1]);
            porcentaje = Object.entries(porcentaje).sort((a, b) => b[1] - a[1]);

            // Recorre las faltas y añade una fila a la tabla por cada falta
            for (let [asignatura, falta] of faltas) {
                let fila = tabla.insertRow(-1);  // Inserta una nueva fila al final de la tabla
                let celda1 = fila.insertCell(0);  // Inserta una nueva celda en la fila
                let celda2 = fila.insertCell(1);  // Inserta una nueva celda en la fila
                let celda3 = fila.insertCell(2);  // Inserta una nueva celda en la fila
                celda1.innerHTML = asignatura;  // Asigna el nombre de la asignatura a la primera celda
                celda2.innerHTML = falta;  // Asigna el número de faltas a la segunda celda
                // Busca el porcentaje de faltas de la asignatura y lo asigna a la tercera celda
                celda3.innerHTML = porcentaje.find(([asig,]) => asig === asignatura)[1].toFixed(2) + '%';
            }
        });
}

