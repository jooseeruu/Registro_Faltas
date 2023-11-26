# Registro de Faltas

Este proyecto proporciona una forma de registrar y analizar las faltas de asistencia.

## Estructura del Proyecto

El proyecto se divide en varias partes:

- `data`: Esta carpeta contiene los datos de asistencia en formato de texto y JSON.
- `src`: Esta carpeta contiene los archivos de código fuente del proyecto.
  - `css`: Esta carpeta contiene los estilos CSS para la interfaz de usuario.
  - `js`: Esta carpeta contiene los scripts de JavaScript para la funcionalidad del lado del cliente.
  - `python`: Esta carpeta contiene los scripts de Python para procesar los datos de asistencia.
- `.gitignore`: Este archivo le dice a Git qué archivos o carpetas ignorar.
- `asistencia.html`: Este archivo es la página principal de la aplicación web.

## Funcionamiento

El proyecto funciona de la siguiente manera:

1. Los datos de asistencia se almacenan en un archivo de texto en la carpeta `data`.
2. Los scripts de Python en la carpeta `src/python` procesan estos datos y generan un archivo JSON en la carpeta `data`.
3. La página `asistencia.html` carga estos datos JSON y los muestra en una tabla. Los usuarios pueden ordenar los datos por diferentes criterios utilizando los botones proporcionados.

## Cómo Usarlo

Para usar este proyecto, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta los scripts de Python para procesar los datos de asistencia.
3. Abre `asistencia.html` en tu navegador para ver los datos.

## Contribuir

Las contribuciones a este proyecto son bienvenidas. Por favor, abre un problema para discutir lo que te gustaría cambiar o añadir.
