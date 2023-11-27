// Esta función crea una tabla en el documento HTML con los datos proporcionados.
// Recibe dos parámetros: datosOrdenados y datos.
export function crearTabla(datosOrdenados, datos) {
    // Obtiene el elemento de la tabla en el documento HTML con el id 'asistenciaTable'
    const tabla = document.getElementById('asistenciaTable');

    // Limpia el contenido de la tabla
    tabla.innerHTML = '<tr><th>Asignatura</th><th>Faltas</th><th>Porcentaje de Faltas</th><th>Faltas Restantes</th><th>Impacto por Falta</th></tr>';

    // Itera sobre los datos ordenados
    for (let [asignatura,] of datosOrdenados) {
        // Crea una nueva fila en la tabla
        let fila = tabla.insertRow(-1);

        // Inserta celdas en la fila
        let celda1 = fila.insertCell(0);
        let celda2 = fila.insertCell(1);
        let celda3 = fila.insertCell(2);
        let celda4 = fila.insertCell(3);
        let celda5 = fila.insertCell(4);

        // Asigna los valores correspondientes a cada celda
        celda1.innerHTML = asignatura;
        celda2.innerHTML = datos['Faltas_no_justificadas'][asignatura];
        celda3.innerHTML = (datos['Porcentaje_faltas'][asignatura] * 1).toFixed(2) + '%';
        celda4.innerHTML = datos['Faltas_restantes'][asignatura];
        celda5.innerHTML = (datos['Valor_porcentaje_falta'][asignatura] * 1).toFixed(2) + '%';
    }
}
