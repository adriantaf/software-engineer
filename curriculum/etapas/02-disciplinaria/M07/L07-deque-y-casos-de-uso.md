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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar un deque mínimo tipado y justificar un caso de
      uso real en 5–8 líneas.


      Un deque cubre patrones (ventana deslizante, BFS 0-1) que pila o cola
      solas no cubren bien.
  - id: s2
    tipo: ejemplo
    titulo: 1. API
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): deque y ejercicio"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Deque y casos de uso" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: Deque mínimo o cola doble + 3 tests
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "feat(m07): deque y ejercicio"`
    comandoEsperado:
      - 'git commit -am "feat(m07): deque y ejercicio"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m07): deque y ejercicio"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar un deque mínimo tipado y justificar un caso de uso real en
          5–8 líneas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
      `src/deque.ts` sobre lista doble o buffer circular. Cuatro operaciones de
      extremo en O(1) amortizado/peor caso documentado.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
