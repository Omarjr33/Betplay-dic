
from equipos import equipos

def jugador_mas_faltas():
    jugadores = []
    for equipo in equipos.values():
        jugadores.extend(equipo['jugadores'])
    
    if not jugadores:
        return "No hay jugadores registrados."
    
    return max(jugadores, key=lambda x: x['faltas'])['nombre']

def jugador_mas_tarjetas_amarillas():
    jugadores = []
    for equipo in equipos.values():
        jugadores.extend(equipo['jugadores'])
    
    if not jugadores:
        return "No hay jugadores registrados."
    
    return max(jugadores, key=lambda x: x['tarjetas_amarillas'])['nombre']

