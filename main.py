while True:
    print("Hola, bienvenido al juego de Mario!")
    print("elija un jugador para comenzar")
    print("1. Jugar con Mario")
    print("2. Jugar con Luigi")

    opcion = input("Ingrese el número del jugador")

    if opcion == "1":
        from Personajes.Mario import Mario
        jugador = Mario("Mario", posicionX=0, posicionY=0, vidas=3)
        print(f"{jugador._Personaje__nombre} ha sido seleccionado.")

    elif opcion == "2":
        from Personajes.Luigi import Luigi
        jugador = Luigi("Luigi", vidas=3, posicionX=0, posicionY=0)
        print(f"{jugador._Personaje__nombre} ha sido seleccionado.")

    else:
        print("Opción no válida. Por favor, elija 1 o 2.")
        continue

    print("¡Jugador seleccionado con éxito!")
    print("¡Comienza la aventura!")

    from Personajes.KoopaTroopa import KoopaTroopa
    enemigo = KoopaTroopa("Koopa Troopa", posicionX=0, posicionY=0, vidas=2)

    print(f"Un enemigo ha aparecido: {enemigo._Personaje__nombre} en la posición ({enemigo._posicionX}, {enemigo._posicionY})")

    while True:

        print("¿Qué quieres hacer?")
        print("1. Lanzar un poder especial")
        print("2. Salir del juego")

        accion = input("Ingrese el número de la acción: 1 o 2: ")

        if accion == "1":
            if isinstance(jugador, Mario):
                jugador.lanzar_fuego()
            elif isinstance(jugador, Luigi):
                jugador.lanzar_hielo()
            else:
                print("Acción no válida.")
                break

        
        elif accion == "2":
            print("Saliendo del juego...")
            break

        else:
            print("Opción no válida. Por favor, elija 1 o 2.")

        enemigo.recibir_dano(1)

        if enemigo._vidas <= 0:
            print(f"{enemigo._Personaje__nombre} ha sido derrotado.")
            break
        else:
            enemigo.atacar(jugador)
            if jugador._vidas <= 0:
                print(f"{jugador._Personaje__nombre} ha sido derrotado. Fin del juego.")
                break
        print(f"{jugador._Personaje__nombre} tiene {jugador._vidas} vidas restantes.")
        print(f"{enemigo._Personaje__nombre} tiene {enemigo._vidas} vidas restantes.")
        print("¡Turno del enemigo!")
        enemigo.caminar()
        enemigo.caparazon()
        print(f"{enemigo._Personaje__nombre} se prepara para atacar.")
        print("¡Turno del jugador!")
        print(f"{jugador._Personaje__nombre} se prepara para atacar.")
        print("¡El juego continúa!")  

        from Personajes.Goomba import Goomba
    enemigo = Goomba("Goomba", posicionX=1, posicionY=1, vidas=1)
    print(f"Un enemigo ha aparecido: {enemigo._Personaje__nombre} en la posición ({enemigo._posicionX}, {enemigo._posicionY})")

    while True:

        print("Presione el siguiente boton")
        print("1. Saltar")
        accion = input("Ingrese el número de la acción: ")

        if accion == "1":
            print(f"{jugador._Personaje__nombre} salta.")
            print(f"Goomba ha sido aplastado!")
            print(f"{jugador._Personaje__nombre} ha ganado.")
            break
        else:
                print("Acción no válida.")
                break
            