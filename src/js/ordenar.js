/**
 * Ordena los datos según el criterio especificado.
 * @param {Object} datos - Los datos a ordenar.
 * @param {string} orden - El criterio de ordenamiento ('porcentaje', 'faltas', 'faltas_restantes', 'valor_porcentaje_falta').
 * @returns {Array} - Los datos ordenados en forma descendente.
 */
export function ordenarDatos(datos, orden) {
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
        case 'valor_porcentaje_falta':
            datosOrdenados = datos['Valor_porcentaje_falta'];
            break;
        default:
            datosOrdenados = datos['Faltas_no_justificadas'];
    }
    return Object.entries(datosOrdenados).sort((a, b) => b[1] - a[1]);
}
