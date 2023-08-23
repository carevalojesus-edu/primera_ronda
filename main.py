import json
import random

def generar_conversacion(id_usuario, id_amigo):
    num_mensajes = random.randint(1, 5)
    mensajes = [f"Mensaje {i} de Usuario{id_usuario} a Usuario{id_amigo}" for i in range(num_mensajes)]
    
    return {
        "con": id_amigo,
        "mensajes": mensajes
    }

def generar_usuario(id_usuario, total_usuarios):
    nombre = f"Usuario{id_usuario}"
    # Generar una lista de amigos aleatorios (entre 1 y 7 amigos). Evitar que un usuario sea amigo de sí mismo
    amigos = random.sample([i for i in range(1, total_usuarios + 1) if i != id_usuario], random.randint(1, 7))
    
    conversaciones = [generar_conversacion(id_usuario, id_amigo) for id_amigo in amigos]
    
    return {
        "id": id_usuario,
        "nombre": nombre,
        "amigos": amigos,
        "conversaciones": conversaciones
    }

usuarios = [generar_usuario(i, 100) for i in range(1, 101)]

data = {"usuarios": usuarios}

with open("interacciones.json", "w") as f:
    json.dump(data, f, indent=4)
