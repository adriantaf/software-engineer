---
id: L24
materia: M07
orden: 24
titulo: Cierre M07 y evidencias
horas: 5
semana: 6
lectura: Checklist de dominio y evidencias en git
evidencia: bitácora + checklist dominio + progress
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar evidencia P1–P3 + proyecto enlazada desde bitácora de
      cierre y el README.


      Si no está en git con checklist, no cuenta. Hoy cierras la materia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist con rutas
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m07-estructuras && npm test
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Cierre M07 y evidencias" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: bitácora + checklist dominio + progress
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

      `cd projects/m07-estructuras && npm test`
    comandoEsperado:
      - cd projects/m07-estructuras && npm test
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: cd projects/m07-estructuras && npm test'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Dejar evidencia P1–P3 + proyecto enlazada desde bitácora de cierre y
          el README.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Criterios de dominio
    xp: 10
    cuerpo: >-
      Grábate o escribe respuesta de 3 minutos: “¿cuándo un hash gana a un
      árbol?”. Pega el outline en la bitácora.
  - id: s7
    tipo: ejemplo
    titulo: 3. Regresión final
    xp: 10
    cuerpo: |-
      ```bash
      cd projects/m07-estructuras && npm test
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con
        rutas de archivo.
      - Suite verde y README de selección presente.
      - 'Commit `docs(m07): cierre materia y evidencias`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L24 — Cierre M07 y evidencias

**~5.0 h · Semana 6**

Si no está en git con checklist, no cuenta. Hoy cierras la materia.

## Objetivo

Dejar evidencia P1–P3 + proyecto enlazada desde bitácora de cierre y el README.

## Pasos

### 1. Checklist con rutas (60 min)

`bitacora/cierre-m07.md`:

- P1: rutas a lista/pila/cola/hash + tests
- P2: bst + recorridos
- P3: `bench/RESULTADOS.md`
- Proyecto: guía README

### 2. Criterios de dominio (50 min)

Grábate o escribe respuesta de 3 minutos: “¿cuándo un hash gana a un árbol?”. Pega el outline en la bitácora.

### 3. Regresión final (40 min)

```bash
cd projects/m07-estructuras && npm test
```

### 4. Limpieza (40 min)

Quita `console.log` de debug, asegura que no hay secretos, actualiza scripts del package.json.

### 5. Commit (20 min)

```bash
git add projects/m07-estructuras
git commit -m "docs(m07): cierre materia y evidencias"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Autoevaluación: explicar hash vs árbol en voz alta | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `bitacora/cierre-m07.md` con checklist P1/P2/P3/proyecto marcados con rutas de archivo.
2. Suite verde y README de selección presente.
3. Commit `docs(m07): cierre materia y evidencias`.

## Errores comunes

- Marcar evidencias sin archivos en git.
- Checklist genérico sin rutas.
- Dejar benches o tests rotos “para después”.

## Siguiente

M07 cerrado — siguiente materia: [M08 · Análisis de algoritmos](../M08-analisis-de-algoritmos.md)
