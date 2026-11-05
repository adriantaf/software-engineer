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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 parcial: tres sorts propios + tabla defendible.


      **Objetivo de esta lección:** Publicar `sorts/README.md` comparativo y
      verificar tests de la carpeta sorts.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría
    xp: 10
    cuerpo: |-
      ```bash
      ls sorts/*.ts
      npm test
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Tabla
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos
      git commit -m "docs(m08): tabla P2 sorts"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tabla P2 sorts en README», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tabla P2 sorts en
          README
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

      `ls sorts/*.ts`
    comandoEsperado:
      - ls sorts/*.ts
      - npm test
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: ls sorts/*.ts'
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
          Publicar `sorts/README.md` comparativo y verificar tests de la carpeta
          sorts.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Microbench opcional
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
