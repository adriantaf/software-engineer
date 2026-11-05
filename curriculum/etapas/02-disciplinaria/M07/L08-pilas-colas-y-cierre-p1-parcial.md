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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar documentado el uso de stack/queue/deque, bitácora de
      semana 2 y suite verde antes de hash.


      P1 pide lista, pila, cola y hash. Hoy cierras la mitad LIFO/FIFO con
      documentación clara.
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist de archivos
    xp: 10
    cuerpo: |-
      ```bash
      ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
      npm test
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Pilas, colas y cierre P1 parcial" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: README sección LIFO/FIFO + bitácora semana 2
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

      `ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts`
    comandoEsperado:
      - ls src/stack.ts src/queue.ts src/deque.ts src/singly-linked-list.ts
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: ls src/stack.ts src/queue.ts src/deque.ts
      src/singly-linked-list.ts
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar documentado el uso de stack/queue/deque, bitácora de semana 2 y
          suite verde antes de hash.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Sección README
    xp: 10
    cuerpo: >-
      Añade tabla: estructura | orden | ops tipicas | ejemplo producto (Agenda
      Ops: undo de cita, cola de espera, etc.).
  - id: s7
    tipo: explicacion
    titulo: 3. Export barrel
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
