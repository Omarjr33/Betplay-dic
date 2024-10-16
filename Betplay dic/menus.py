
import mensajes

def mostrar_menu_principal():
    print(mensajes.MENU_PRINCIPAL)
    return input("Seleccione una opción: ")

def mostrar_menu_registro_integrante():
    print(mensajes.TIPO_INTEGRANTE)
    return input("Seleccione el tipo de integrante: ")

def mostrar_menu_estadisticas_equipos():
    print("""
    Estadísticas de equipos:
    1. Equipo con más goles marcados
    2. Equipo con más goles en contra
    3. Equipo en último puesto
    4. Volver al menú principal
    """)
    return input("Seleccione una opción: ")

def mostrar_menu_estadisticas_jugadores():
    print("""
    Estadísticas de jugadores:
    1. Jugador con más faltas cometidas
    2. Jugador con más tarjetas amarillas
    3. Volver al menú principal
    """)
    return input("Seleccione una opción: ")

