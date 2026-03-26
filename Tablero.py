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

for fila in tablero: #recorre el cada fila en el tablero
    print(" ".join(fila)) #caracter espacio en string mas .join para unir los elementos con el caracter
