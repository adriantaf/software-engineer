---
id: L16
materia: M09
orden: 16
titulo: Documentar planes de ejecución
horas: 5
semana: 4
lectura: Repaso EXPLAIN + tu explain-notas.md
evidencia: explain-notas.md completo — cierra P2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La evidencia de P2 es legible por otro humano (tú en tres meses).


      **Objetivo de esta lección:** Cerrar `explain-notas.md` y la checklist P2
      en el README.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Pulido del documento
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): cierra P2 explain y sql"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Índice de sql/
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): cierra P2 explain y sql"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Documentar planes de ejecución», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Documentar planes de
          ejecución
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

      `git commit -am "docs(m09): cierra P2 explain y sql"`
    comandoEsperado:
      - 'git commit -am "docs(m09): cierra P2 explain y sql"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "docs(m09): cierra P2 explain y sql"'
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
        texto: Cerrar `explain-notas.md` y la checklist P2 en el README.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Autorevisión P2
    xp: 10
    cuerpo: >-
      Checklist ficha M09: joins/agregaciones + EXPLAIN comentado. Lista gaps si
      los hay (y ciérralos).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `explain-notas.md` tiene pregunta, SQL, antes, cambio, después,
        conclusión.
      - README marca P2 (sql/ + explain) como listo.
      - Commit de cierre P2.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Documentar planes de ejecución

**~5.0 h · Semana 4**

La evidencia de P2 es legible por otro humano (tú en tres meses).

## Objetivo

Cerrar `explain-notas.md` y la checklist P2 en el README.

## Pasos

### 1. Pulido del documento (90 min)

Relee `explain-notas.md`. Añade:

- Link relativo al `.sql`
- Pregunta de negocio en una línea
- Conclusión binaria: ¿mantenemos el índice? sí/no + cuándo revisarlo

### 2. Índice de sql/ (40 min)

Tabla corta en README: archivo → pregunta.

### 3. Autorevisión P2 (40 min)

Checklist ficha M09: joins/agregaciones + EXPLAIN comentado. Lista gaps si los hay (y ciérralos).

### 4. Commit (20 min)

```bash
git commit -am "docs(m09): cierra P2 explain y sql"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Repaso EXPLAIN + tu explain-notas.md | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `explain-notas.md` tiene pregunta, SQL, antes, cambio, después, conclusión.
2. README marca P2 (sql/ + explain) como listo.
3. Commit de cierre P2.

## Errores comunes

- Notas solo con screenshots ilegibles.
- No enlazar el archivo SQL del reporte.
- Cerrar P2 sin ≥5 queries de L12.

## Siguiente

[L17 — Transacciones ACID](L17-transacciones-acid.md)
