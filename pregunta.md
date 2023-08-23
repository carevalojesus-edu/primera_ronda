# Análisis de Datos de Usuarios desde un JSON
Te ha sido proporcionado un archivo JSON con información detallada de varios usuarios, sus respectivas publicaciones y los comentarios que han hecho. Debes analizar este archivo y responder a una serie de consultas sobre estos datos.

## Tareas a Realizar:
1. Usuario Activo:
Encuentra el nombre del usuario que ha hecho más publicaciones.

2. Comentador Principal:
Encuentra el nombre del usuario que ha escrito más comentarios.

3. Publicación Popular:
Encuentra la id_pub de la publicación que ha recibido más comentarios de diferentes usuarios.

4. Búsqueda de Palabras Clave:
Dada una lista de palabras clave, encuentra todas las publicaciones y comentarios que contienen al menos una de esas palabras clave.

Entrada:
Un archivo JSON con la estructura mencionada anteriormente.
Una lista de palabras clave para la tarea 4.
Salida:
El nombre del usuario más activo.
El nombre del principal comentador.
La id_pub de la publicación más popular.
Una lista de id_pub y textos de publicaciones y comentarios que contienen las palabras clave.

```Usuario más activo: Juan
Principal comentador: Juan
Publicación más popular: A
Publicaciones y comentarios con palabras clave:
- id_pub: A, texto: "Publicación 1 de Juan"
- id_pub: B, texto: "Publicación 2 de Juan"
- id_pub: A, texto: "Comentario en la publicación A"
