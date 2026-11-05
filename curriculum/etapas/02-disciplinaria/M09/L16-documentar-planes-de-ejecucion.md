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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Cerrar `explain-notas.md` y la checklist P2 en el README.

      La evidencia de P2 es legible por otro humano (tú en tres meses).
  - id: s2
    tipo: ejemplo
    titulo: 1. Pulido del documento
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): cierra P2 explain y sql"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Documentar planes de ejecución" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: explain-notas.md completo — cierra P2
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

      `git commit -am "docs(m09): cierra P2 explain y sql"`
    comandoEsperado:
      - 'git commit -am "docs(m09): cierra P2 explain y sql"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "docs(m09): cierra P2 explain y sql"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Cerrar `explain-notas.md` y la checklist P2 en el README.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Índice de sql/
    xp: 10
    cuerpo: 'Tabla corta en README: archivo → pregunta.'
  - id: s7
    tipo: explicacion
    titulo: 3. Autorevisión P2
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
