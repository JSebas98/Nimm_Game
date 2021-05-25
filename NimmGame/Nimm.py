"""Este programa corresponde al juego de Nimm en el que dos jugadores
tienen una pila de 20 piedras frente a sí. Por turnos, cada jugador toma
una o dos piedras de la pila. El jugador que tome la última piedra
pierde el juego.
"""
__version__ = 1.0
__author__ = "Sebastián Beltrán"

import random

MODOS_JUEGO = ['p', 'c']
OPS_FINAL = ['y', 'n']
# OPS_PIEDRAS = [1, 2]

def main():
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

def introduccion():
    """Esta función imprime la introducción y las instrucciones
    del juego
    """
    print("\n================ NIMM GAME ================")
    print("===== Creado por J. Sebastián Beltrán =====")
    print("\n¡Bienvenido al juego ancestral de Nimm!\n")
    print("============== INSTRUCCIONES ==============")
    print("Dos jugadores se turnan para tomar 1 o 2 piedras\n" 
        "de una pila de 20 piedras. El jugador que tome la\n" 
        "última piedra de la pila pierde.\n")

def elegir_modo():
    """Permite escoger entre modo PvP o PvC. Devuelve el modo escogido."""
    modo_juego = input("\nEscoge el modo de juego. \nJugador vs jugador: 'p'\t Jugador vs computador: 'c' ")
    while modo_juego not in MODOS_JUEGO:
        modo_juego = input("\nIngresa un modo de juego válido."
            "\nJugador vs jugador: 'p'\t Jugador vs computador: 'c' ")   
    
    return modo_juego

def identificar_jugadores(modo_juego):
    """Permite la identificación de los jugadores dependiendo del modo escogido.
    Devuelve los nombres de los jugadores.
    """
    if modo_juego.lower() == 'p':
        jug1 = input("Jugador 1, ingresa tu nombre: ")
        jug2 = input("Jugador 2, ingresa tu nombre: ")

        return jug1, jug2
    else:
        jug1 = input("Jugador, ingresa tu nombre: ")
        
        return jug1

def juego_PvP(jug1, jug2):
    """Ejecuta el modo de juego jugador vs jugador."""
    pila_piedras = 20
    while pila_piedras > 0:
        # Turno del jugador 1
        print(f"\nHay {pila_piedras} piedras disponibles.")
        turno = jug1
        piedras_tomadas = int(input(f"\n{jug1}, ¿quieres tomar 1 o 2 piedras? "))
        
        # Limita la cantidad de piedras tomadas cuando sólo queda una.
        while pila_piedras == 1 and piedras_tomadas == 2:
            piedras_tomadas = int(input(f"Lo siento, {jug1}. Sólo hay 1 piedra disponible. "))

        while piedras_tomadas < 1 or piedras_tomadas > 2:
            piedras_tomadas = int(input(f"{jug1}, ingresa 1 o 2: "))
        pila_piedras -= piedras_tomadas
        # Si el jugador 1 es el último en tomar una piedra, el ciclo se interrumpe
        # para evitar que se pida al jugador 2 tomar piedras.
        if pila_piedras == 0:
            break

        # Turno del jugador 2
        print(f"\nHay {pila_piedras} piedras disponibles.")
        turno = jug2
        piedras_tomadas = int(input(f"\n{jug2}, ¿quieres tomar 1 o 2 piedras? "))

        # Limita la cantidad de piedras tomadas cuando sólo queda una.
        while pila_piedras == 1 and piedras_tomadas == 2:
            piedras_tomadas = int(input(f"Lo siento, {jug2}. Sólo hay 1 piedra disponible. "))

        while piedras_tomadas < 1 or piedras_tomadas > 2:
            piedras_tomadas = int(input(f"{jug2}, ingresa 1 o 2: "))
        pila_piedras -= piedras_tomadas
    
    # Determina el ganador dependiendo del valor en turno.
    # Devuelve el nombre del ganador.
    if turno == jug1:
        return jug2
    else:
        return jug1

def juego_PvC(jug1):
    """Ejecuta el modo de juego jugador vs computador."""
    pila_piedras = 20
    while pila_piedras > 0:
        # Turno del jugador 1
        print(f"\nHay {pila_piedras} piedras disponibles.")
        turno = jug1
        piedras_tomadas = int(input(f"\n{jug1}, ¿quieres tomar 1 o 2 piedras? "))
        
        # Limita la cantidad de piedras tomadas cuando sólo queda una.
        while pila_piedras == 1 and piedras_tomadas == 2:
            piedras_tomadas = int(input(f"Lo siento, {jug1}. Sólo hay 1 piedra disponible. "))

        while piedras_tomadas < 1 or piedras_tomadas > 2:
            piedras_tomadas = int(input(f"{jug1}, ingresa 1 o 2: "))
        pila_piedras -= piedras_tomadas
        # Si el jugador 1 es el último en tomar una piedra, el ciclo se interrumpe
        # para evitar que el computador tome piedras.
        if pila_piedras == 0:
            break

        # Turno del computador
        print(f"\nHay {pila_piedras} piedras disponibles.")
        turno = 'computador'
        # Toma un número aleatorio de piedras entre 1 y 2.
        piedras_tomadas = random.randint(1, 2)
        
        # Se asegura la victoria de la computadora si existe la posibilidad
        if pila_piedras == 3:
            piedras_tomadas = 2
        elif pila_piedras == 2:
            piedras_tomadas = 1
        
        # Si sólo queda una piedra, se limita la elección del computador a una sola piedra.
        if pila_piedras == 1:
            piedras_tomadas = 1
        
        print(f"\nComputador ha tomado {piedras_tomadas} piedras.")
        pila_piedras -= piedras_tomadas
    
    # Determina el ganador dependiendo del valor en turno.
    # Devuelve el nombre del ganador.
    if turno == jug1:
        return 'computador'
    else:
        return jug1

def fin_juego(ganador, jug1):
    # Imprime un mensaje personalizado dependiendo del modo de juego
    if ganador == 'computador':
        print(f"\nLo siento, {jug1}. Has perdido.")
    else:
        print(f"\n¡Felicitaciones, {ganador}! ¡Has ganado!")

    continuacion = input("\n¿Volver a jugar?\nIngresa 'y' para volver a jugar o 'n' para salir: ")
    while continuacion not in OPS_FINAL:
        continuacion = input("Ingresa una opción válida.\nIngresa 'y' para volver a jugar o 'n' para salir: ")
    
    if continuacion.lower() == 'y':
        return True
    else:
        return False

# Ejecución del programa mientras el usuario quiera continuar jugando.
reinicio = True
while reinicio == True:
    reinicio = main()

print("\nGracias por jugar Nimm.")
print("Creado por J. Sebastián Beltrán.")
print("Más código en https://github.com/JSebas98")