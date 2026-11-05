---
id: L08
materia: M07
orden: 8
titulo: 'Pilas, colas y cierre P1 parcial'
horas: 5
semana: 2
lectura: Repaso LIFO/FIFO y checklist P1 parcial
evidencia: README sección LIFO/FIFO + bitácora semana 2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 pide lista, pila, cola y hash. Hoy cierras la mitad LIFO/FIFO con
      documentación clara.


      **Objetivo de esta lección:** Dejar documentado el uso de
      stack/queue/deque, bitácora de semana 2 y suite verde antes de hash.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist de archivos
    xp: 10
    cuerpo: |-
      ```bash
      ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
      npm test
      ```

      Arregla fallos antes de documentar.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Sección README
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m07-estructuras
      git commit -m "docs(m07): cierre semana 2 pilas y colas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pilas, colas y cierre P1 parcial», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pilas, colas y cierre
          P1 parcial
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

      `ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts`
    comandoEsperado:
      - ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
      - npm test
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: ls src/stack.ts src/queue.ts src/deque.ts
      src/singly-linked-list.ts
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
          Dejar documentado el uso de stack/queue/deque, bitácora de semana 2 y
          suite verde antes de hash.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Export barrel
    xp: 10
    cuerpo: >-
      `src/index.ts` reexporta Stack, Queue, Deque, listas, DynamicArray.
      Verifica `npm run build` si tienes `tsc`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        README tiene sección “LIFO / FIFO / Deque” con cuándo usar cada una
        (tabla o bullets).
      - '`bitacora/semana-02.md` + `npm test` verde para stack/queue/deque.'
      - 'Commit `docs(m07): cierre semana 2 pilas y colas`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Pilas, colas y cierre P1 parcial

**~5.0 h · Semana 2**

P1 pide lista, pila, cola y hash. Hoy cierras la mitad LIFO/FIFO con documentación clara.

## Objetivo

Dejar documentado el uso de stack/queue/deque, bitácora de semana 2 y suite verde antes de hash.

## Pasos

### 1. Checklist de archivos (30 min)

```bash
ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
npm test
```

Arregla fallos antes de documentar.

### 2. Sección README (75 min)

Añade tabla: estructura | orden | ops tipicas | ejemplo producto (Agenda Ops: undo de cita, cola de espera, etc.).

### 3. Export barrel (45 min)

`src/index.ts` reexporta Stack, Queue, Deque, listas, DynamicArray. Verifica `npm run build` si tienes `tsc`.

### 4. Bitácora (40 min)

`bitacora/semana-02.md`: un bug que cazaste (p. ej. circular lleno/vacío) y cómo lo viste en un test.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre semana 2 pilas y colas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Cuándo pila vs cola vs deque | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. README tiene sección “LIFO / FIFO / Deque” con cuándo usar cada una (tabla o bullets).
2. `bitacora/semana-02.md` + `npm test` verde para stack/queue/deque.
3. Commit `docs(m07): cierre semana 2 pilas y colas`.

## Errores comunes

- README genérico sin mencionar tus archivos `src/*.ts`.
- Dejar ejercicios de paréntesis rotos.
- Marcar P1 “parcial” sin lista/pila/cola presentes.

## Siguiente

[L09 — Función hash y mapa conceptual](L09-funcion-hash-y-mapa-conceptual.md)
