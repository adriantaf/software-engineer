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
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Última semana: grafos unen discretas con redes, rutas y algoritmos.
      Empiezas con el modelo y un ejemplo concreto.


      **Objetivo de esta lección:** Definir grafo `G=(V,E)` (dirigido o no según
      elijas); grado, camino, ciclo, grafo completo; modelar un problema pequeño
      como grafo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Apuntes
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Dibujo y JSON
    xp: 10
    cuerpo: >-
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


      Elige un grafo de **5–6** nodos (mapa de ciudad ficticia, dependencias de
      tareas, amistades). Dibuja a mano y escanea/foto opcional en `apuntes/` o
      describe aristas en texto. Crea
      `projects/m03-discretas/grafos/ejemplo.json`: Ajusta a tu dibujo. Lista
      grado de cada vértice **a mano** y verifica suma de grados = 2|E| (no
      dirigido).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Grafos — modelo y terminología», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: '`grafos.md` con definiciones y grados calculados para `ejemplo.json`.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Grafos — modelo y
          terminología
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Aristas duplicadas sin documentar
      multigrafo."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Definir grafo `G=(V,E)` (dirigido o no según elijas); grado, camino,
          ciclo, grafo completo; modelar un problema pequeño como grafo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Modelado
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
