import random


FILAS = 5
COLUMNAS = 5
MAX_TURNOS = 30


def crear_tablero(filas, columnas):
    tablero = []

    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(".")
        tablero.append(fila)

    return tablero


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()


def colocar_personajes(tablero, gato, raton):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = "."

    tablero[gato[0]][gato[1]] = "G"
    tablero[raton[0]][raton[1]] = "R"


def obtener_movimientos_validos(posicion, filas, columnas):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    movimientos_validos = []

    for mov in movimientos:
        nueva_fila = posicion[0] + mov[0]
        nueva_columna = posicion[1] + mov[1]

        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            movimientos_validos.append(mov)

    return movimientos_validos


def aplicar_movimiento(posicion, mov):
    nueva_fila = posicion[0] + mov[0]
    nueva_columna = posicion[1] + mov[1]
    return (nueva_fila, nueva_columna)


def distancia_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def juego_terminado(gato, raton):
    return gato == raton


def evaluar_estado(gato, raton):
    if juego_terminado(gato, raton):
        return 100

    distancia = distancia_manhattan(gato, raton)
    return -distancia


def minimax(gato, raton, profundidad, es_turno_gato, filas, columnas):
    if profundidad == 0 or juego_terminado(gato, raton):
        return evaluar_estado(gato, raton)

    if es_turno_gato:
        mejor_valor = float("-inf")
        movimientos = obtener_movimientos_validos(gato, filas, columnas)

        for mov in movimientos:
            nuevo_gato = aplicar_movimiento(gato, mov)
            valor = minimax(nuevo_gato, raton, profundidad - 1, False, filas, columnas)

            if valor > mejor_valor:
                mejor_valor = valor

        return mejor_valor

    else:
        peor_valor = float("inf")
        movimientos = obtener_movimientos_validos(raton, filas, columnas)

        for mov in movimientos:
            nuevo_raton = aplicar_movimiento(raton, mov)
            valor = minimax(gato, nuevo_raton, profundidad - 1, True, filas, columnas)

            if valor < peor_valor:
                peor_valor = valor

        return peor_valor


def mejor_movimiento_gato(gato, raton, profundidad, filas, columnas):
    mejor_valor = float("-inf")
    mejor_mov = None
    movimientos = obtener_movimientos_validos(gato, filas, columnas)

    for mov in movimientos:
        nuevo_gato = aplicar_movimiento(gato, mov)
        valor = minimax(nuevo_gato, raton, profundidad - 1, False, filas, columnas)

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_mov


def movimiento_raton_random(raton, filas, columnas):
    movimientos = obtener_movimientos_validos(raton, filas, columnas)
    return random.choice(movimientos)


def mover_personaje(posicion, mov):
    return aplicar_movimiento(posicion, mov)


def main():
    tablero = crear_tablero(FILAS, COLUMNAS)

    gato = (0, 0)
    raton = (4, 4)

    turnos = 0

    while turnos < MAX_TURNOS:
        colocar_personajes(tablero, gato, raton)

        print(f"Turno {turnos + 1}")
        mostrar_tablero(tablero)

        mov_raton = movimiento_raton_random(raton, FILAS, COLUMNAS)
        raton = mover_personaje(raton, mov_raton)

        if juego_terminado(gato, raton):
            colocar_personajes(tablero, gato, raton)
            mostrar_tablero(tablero)
            print("El gato atrapó al ratón.")
            return

        mov_gato = mejor_movimiento_gato(gato, raton, 3, FILAS, COLUMNAS)
        gato = mover_personaje(gato, mov_gato)

        if juego_terminado(gato, raton):
            colocar_personajes(tablero, gato, raton)
            mostrar_tablero(tablero)
            print("El gato atrapó al ratón.")
            return

        turnos += 1

    colocar_personajes(tablero, gato, raton)
    mostrar_tablero(tablero)
    print("El ratón escapó por límite de turnos.")


main()