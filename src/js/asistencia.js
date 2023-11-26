// Función para ordenar los datos
function ordenarDatos(datos, orden) {
    let datosOrdenados;
    switch (orden) {
        case 'porcentaje':
            datosOrdenados = datos['Porcentaje_faltas'];
            break;
        case 'faltas':
            datosOrdenados = datos['Faltas_no_justificadas'];
            break;
        case 'faltas_restantes':
            datosOrdenados = datos['Faltas_restantes'];
            break;
        default:
            datosOrdenados = datos['Faltas_no_justificadas'];
    }
    return Object.entries(datosOrdenados).sort((a, b) => b[1] - a[1]);
}

// Función para crear la tabla
function crearTabla(datosOrdenados, datos) {
    const tabla = document.getElementById('asistenciaTable');
    tabla.innerHTML = '<tr><th>Asignatura</th><th>Faltas</th><th>Porcentaje de Faltas</th><th>Faltas Restantes</th></tr>';
    for (let [asignatura, valor] of datosOrdenados) {
        let fila = tabla.insertRow(-1);
        let celda1 = fila.insertCell(0);
        let celda2 = fila.insertCell(1);
        let celda3 = fila.insertCell(2);
        let celda4 = fila.insertCell(3);
        celda1.innerHTML = asignatura;
        celda2.innerHTML = datos['Faltas_no_justificadas'][asignatura];
        celda3.innerHTML = (datos['Porcentaje_faltas'][asignatura] * 1).toFixed(2) + '%';
        celda4.innerHTML = datos['Faltas_restantes'][asignatura];
    }
}

// Función para cargar los datos de asistencia
function cargarDatosAsistencia(orden) {
    fetch('data/asistencia.json')
        .then(respuesta => respuesta.json())
        .then(datos => {
            let datosOrdenados = ordenarDatos(datos, orden);
            crearTabla(datosOrdenados, datos);
        });
}





