---
id: L07
materia: M07
orden: 7
titulo: Deque y casos de uso
horas: 5
semana: 2
lectura: 'Deque: inserción/borrado en ambos extremos'
evidencia: Deque mínimo o cola doble + 3 tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un deque cubre patrones (ventana deslizante, BFS 0-1) que pila o cola
      solas no cubren bien.


      **Objetivo de esta lección:** Implementar un deque mínimo tipado y
      justificar un caso de uso real en 5–8 líneas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: API
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): deque y ejercicio"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): deque y ejercicio"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Deque y casos de uso», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Deque y casos de uso
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "feat(m07): deque y ejercicio"`
    comandoEsperado:
      - 'git commit -am "feat(m07): deque y ejercicio"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m07): deque y ejercicio"'
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
          Implementar un deque mínimo tipado y justificar un caso de uso real en
          5–8 líneas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests
    xp: 10
    cuerpo: >-
      Mezcla front/back; vaciar por un extremo tras llenar por el otro; size
      coherente.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `src/deque.ts` con `pushFront`/`pushBack`/`popFront`/`popBack` (o
        nombres equivalentes).
      - >-
        ≥3 tests + un caso de uso escrito (sliding window / undo-redo /
        palíndromo).
      - 'Commit `feat(m07): deque y ejercicio`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Deque y casos de uso

**~5.0 h · Semana 2**

Un deque cubre patrones (ventana deslizante, BFS 0-1) que pila o cola solas no cubren bien.

## Objetivo

Implementar un deque mínimo tipado y justificar un caso de uso real en 5–8 líneas.

## Pasos

### 1. API (20 min)

Decide nombres y anótalos en el README bajo “API semana 2”.

### 2. Implementación (90 min)

`src/deque.ts` sobre lista doble o buffer circular. Cuatro operaciones de extremo en O(1) amortizado/peor caso documentado.

### 3. Tests (45 min)

Mezcla front/back; vaciar por un extremo tras llenar por el otro; size coherente.

### 4. Caso de uso (60 min)

En `docs/casos-deque.md` (o sección README): elige **uno** — comprobar palíndromo con deque, o bosquejo de sliding-window máximo. Pseudocódigo + complejidad.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): deque y ejercicio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Deque / cola doble extremos | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/deque.ts` con `pushFront`/`pushBack`/`popFront`/`popBack` (o nombres equivalentes).
2. ≥3 tests + un caso de uso escrito (sliding window / undo-redo / palíndromo).
3. Commit `feat(m07): deque y ejercicio`.

## Errores comunes

- Deque que solo envuelve dos stacks sin documentar costos amortizados.
- Olvidar actualizar size en un extremo.
- Caso de uso genérico (“sirve para todo”) sin ejemplo concreto.

## Siguiente

[L08 — Pilas, colas y cierre P1 parcial](L08-pilas-colas-y-cierre-p1-parcial.md)
