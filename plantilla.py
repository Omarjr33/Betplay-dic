
import mensajes
from equipos import equipos

def registrar_integrante(tipo):
    print(mensajes.REGISTRO_INTEGRANTE)
    nombre = input(mensajes.NOMBRE_INTEGRANTE)
    equipo = input("Ingrese el nombre del equipo al que pertenece: ")
    
    if equipo not in equipos:
        return "El equipo no existe."
    
    if tipo == '1':  # Jugador
        equipos[equipo]['jugadores'].append({
            'nombre': nombre,
            'goles': 0,
            'tarjetas_amarillas': 0,
            'tarjetas_rojas': 0,
            'faltas': 0
        })
    else:
        equipos[equipo]['cuerpo_tecnico'].append({
            'nombre': nombre,
            'tipo': tipo
        })
    
    print(mensajes.INTEGRANTE_REGISTRADO)

