---
id: L08
materia: M08
orden: 8
titulo: Tabla P2 sorts en README
horas: 5
semana: 2
lectura: Comparativa de ordenamientos P2
evidencia: sorts/README.md P2 parcial
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Publicar `sorts/README.md` comparativo y verificar tests de
      la carpeta sorts.


      P2 parcial: tres sorts propios + tabla defendible.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría
    xp: 10
    cuerpo: |-
      ```bash
      ls sorts/*.ts
      npm test
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Tabla P2 sorts en README" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: sorts/README.md P2 parcial
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

      `ls sorts/*.ts`
    comandoEsperado:
      - ls sorts/*.ts
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: ls sorts/*.ts'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Publicar `sorts/README.md` comparativo y verificar tests de la carpeta
          sorts.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tabla
    xp: 10
    cuerpo: >-
      Columnas: algoritmo | peor | promedio | espacial | estable | cuándo
      usarlo. Filas: insertion, merge, quick, `Array.sort` (motor).
  - id: s7
    tipo: explicacion
    titulo: 3. Microbench opcional
    xp: 10
    cuerpo: '`sorts/bench.ts` N=5_000 — pega números en el README (honestos).'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `sorts/README.md` con tabla insertion/merge/quick (y nativo como
        referencia).
      - Suite de sorts verde; enlace desde README raíz del proyecto.
      - 'Commit `docs(m08): tabla P2 sorts`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Tabla P2 sorts en README

**~5.0 h · Semana 2**

P2 parcial: tres sorts propios + tabla defendible.

## Objetivo

Publicar `sorts/README.md` comparativo y verificar tests de la carpeta sorts.

## Pasos

### 1. Auditoría (30 min)

```bash
ls sorts/*.ts
npm test
```

### 2. Tabla (70 min)

Columnas: algoritmo | peor | promedio | espacial | estable | cuándo usarlo. Filas: insertion, merge, quick, `Array.sort` (motor).

### 3. Microbench opcional (60 min)

`sorts/bench.ts` N=5_000 — pega números en el README (honestos).

### 4. Enlace raíz (30 min)

Desde `projects/m08-algoritmos/README.md` → sección P2.

### 5. Commit (20 min)

```bash
git add projects/m08-algoritmos
git commit -m "docs(m08): tabla P2 sorts"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Tabla peor/promedio/espacial/estable por sort | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. `sorts/README.md` con tabla insertion/merge/quick (y nativo como referencia).
2. Suite de sorts verde; enlace desde README raíz del proyecto.
3. Commit `docs(m08): tabla P2 sorts`.

## Errores comunes

- Tabla copiada de Internet sin alinear a tu código.
- Omitir estabilidad o memoria.
- Dejar quick sin nota de peor caso.

## Siguiente

[L09 — Hash maps en problemas de conteo](L09-hash-maps-en-problemas-de-conteo.md)
