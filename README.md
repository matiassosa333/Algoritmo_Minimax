# 🐱 Gato vs Ratón con Minimax

## 🧠 Descripción

Este proyecto implementa un simulador de persecución entre un gato y un ratón en un tablero bidimensional utilizando el algoritmo Minimax.

El gato utiliza inteligencia artificial para anticipar los movimientos del ratón y minimizar la distancia hasta capturarlo, mientras que el ratón puede comportarse de forma aleatoria o inteligente dependiendo de la configuración.

---

## ⚙️ Qué se implementó

- Tablero bidimensional (matriz)
- Movimiento en 4 direcciones (arriba, abajo, izquierda, derecha)
- Simulación de estados sin modificar el entorno real
- Función heurística basada en distancia Manhattan
- Algoritmo Minimax con profundidad limitada
- Sistema de turnos (ratón → gato)
- Condición de finalización (captura del ratón)

---

## 🧠 Lógica de IA

- El gato actúa como jugador MAX (maximiza el puntaje)
- El ratón actúa como jugador MIN (minimiza el puntaje)
- Se utiliza una heurística simple basada en distancia:
  
  - Menor distancia → mejor para el gato
  - Mayor distancia → mejor para el ratón

---

## ⚠️ Limitaciones

- La heurística es básica (solo considera distancia)
- La profundidad limitada puede generar decisiones subóptimas
- Pueden ocurrir ciclos o bucles en el comportamiento
- No se implementó poda alpha-beta

---

## 💡 Aprendizajes ("Aha moment")

- Entender cómo una IA puede "simular el futuro" usando recursividad
- Comprender la diferencia entre estado real y estado simulado
- Ver cómo una heurística simple puede guiar decisiones complejas
- Darse cuenta de que Minimax no es perfecto sin profundidad suficiente

---

## 🚀 Posibles mejoras

- Implementar alpha-beta pruning
- Mejorar la heurística (zonas, bloqueos, escape)
- Añadir obstáculos en el tablero
- Permitir IA vs IA
- Agregar interfaz interactiva más avanzada

---

## 🛠️ Tecnologías

- Python (sin librerías externas)
