#vamos a hacer un tik tak toe

#vamos a crear una lista con los valores de las posiciones del tablero

tablero = ["-", "-", "-",
              "-", "-", "-",
                "-", "-", "-"]

#vamos a crear una variable para saber si el juego esta en marcha

juego_en_marcha = True

#vamos a crear una variable para saber quien es el ganador

ganador = None

#vamos a crear una variable para saber quien es el jugador actual

jugador_actual = "X"

#vamos a crear una funcion para mostrar el tablero

def mostrar_tablero():
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

#vamos a crear una funcion para jugar

def jugar():
    #mostramos el tablero
    mostrar_tablero()

    #mientras el juego este en marcha
    while juego_en_marcha:
        #manejamos el turno del jugador
        manejar_turno(jugador_actual)

        #comprobamos si el juego ha terminado
        comprobar_si_ha_terminado()

        #cambiamos al otro jugador
        cambiar_jugador()

    #el juego ha terminado
    if ganador == "X" or ganador == "O":
        print(ganador + " gano.")
    elif ganador == None:
        print("Empate.")

#vamos a crear una funcion para manejar el turno del jugador

def manejar_turno(jugador):
    print(jugador + "'s turno.")
    posicion = input("Elige una posicion del 1 al 9: ")

    valido = False
    while not valido:
        while posicion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            posicion = input("Elige una posicion del 1 al 9: ")

        posicion = int(posicion) - 1

        if tablero[posicion] == "-":
            valido = True
        else:
            print("No puedes ir ahi. Elige otra posicion.")

    tablero[posicion] = jugador

    mostrar_tablero()

#vamos a crear una funcion para comprobar si el juego ha terminado

def comprobar_si_ha_terminado():
    comprobar_si_ha_ganado()
    comprobar_si_hay_empate()

#vamos a crear una funcion para comprobar si ha ganado

def comprobar_si_ha_ganado():
    #establecemos las variables globales
    global ganador

    #comprobamos si hay alguna fila ganadora
    fila_ganadora = comprobar_filas()
    #comprobamos si hay alguna columna ganadora
    columna_ganadora = comprobar_columnas()
    #comprobamos si hay alguna diagonal ganadora
    diagonal_ganadora = comprobar_diagonales()
    if fila_ganadora:
        ganador = fila_ganadora
    elif columna_ganadora:
        ganador = columna_ganadora
    elif diagonal_ganadora:
        ganador = diagonal_ganadora
    else:
        ganador = None

#vamos a crear una funcion para comprobar si hay alguna fila ganadora

def comprobar_filas():
    #establecemos las variables globales
    global juego_en_marcha

    #comprobamos si hay alguna fila ganadora
    fila_1 = tablero[0] == tablero[1] == tablero[2] != "-"
    fila_2 = tablero[3] == tablero[4] == tablero[5] != "-"
    fila_3 = tablero[6] == tablero[7] == tablero[8] != "-"
    if fila_1 or fila_2 or fila_3:
        juego_en_marcha = False
    #devolvemos el ganador (X o O)
    if fila_1:
        return tablero[0]
    elif fila_2:
        return tablero[3]
    elif fila_3:
        return tablero[6]
    else:
        return None

#vamos a crear una funcion para comprobar si hay alguna columna ganadora

def comprobar_columnas():
    #establecemos las variables globales
    global juego_en_marcha

    #comprobamos si hay alguna columna ganadora
    columna_1 = tablero[0] == tablero[3] == tablero[6] != "-"
    columna_2 = tablero[1] == tablero[4] == tablero[7] != "-"
    columna_3 = tablero[2] == tablero[5] == tablero[8] != "-"
    if columna_1 or columna_2 or columna_3:
        juego_en_marcha = False
    #devolvemos el ganador (X o O)
    if columna_1:
        return tablero[0]
    elif columna_2:
        return tablero[1]
    elif columna_3:
        return tablero[2]
    else:
        return None

#vamos a crear una funcion para comprobar si hay alguna diagonal ganadora

def comprobar_diagonales():
    #establecemos las variables globales
    global juego_en_marcha

    #comprobamos si hay alguna diagonal ganadora
    diagonal_1 = tablero[0] == tablero[4] == tablero[8] != "-"
    diagonal_2 = tablero[2] == tablero[4] == tablero[6] != "-"
    if diagonal_1 or diagonal_2:
        juego_en_marcha = False
    #devolvemos el ganador (X o O)
    if diagonal_1:
        return tablero[0]
    elif diagonal_2:
        return tablero[2]
    else:
        return None

#vamos a crear una funcion para comprobar si hay empate

def comprobar_si_hay_empate():
    #establecemos las variables globales
    global juego_en_marcha

    if "-" not in tablero:
        juego_en_marcha = False
        return True
    else:
        return False

#vamos a crear una funcion para cambiar al otro jugador

def cambiar_jugador():
    #establecemos las variables globales
    global jugador_actual

    #si el jugador actual es X, cambiamos a O
    if jugador_actual == "X":
        jugador_actual = "O"
    #si el jugador actual es O, cambiamos a X
    elif jugador_actual == "O":
        jugador_actual = "X"

#vamos a crear una funcion para reiniciar el juego

def reiniciar_juego():
    #establecemos las variables globales
    global tablero
    global juego_en_marcha
    global jugador_actual
    global ganador

    #reiniciamos el tablero
    tablero = ["-", "-", "-",
              "-", "-", "-",
                "-", "-", "-"]

    #reiniciamos las variables
    juego_en_marcha = True
    jugador_actual = "X"
    ganador = None

#iniciamos el juego

jugar()