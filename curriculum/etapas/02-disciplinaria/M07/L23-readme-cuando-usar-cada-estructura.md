---
id: L23
materia: M07
orden: 23
titulo: README cuándo usar cada estructura
horas: 5
semana: 6
lectura: Guía de selección de estructuras
evidencia: README guía de selección + API pública
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El proyecto útil es una librería documentada, no solo archivos sueltos.


      **Objetivo de esta lección:** Redactar la guía de selección y dejar la API
      pública exportada y testeada.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      npm test && npm run build
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Guía de selección
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m07): guia cuando usar cada estructura"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «README cuándo usar cada estructura», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de README cuándo usar cada
          estructura
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

      `npm test && npm run build`
    comandoEsperado:
      - npm test && npm run build
      - 'git commit -am "docs(m07): guia cuando usar cada estructura"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm test && npm run build'
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
          Redactar la guía de selección y dejar la API pública exportada y
          testeada.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: API y ejemplo
    xp: 10
    cuerpo: >-
      `src/index.ts` limpio. Bloque “Quick start” de 15 líneas en README
      importando Stack/HashMap/BST.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        README con guía “cuándo usar cada una” (todas las estructuras del
        curso).
      - '`src/index.ts` exporta la API pública; `npm test` verde.'
      - 'Commit `docs(m07): guia cuando usar cada estructura`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L23 — README cuándo usar cada estructura

**~5.0 h · Semana 6**

El proyecto útil es una librería documentada, no solo archivos sueltos.

## Objetivo

Redactar la guía de selección y dejar la API pública exportada y testeada.

## Pasos

### 1. Inventario (30 min)

Lista clases en `src/` y márcalas P1/P2/P3.

### 2. Guía de selección (90 min)

En README: preguntas → estructura (¿acceso aleatorio? ¿LIFO? ¿prioridad? ¿prefijo? → “eso es M08”). Tabla resumen + enlace a `COMPLEJIDAD.md`.

### 3. API y ejemplo (60 min)

`src/index.ts` limpio. Bloque “Quick start” de 15 líneas en README importando Stack/HashMap/BST.

### 4. QA (30 min)

```bash
npm test && npm run build
```

### 5. Commit (15 min)

```bash
git commit -am "docs(m07): guia cuando usar cada estructura"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Árbol de decisión: acceso, orden, prioridad, grafo | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. README con guía “cuándo usar cada una” (todas las estructuras del curso).
2. `src/index.ts` exporta la API pública; `npm test` verde.
3. Commit `docs(m07): guia cuando usar cada estructura`.

## Errores comunes

- Guía genérica de Internet sin tus nombres de clase.
- Olvidar heap/grafo en la tabla.
- README sin cómo correr tests.

## Siguiente

[L24 — Cierre M07 y evidencias](L24-cierre-m07-y-evidencias.md)
