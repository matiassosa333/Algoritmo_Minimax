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

for fila in tablero:
    print(" ".join(fila))

#========================Funcion para mostrar tablero mas simple=======================
def mostrar_tablero(tablero):
    for filas in tablero:
        print(''.join(filas))