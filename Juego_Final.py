FILAS = 5
COLUMNAS = 5
MAX_TURNOS = 30
PROFUNDIDAD = 3


def crear_tablero(filas, columnas):
    return [["." for _ in range(columnas)] for _ in range(filas)]


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()


def limpiar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = "."


def colocar_personajes(tablero, gato, raton):
    limpiar_tablero(tablero)
    tablero[gato[0]][gato[1]] = "G"
    tablero[raton[0]][raton[1]] = "R"


def obtener_movimientos_validos(posicion, filas, columnas):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [
        mov for mov in movimientos
        if 0 <= posicion[0] + mov[0] < filas and 0 <= posicion[1] + mov[1] < columnas
    ]


def aplicar_movimiento(posicion, movimiento):
    return (posicion[0] + movimiento[0], posicion[1] + movimiento[1])


def distancia_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def juego_terminado(gato, raton):
    return gato == raton


def evaluar_estado(gato, raton):
    if juego_terminado(gato, raton):
        return 100
    return -distancia_manhattan(gato, raton)


def minimax(gato, raton, profundidad, es_turno_gato, filas, columnas):
    if profundidad == 0 or juego_terminado(gato, raton):
        return evaluar_estado(gato, raton)

    if es_turno_gato:
        mejor = float("-inf")
        for mov in obtener_movimientos_validos(gato, filas, columnas):
            valor = minimax(
                aplicar_movimiento(gato, mov),
                raton,
                profundidad - 1,
                False,
                filas,
                columnas
            )
            mejor = max(mejor, valor)
        return mejor
    else:
        peor = float("inf")
        for mov in obtener_movimientos_validos(raton, filas, columnas):
            valor = minimax(
                gato,
                aplicar_movimiento(raton, mov),
                profundidad - 1,
                True,
                filas,
                columnas
            )
            peor = min(peor, valor)
        return peor


def mejor_movimiento_gato(gato, raton, profundidad, filas, columnas):
    mejor_valor = float("-inf")
    mejor_mov = None

    for mov in obtener_movimientos_validos(gato, filas, columnas):
        valor = minimax(
            aplicar_movimiento(gato, mov),
            raton,
            profundidad - 1,
            False,
            filas,
            columnas
        )

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_mov


def mejor_movimiento_raton(gato, raton, profundidad, filas, columnas):
    peor_valor = float("inf")
    mejor_mov = None

    for mov in obtener_movimientos_validos(raton, filas, columnas):
        valor = minimax(
            gato,
            aplicar_movimiento(raton, mov),
            profundidad - 1,
            True,
            filas,
            columnas
        )

        if valor < peor_valor:
            peor_valor = valor
            mejor_mov = mov

    return mejor_mov


def ejecutar_turno(gato, raton):
    raton = aplicar_movimiento(
        raton,
        mejor_movimiento_raton(gato, raton, PROFUNDIDAD, FILAS, COLUMNAS)
    )

    if juego_terminado(gato, raton):
        return gato, raton, True

    gato = aplicar_movimiento(
        gato,
        mejor_movimiento_gato(gato, raton, PROFUNDIDAD, FILAS, COLUMNAS)
    )

    return gato, raton, juego_terminado(gato, raton)


def main():
    tablero = crear_tablero(FILAS, COLUMNAS)

    gato = (0, 0)
    raton = (FILAS - 1, COLUMNAS - 1)

    for turno in range(1, MAX_TURNOS + 1):
        colocar_personajes(tablero, gato, raton)

        print(f"Turno {turno}")
        mostrar_tablero(tablero)

        gato, raton, terminado = ejecutar_turno(gato, raton)

        if terminado:
            colocar_personajes(tablero, gato, raton)
            mostrar_tablero(tablero)
            print("El gato atrapó al ratón.")
            return

    colocar_personajes(tablero, gato, raton)
    mostrar_tablero(tablero)
    print("Empate o escape del ratón.")


if __name__ == "__main__":
    main()