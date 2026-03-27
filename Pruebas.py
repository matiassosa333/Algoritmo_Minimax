#Variables iniciales para definir el tamaño del mundo
fila = 5
columna = 5

#Despues una estructura que sera nuestra tabla
tablero = []


#creamos las filas y columnas (lista en lista)
for i in range(fila): #Primer bucle que va a generar la fila vacia por la cantidad de range(fila)
    fila = []
    for j in range(columna): #bucle dentro del bucle anterior para llenar la fila con elementos y la cantidad es range(columna)
        fila.append(".") # agrega un elemento a la lista que seria lo que va dentro del parentesis, en este caso un .
    tablero.append(fila) # mete la fila dentro del tablero


#============================POSICIONES========================



gato = (0,0) #estamos ubicando al gato en fila 0 columna 0 y se usa tupla porque esto no se necesita modificar
raton = (2,2) # ubicamos al raton en el centro


#Dibujamos al gato en el tablero
tablero[gato[0]][gato[1]] = "G" #aca python lee que el indice 0 es el primer elemento y el indice 1 es segundo entonces primer valor fila y segundo la columna
tablero[raton[0]][raton[1]] = "R" #aca lo mismo pero con el raton

#agregamos movimiento con un ejemplo derecha
mov = (0, 1) #la fila no cambia, se agrega +1 a la columna (avanza derecha)

#borramos posicion anterior
tablero[raton[0]][raton[1]] = "." 

#una vez borrada se calcula la nueva posición
nueva_fila = raton[0] + mov[0]
nueva_columna = raton[1] + mov[1] #formula para posicion + movimiento

#una vez ejecutada el nuevo movimiento actualizamos su nueva posicion
raton = (nueva_fila, nueva_columna) 

#dibujamos la nueva posicion
tablero[raton[0]][raton[1]] = "R"


for fila in tablero: #recorre el cada fila en el tablero
    print(" ".join(fila)) #caracter espacio en string mas .join para unir los elementos con el caracter

#obs: aca se mueven sin limites


#=====================Limites================
# movimiento (ejemplo: derecha)
mov = (0, 1)

# calcular nueva posición
nueva_fila = raton[0] + mov[0]
nueva_col = raton[1] + mov[1]


# validar límites
if 0 <= nueva_fila < fila and 0 <= nueva_col < columna: #la nueva fila no puede ser menor o igual que 0 ni tampoco mayor que mi fila de "mundo"/ lo mismo con la nueva columna respectivamente
    
    # borrar posición anterior
    tablero[raton[0]][raton[1]] = "."

    # actualizar posición del ratón
    raton = (nueva_fila, nueva_col)

    # dibujar nueva posición
    tablero[raton[0]][raton[1]] = "R"
else:  #si no se cumple entonces que mande un error
    print("Movimiento inválido: fuera del tablero")


#================Movimiento manual en funcion================


filas = 5
columnas = 5

tablero = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(".")
    tablero.append(fila)

gato = (0, 0)
raton = (2, 2)

tablero[gato[0]][gato[1]] = "G"
tablero[raton[0]][raton[1]] = "R"


def mover_raton(tablero, raton, mov, filas, columnas): #Funcion con parametros tablero: para borrar y dibujar, raton: para ubicarle, mov: saber donde mover, filas y columnas: para los limites
    nueva_fila = raton[0] + mov[0]
    nueva_col = raton[1] + mov[1]

    if 0 <= nueva_fila < filas and 0 <= nueva_col < columnas:
        tablero[raton[0]][raton[1]] = "."
        raton = (nueva_fila, nueva_col)
        tablero[raton[0]][raton[1]] = "R"
    else:
        print("Movimiento inválido: fuera del tablero")

    return raton #devolvemos el valor de raton a quien llamo esta funcion


mov = (1, 0) #aca elegimos el movimiento
raton = mover_raton(tablero, raton, mov, filas, columnas) #aca ya se llama a la funcion teniendo el movimiento


#========================Funcion para mostrar tablero mas simple=======================
def mostrar_tablero(tablero):
    for fila in tablero:
        print(''.join(fila))


#================Implementar un loop para que (while)======================
movimientos = [(0,1), (1,0), (0,-1), (-1,0)] #nuestra lista de movimientos (derecha,abajo,izquierda,arriba)

contador = 0 #variable para controlar cuantas veces se ejecuta el loop

while contador < 5: #para repetir 5 veces 
    mov = movimientos[contador % 4] # % es un modulo (resto de division) 

    raton = mover_raton(tablero, raton, mov, filas, columnas)

    mostrar_tablero(tablero)
    print("------")

    contador += 1 #importante si no el loop nunca termina, como las vidas

#===========================Ia simple del gato==============================
def obtener_movimientos_validos(posicion, filas, columnas): #una funcion que va obtener los movimientos validos
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #variable movimientos para ver las direcciones permitidas guardadas en lista
    movimientos_validos = [] #lista vacia para guardar movimientos que si se pueden

    for mov in movimientos: #para recorrer los movimientos posibles
        nueva_fila = posicion[0] + mov[0]
        nueva_columna = posicion[1] + mov[1]

        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            movimientos_validos.append(mov) #si cumple guardamos el valor

    return movimientos_validos


def distancia_manhattan(pos1, pos2): #esta segunda funcion mide tan lejos esta una posicion de otra 
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) #abs convierte a valor absoluto


def decidir_movimiento_gato(gato, raton, filas, columnas): #esta funcion es la ia simple, va a recibir las posiciones, etc
    movimientos_validos = obtener_movimientos_validos(gato, filas, columnas) #llamamos funcion anterior de movimientos permitidos

    mejor_movimiento = None #variable para almacenar el mejor movimiento posible sin datos con none
    mejor_distancia = float("inf") #la mejor distancia es con float(inf) que significa infinito de inicio asi cualquier distancia real va a ser menor siempre

    for mov in movimientos_validos: #recorremos movimiento del gato para ver cual conviene
        nueva_posicion = (gato[0] + mov[0], gato[1] + mov[1]) #simulamos movimiento, aun no movemos de verdad
        distancia = distancia_manhattan(nueva_posicion, raton) #calculamos que tan cerca quedaria el gato con esa nueva posicion para recortar distancia

        if distancia < mejor_distancia: #condicion que si la distancia deja al gato más cerca que la mejor jugada encontrada hasta ahora..
            mejor_distancia = distancia #se actualiza la distancia...
            mejor_movimiento = mov #y guardamos el movimiento...

    return mejor_movimiento #hecha la funcion ya lo podemos llamar

#===================Funcion evaluacion======================
#sirve para evaluar el estado de juego y convertir en numero, el numero sirve para comparar opciones. Antes solo se acercaba, con esto evalua mejores opciones
puntaje = -distancia #negativo para ver si es mejor o no en la evaluacion, ejemplo si el resultado es -1, es mejor que -5 por ejemplo, que en positivo seria al revez

def juego_terminado(gato, raton):
    return gato == raton # si los dos iguales (misma casilla) da positivo (true) sino devuelve false

def evaluar_estado(gato, raton):
    if juego_terminado(gato, raton):
        return 100 #si el juego termino 100 para el gato, un valor alto para que la ia ya sepa que es mejor eso que solo acercarse
    
    distancia = distancia_manhattan(gato, raton) #si no termino llamamos la funcion anterior para calcular la distancia 
    return -distancia # y devolvemos la distancia en negativo


#=========================Version diferente para valores positivos pero simple==================================
def evaluar_estado(gato, raton):
    if juego_terminado(gato, raton):
        return 100

    distancia = distancia_manhattan(gato, raton)
    return 10 - distancia

#=========================Funcion que solo calcula======================
def aplicar_movimiento(posicion, mov):
    nueva_fila=posicion[o] + mov[0]
    nueva_col=posicion[1] + mov[1]

    return (nueva_fila, nueva_col)#Devolvemos el valor pero no toca tablero ni modifica nada externo, sirve para "imaginar"

#=======================Ahora si entramos con la funcion de Minimax=========================
def minimax (gato, raton, profundidad, es_turno_gato, filas, columnas): #gato, raton: posiciones actuales; profundidad: cuántos pasos hacia adelante simulamos; es_turno_gato: True o False (quién juega); filas, columnas: límites del tablero

    #caso base
    if profundidad == 0 or juego_terminado(gato, raton): # cortamos si llegamos al límite de profundidad o el juego ya terminó
        return evaluar_estado(gato, raton) #número que representa qué tan bueno es el estado
    
    if es_turno_gato: #Turno del gato (MAX)
        mejor_valor = float("-inf") #se empieza con el peor valor asi cualquier cosa sera mejor

        movimientos = obtener_movimientos_validos(gato, filas, columnas) #generamos todos los movimientos posibles del gato

        for mov in movimientos: #se prueba cada movimiento
            nuevo_gato = aplicar_movimiento(gato, mov) #aca solo simulamos no se modifica nada

            valor = minimax(nuevo_gato, raton, profundidad -1, False) #volvemos al minimax, le toca al raton(false) y reducimos la profundidad

            if valor > mejor_valor: 
                mejor_valor=valor #condicionamos para que el gato elija el mayor valor

        return mejor_valor # y lo devolvemos
    else: #Turno del raton (min)
        peor_valor= float ("inf")#empezamos con el peor valor para poder minimizar

        movimientos = obtener_movimientos_validos(raton, filas, columnas)# se genera el movimiento del raton

        for mov in movimientos: #se prueba cada uno
            nuevo_raton = aplicar_movimiento (raton, mov)#luego se simula

            valor = minimax(gato, nuevo_raton, profundidad -1, True, filas, columnas)
            
            if valor < peor_valor:
                peor_valor = valor #el raton elige el peor valor para el gato
        
        return peor_valor


#=================== Funcion para ejecutar el mejor movimiento====================
def mejor_movimiento_minimax(gato, raton, profundidad, filas, columnas):
    mejor_valor = float("-inf")
    mejor_mov = None

    movimientos = obtener_movimientos_validos(gato, filas, columnas)

    for mov in movimientos:
        nuevo_gato = aplicar_movimiento (gato, mov)

        valor= minimax(nuevo_gato, raton, profundidad -1, False, filas, columnas)

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

        return mejor_mov
    
#Ejemplo de como usar en el loop
mov = mejor_movimiento_minimax(gato, raton, 3, filas, columnas) #mientras mas profundidad mas inteligente pero mas lento y mayor consumo de stack
gato = mover_gato(tablero, gato, mov, filas, columnas)