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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar la guía de selección y dejar la API pública
      exportada y testeada.


      El proyecto útil es una librería documentada, no solo archivos sueltos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario
    xp: 10
    cuerpo: |-
      ```bash
      npm test && npm run build
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "README cuándo usar cada estructura" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: README guía de selección + API pública
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

      `npm test && npm run build`
    comandoEsperado:
      - npm test && npm run build
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm test && npm run build'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Redactar la guía de selección y dejar la API pública exportada y
          testeada.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Guía de selección
    xp: 10
    cuerpo: >-
      En README: preguntas → estructura (¿acceso aleatorio? ¿LIFO? ¿prioridad?
      ¿prefijo? → “eso es M08”). Tabla resumen + enlace a `COMPLEJIDAD.md`.
  - id: s7
    tipo: explicacion
    titulo: 3. API y ejemplo
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
