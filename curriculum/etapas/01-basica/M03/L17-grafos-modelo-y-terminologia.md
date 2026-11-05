---
id: L17
materia: M03
orden: 17
titulo: Grafos — modelo y terminología
horas: 2.5
semana: 5
lectura: 'Rosen Cap. 10.1–10.2 — grafos, aristas, grados, caminos, ciclos'
evidencia: apuntes/grafos.md + grafos/ejemplo.json (5–6 nodos) dibujado a mano
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir grafo `G=(V,E)` (dirigido o no según elijas); grado,
      camino, ciclo, grafo completo; modelar un problema pequeño como grafo.


      Última semana: grafos unen discretas con redes, rutas y algoritmos.
      Empiezas con el modelo y un ejemplo concreto.
  - id: s2
    tipo: ejemplo
    titulo: 1. Apuntes
    xp: 10
    cuerpo: |-
      ```json
      {
        "dirigido": false,
        "vertices": ["A", "B", "C", "D", "E"],
        "aristas": [
          ["A", "B"],
          ["A", "C"],
          ["B", "D"],
          ["C", "D"],
          ["D", "E"]
        ]
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Grafos — modelo y terminología" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: apuntes/grafos.md + grafos/ejemplo.json (5–6 nodos) dibujado a mano
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Aristas duplicadas sin documentar
      multigrafo."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Definir grafo `G=(V,E)` (dirigido o no según elijas); grado, camino,
          ciclo, grafo completo; modelar un problema pequeño como grafo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Dibujo y JSON
    xp: 10
    cuerpo: >-
      Elige un grafo de **5–6** nodos (mapa de ciudad ficticia, dependencias de
      tareas, amistades). Dibuja a mano y escanea/foto opcional en `apuntes/` o
      describe aristas en texto.


      Crea `projects/m03-discretas/grafos/ejemplo.json`:


      ```json

      {
        "dirigido": false,
        "vertices": ["A", "B", "C", "D", "E"],
        "aristas": [
          ["A", "B"],
          ["A", "C"],
          ["B", "D"],
          ["C", "D"],
          ["D", "E"]
        ]
      }

      ```


      Ajusta a tu dibujo. Lista grado de cada vértice **a mano** y verifica suma
      de grados = 2|E| (no dirigido).
  - id: s7
    tipo: explicacion
    titulo: 3. Modelado
    xp: 10
    cuerpo: >-
      Segundo mini-ejemplo en el apunte: traduce “prerrequisitos de cursos” a
      DAG dirigido (3–4 nodos).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`grafos.md` con definiciones y grados calculados para `ejemplo.json`.'
      - Existe `grafos/ejemplo.json` coherente con el dibujo.
      - Distingues camino de ciclo con un ejemplo en tu grafo.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — Grafos: modelo y terminología

**~2.5 h · Semana 5**

Última semana: grafos unen discretas con redes, rutas y algoritmos. Empiezas con el modelo y un ejemplo concreto.

## Objetivo

Definir grafo `G=(V,E)` (dirigido o no según elijas); grado, camino, ciclo, grafo completo; modelar un problema pequeño como grafo.

## Pasos

### 1. Apuntes (50 min)

`projects/m03-discretas/apuntes/grafos.md`:

- Vértices, aristas, adyacencia.
- Grafo simple vs multigrafo (mención).
- Grado en grafo no dirigido; grado entrante/saliente si es dirigido.
- Camino, ciclo, grafo conexo (definición).

### 2. Dibujo y JSON (50 min)

Elige un grafo de **5–6** nodos (mapa de ciudad ficticia, dependencias de tareas, amistades). Dibuja a mano y escanea/foto opcional en `apuntes/` o describe aristas en texto.

Crea `projects/m03-discretas/grafos/ejemplo.json`:

```json
{
  "dirigido": false,
  "vertices": ["A", "B", "C", "D", "E"],
  "aristas": [
    ["A", "B"],
    ["A", "C"],
    ["B", "D"],
    ["C", "D"],
    ["D", "E"]
  ]
}
```

Ajusta a tu dibujo. Lista grado de cada vértice **a mano** y verifica suma de grados = 2|E| (no dirigido).

### 3. Modelado (30 min)

Segundo mini-ejemplo en el apunte: traduce “prerrequisitos de cursos” a DAG dirigido (3–4 nodos).

### 4. Lectura Rosen (30 min)

Ejercicio de terminología del 10.1 en `grafos.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 10.1–10.2 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `grafos.md` con definiciones y grados calculados para `ejemplo.json`.
2. Existe `grafos/ejemplo.json` coherente con el dibujo.
3. Distingues camino de ciclo con un ejemplo en tu grafo.

## Errores comunes

- Aristas duplicadas sin documentar multigrafo.
- Confundir grafo dirigido con no dirigido al contar grados.
- JSON sin lista de vértices aislados (inclúyelos si existen).

## Siguiente

[L18 — Representación de grafos en TS](L18-representacion-de-grafos-en-ts.md)
