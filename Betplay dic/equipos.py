
import mensajes

equipos = {}

def registrar_equipo():
    print(mensajes.REGISTRO_EQUIPO)
    nombre = input(mensajes.NOMBRE_EQUIPO)
    equipos[nombre] = {
        'jugadores': [],
        'cuerpo_tecnico': [],
        'goles_favor': 0,
        'goles_contra': 0,
        'puntos': 0
    }
    print(mensajes.EQUIPO_REGISTRADO)

def obtener_equipo_mas_goles():
    if not equipos:
        return "No hay equipos registrados."
    return max(equipos, key=lambda x: equipos[x]['goles_favor'])

def obtener_equipo_mas_goles_contra():
    if not equipos:
        return "No hay equipos registrados."
    return max(equipos, key=lambda x: equipos[x]['goles_contra'])

def obtener_ultimo_equipo():
    if not equipos:
        return "No hay equipos registrados."
    return min(equipos, key=lambda x: equipos[x]['puntos'])

# ... Puedes agregar más funciones relacionadas con equipos según sea necesario