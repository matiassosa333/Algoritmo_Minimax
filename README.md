# 🐱 Gato vs Ratón con Minimax

## 🧠 Descripción

Este proyecto implementa un simulador de persecución entre un gato y un ratón en un tablero bidimensional utilizando el algoritmo Minimax.

El objetivo es modelar un entorno donde dos agentes inteligentes toman decisiones opuestas:

- El gato intenta **minimizar la distancia** para atrapar al ratón.
- El ratón intenta **maximizar su distancia** para escapar.

Ambos utilizan Minimax, simulando futuros posibles y tomando decisiones basadas en una heurística.

---

## ⚙️ Qué se implementó

- Tablero bidimensional (matriz)
- Movimiento en 4 direcciones (arriba, abajo, izquierda, derecha)
- Representación de estados mediante posiciones `(fila, columna)`
- Simulación de movimientos sin modificar el estado real
- Heurística basada en distancia Manhattan
- Algoritmo Minimax con profundidad limitada
- Sistema de turnos (ratón → gato)
- IA vs IA (ambos agentes toman decisiones inteligentes)
- Condición de finalización:
  - Captura del ratón
  - Límite de turnos (escape)

---

## 🧠 Lógica de IA

El sistema se basa en un modelo de **juego adversarial de suma cero**:

- El gato actúa como **jugador MAX** (busca el mayor valor posible)
- El ratón actúa como **jugador MIN** (busca el menor valor posible)

Cada estado del juego se evalúa mediante una función heurística:

```python
puntaje = -distancia(gato, raton)
