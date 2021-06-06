import random

MODOS_JUEGO = ['p', 'c']
OPS_FINAL = ['y', 'n']

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
        while len(jug1) == 0:
            jug1 = input("Jugador 1, ingresa un nombre válido: ") 
        jug2 = input("Jugador 2, ingresa tu nombre: ")
        while len(jug2) == 0:
            jug2 = input("Jugador 2, ingresa un nombre válido: ")

        return jug1, jug2
    else:
        jug1 = input("Jugador, ingresa tu nombre: ")
        while len(jug1) == 0:
            jug1 = input("Jugador 1, ingresa un nombre válido: ")
        
        return jug1

def juego_PvP(jug1, jug2):
    """Ejecuta el modo de juego jugador vs jugador."""
    pila_piedras = 20
    activo = True
    while activo:
        # Turno del jugador 1
        print(f"\nHay {pila_piedras} piedras disponibles.")
        turno = jug1
        while turno == jug1:
            try:
                piedras_tomadas = int(input(f"\n{jug1}, ¿quieres tomar 1 o 2 piedras? "))
                # Se asegura de que el input sea válido
                if piedras_tomadas < 1 or piedras_tomadas > 2:
                    print("Valor no válido. Sólo puedes tomar 1 o 2 piedras.")
                    raise ValueError
                # Limita la cantidad de piedras tomadas cuando sólo queda una.
                elif pila_piedras == 1 and piedras_tomadas == 2:
                    print(f"Lo siento, {jug1}. Sólo hay 1 piedra disponible.")
                    raise ValueError
                else:
                    turno = jug2
                    pila_piedras -= piedras_tomadas
                # Si el jugador 1 es el último en tomar una piedra, el ciclo se interrumpe
                # para evitar que se pida al jugador 2 tomar piedras.
                    if pila_piedras == 0:
                        activo = False
                
            except ValueError:
                continue
        
        print(f"\nHay {pila_piedras} piedras disponibles.")
        # Turno del jugador 2
        while turno == jug2 and activo == True:
            try:
                piedras_tomadas = int(input(f"\n{jug2}, ¿quieres tomar 1 o 2 piedras? "))
                # Se asegura de que el input sea válido
                if piedras_tomadas < 1 or piedras_tomadas > 2:
                    print("Valor no válido. Sólo puedes tomar 1 o 2 piedras.")
                    raise ValueError
                # Limita la cantidad de piedras tomadas cuando sólo queda una.
                elif pila_piedras == 1 and piedras_tomadas == 2:
                    print(f"Lo siento, {jug2}. Sólo hay 1 piedra disponible.")
                    raise ValueError
                else:
                    turno = jug1
                    pila_piedras -= piedras_tomadas
                    # Si el jugador 2 es el último en tomar una piedra, el ciclo se interrumpe
                    # y termina el programa.
                    if pila_piedras == 0:
                        activo = False
            except ValueError:
                continue
    
    # Determina el ganador dependiendo del valor en turno.
    # Devuelve el nombre del ganador.
    if turno == jug1:
        return jug1
    else:
        return jug2

def juego_PvC(jug1):
    """Ejecuta el modo de juego jugador vs computador."""
    pila_piedras = 20
    activo = True
    while activo:
        # Turno del jugador 1
        print(f"\nHay {pila_piedras} piedras disponibles.")
        turno = jug1
        while turno == jug1:
            try:
                piedras_tomadas = int(input(f"\n{jug1}, ¿quieres tomar 1 o 2 piedras? "))
                # Se asegura de que el input sea válido
                if piedras_tomadas < 1 or piedras_tomadas > 2:
                    print("Valor no válido. Sólo puedes tomar 1 o 2 piedras.")
                    raise ValueError
                # Limita la cantidad de piedras tomadas cuando sólo queda una.
                elif pila_piedras == 1 and piedras_tomadas == 2:
                    print(f"Lo siento, {jug1}. Sólo hay 1 piedra disponible.")
                    raise ValueError
                else:
                    turno = 'computador'
                    pila_piedras -= piedras_tomadas
                # Si el jugador 1 es el último en tomar una piedra, el ciclo se interrumpe
                # para evitar que se pida al jugador 2 tomar piedras.
                    if pila_piedras == 0:
                        activo = False
            except ValueError:
                continue

        # Turno del computador
        print(f"\nHay {pila_piedras} piedras disponibles.")
        if activo == False:
            break
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
            activo = False
        
        print(f"\nComputador ha tomado {piedras_tomadas} piedras.")
        pila_piedras -= piedras_tomadas
        turno = jug1
    
    # Determina el ganador dependiendo del valor en turno.
    # Devuelve el nombre del ganador.
    if turno == 'computador':
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