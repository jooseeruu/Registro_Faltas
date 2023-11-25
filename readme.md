# Proyecto REGISTRO_FALTAS

## Descripción

Este proyecto se encarga de la gestión de la asistencia. Permite registrar las faltas de asistencia de los estudiantes y calcular el porcentaje de faltas por asignatura.

## Estructura del proyecto

El proyecto está organizado en las siguientes carpetas:

- `src`: Contiene el código fuente del proyecto.
  - `js`: Contiene los archivos JavaScript.
  - `css`: Contiene los archivos de estilos CSS.
  - `python`: Contiene los scripts de Python.
- `data`: Contiene los archivos de datos en formato JSON y TXT.

El archivo `asistencia.html` es el punto de entrada al sitio web y se encuentra en la carpeta raíz del proyecto.

## Cómo usar

1. Clona el repositorio en tu máquina local.
2. Abre el archivo `asistencia.html` en tu navegador para ver la tabla de asistencia.
3. Los datos de asistencia se cargan en `asistencia.txt` siguiendo el formato de ejemplo, compila `procesar_asistencia.py`.
4. Se generará un archivo `asistentia.json` que será utilizado por `asistencia.js`.
5. Compila con *Live Server* `asistencia.html`y verás tus faltas ordenadas en una tabla.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir lo que te gustaría cambiar o añadir.