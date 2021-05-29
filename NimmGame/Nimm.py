"""Este programa corresponde al juego de Nimm en el que dos jugadores
tienen una pila de 20 piedras frente a sí. Por turnos, cada jugador toma
una o dos piedras de la pila. El jugador que tome la última piedra
pierde el juego.
"""
__version__ = 1.0
__author__ = "Sebastián Beltrán"

from Funciones import *

def nimm():
    """Esta función ejecuta el juego."""
    # Introducción al juego
    introduccion()
    
    # El usuario escoge el modo de juego
    modo_juego = elegir_modo()
    
    # Si el modo es PvP, los jugadores se identifican. Si es PvC
    # el jugador 1 se identifica 
    if modo_juego.lower() == 'p':
        jug1, jug2 = identificar_jugadores(modo_juego)
    else:
        jug1 = identificar_jugadores(modo_juego)
    
    # Ejecuta el modo de juego PvP
    if modo_juego.lower() == 'p':
        ganador = juego_PvP(jug1, jug2)
    # Ejecuta el modo de juego PvC
    else:
        ganador = juego_PvC(jug1)

    # Imprime el nombre del ganador y pregunta si se desea jugar de nuevo.
    # Devuelve un booleano. True = vuelve a ejecutarse, False = termina el programa.
    reinicio = fin_juego(ganador, jug1)

    return reinicio

# Ejecución del programa mientras el usuario quiera continuar jugando.
reinicio = True
while reinicio == True:
    reinicio = nimm()

print("\nGracias por jugar Nimm.")
print("Creado por J. Sebastián Beltrán.")
print("Más código en https://github.com/JSebas98")