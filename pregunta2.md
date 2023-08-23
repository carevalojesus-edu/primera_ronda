# Análisis de Interacciones en Red Social
Se te ha entregado un archivo JSON que contiene información sobre varios usuarios, sus respectivos amigos y las conversaciones que han tenido. Tu tarea es analizar este archivo y responder a una serie de consultas sobre las interacciones de estos usuarios.

Tareas a Realizar:
1. Usuario Social:
Identifica y devuelve el nombre del usuario que tiene el mayor número de amigos.

2. Conversador Activo:
Identifica y devuelve el nombre del usuario que ha enviado el mayor número de mensajes.

3. Amistad Comunicativa:
Determina cuáles dos usuarios (sus id) han intercambiado el mayor número de mensajes entre ellos.

4. Mensajes Específicos:
Se te proporcionará una lista de frases o palabras clave. Debes buscar y devolver todas las conversaciones (usuario y amigo) que contienen al menos una de estas frases o palabras en sus mensajes.

## Entrada:
Un archivo JSON estructurado como se mostró anteriormente.
Una lista de frases o palabras clave para la tarea 4.

## Salida:
```El nombre del usuario con más amigos.
El nombre del usuario que ha enviado más mensajes.
Los id de los dos usuarios que han intercambiado más mensajes.
Una lista de usuarios, amigos y los mensajes correspondientes que contienen al menos una de las frases o palabras clave proporcionadas.
