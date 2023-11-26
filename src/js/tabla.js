export function crearTabla(datosOrdenados, datos) {
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