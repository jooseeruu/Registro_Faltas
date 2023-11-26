let faltas;
let porcentaje;

// Función para cargar los datos de asistencia
function cargarDatosAsistencia(orden) {
    // Realiza una solicitud a la API para obtener los datos de asistencia
    fetch('data/asistencia.json')
        .then(respuesta => respuesta.json())  // Convierte la respuesta en un objeto JSON
        .then(datos => {
            const tabla = document.getElementById('asistenciaTable');  // Obtiene la tabla del DOM
            faltas = datos['Faltas_no_justificadas'];  // Obtiene las faltas de los datos
            porcentaje = datos['Porcentaje_faltas'];  // Obtiene el porcentaje de faltas de los datos

            // Ordena los datos según el orden especificado
            let datosOrdenados = orden === 'porcentaje' ? porcentaje : faltas;
            datosOrdenados = Object.entries(datosOrdenados).sort((a, b) => b[1] - a[1]);

            // Limpia la tabla antes de agregar nuevas filas
            tabla.innerHTML = '<tr><th>Asignatura</th><th>Faltas</th><th>Porcentaje de Faltas</th></tr>';

            // Recorre los datos ordenados y añade una fila a la tabla por cada elemento
            for (let [asignatura, valor] of datosOrdenados) {
                let fila = tabla.insertRow(-1);  // Inserta una nueva fila al final de la tabla
                let celda1 = fila.insertCell(0);  // Inserta una nueva celda en la fila
                let celda2 = fila.insertCell(1);  // Inserta una nueva celda en la fila
                let celda3 = fila.insertCell(2);  // Inserta una nueva celda en la fila
                celda1.innerHTML = asignatura;  // Asigna el nombre de la asignatura a la primera celda
                celda2.innerHTML = faltas[asignatura];  // Asigna las faltas a la segunda celda
                celda3.innerHTML = (porcentaje[asignatura] * 1).toFixed(2) + '%';  // Asigna el porcentaje de faltas a la tercera celda

            }
        });
}



