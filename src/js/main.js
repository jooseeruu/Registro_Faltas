document.addEventListener("DOMContentLoaded", async () => {
  const botones = {
    porcentajeButton: "Porcentaje_faltas",
    faltasButton: "Faltas_no_justificadas",
    faltasRestantesButton: "Faltas_restantes",
    valorPorcentajeFaltaButton: "Valor_porcentaje_falta"
  };

  await cargarDatosAsistencia("Porcentaje_faltas");
  Object.keys(botones).forEach((id) => {
    document
      .querySelector(`#${id}`)
      .addEventListener("click", () => cargarDatosAsistencia(botones[id]));
  });

  async function cargarDatosAsistencia(orden) {
    const respuesta = await fetch("data/asistencia.json");
    const datos = await respuesta.json();
    const datosOrdenados = ordenarDatos(datos, orden);
    crearTabla(datosOrdenados, datos);
  }

  function ordenarDatos(datos, orden) {
    return Object.entries(datos[orden]).sort((a, b) => b[1] - a[1]);
  }

  function crearTabla(datosOrdenados, datos) {
    const tabla = document.getElementById("asistenciaTable");
    // Limpiar las filas existentes
    tabla.innerHTML =
      "<tr><th>Asignatura</th><th>Faltas</th><th>Porcentaje de Faltas</th><th>Faltas Restantes</th><th>Impacto por Falta</th></tr>";
    datosOrdenados.forEach(([asignatura]) => {
      const fila = tabla.insertRow(-1);
      fila.innerHTML = `
                <td>${asignatura}</td>
                <td>${datos["Faltas_no_justificadas"][asignatura]}</td>
                <td>${(datos["Porcentaje_faltas"][asignatura] * 1).toFixed(2)}%</td>
                <td>${datos["Faltas_restantes"][asignatura]}</td>
                <td>${(datos["Valor_porcentaje_falta"][asignatura] * 1).toFixed(2)}%</td>
            `;
    });
  }
});
