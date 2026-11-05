---
id: L20
materia: M09
orden: 20
titulo: 'Reportes, seeds y cierre M09'
horas: 5
semana: 5
lectura: 'Cierre: seeds + reportes de negocio'
evidencia: seeds + reportes.md + README — cierra proyecto M09
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras el **proyecto** de la materia: esquema reproducible, seeds y
      reportes útiles.


      **Objetivo de esta lección:** Dejar `seeds/`, `reportes.md` y README en
      estado “otro humano levanta esto”.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Seeds realistas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos
      git commit -m "docs(m09): cierre materia seeds y reportes"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Dos reportes
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos
      git commit -m "docs(m09): cierre materia seeds y reportes"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Reportes, seeds y cierre M09», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Reportes, seeds y
          cierre M09
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

      `git add projects/m09-bases-datos`
    comandoEsperado:
      - git add projects/m09-bases-datos
      - 'git commit -m "docs(m09): cierre materia seeds y reportes"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m09-bases-datos'
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
          Dejar `seeds/`, `reportes.md` y README en estado “otro humano levanta
          esto”.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M09
    xp: 25
    enunciado: >-
      Cierra **Bases de datos** con evidencia real en el repo. Marca la rúbrica
      solo si puedes demostrar cada criterio (si no está en git, no cuenta).
    entregables:
      - 'P1: Modelo ER + normalización hasta 3FN'
      - 'P2: SQL: joins, agregaciones, índices'
      - 'P3: Migraciones, transacciones y least privilege'
      - 'Proyecto: Esquema de Vitrina/POS con seeds y reportes'
      - seeds + reportes.md + README — cierra proyecto M09
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: '`seeds/001_demo.sql` (o ampliado) aplica limpio.'
      - id: r3
        criterio: '`reportes.md` tiene ≥2 reportes con SQL + salida.'
      - id: r4
        criterio: Otro dev podría recrear la BD solo con tu README (lo simulas tú).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`seeds/001_demo.sql` (o ampliado) aplica limpio.'
      - '`reportes.md` tiene ≥2 reportes con SQL + salida.'
      - Otro dev podría recrear la BD solo con tu README (lo simulas tú).
    siguiente: Materia M09 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Reportes, seeds y cierre M09

**~5.0 h · Semana 5**

Cierras el **proyecto** de la materia: esquema reproducible, seeds y reportes útiles.

## Objetivo

Dejar `seeds/`, `reportes.md` y README en estado “otro humano levanta esto”.

## Pasos

### 1. Seeds realistas (75 min)

Amplía `seeds/001_demo.sql`: ≥5 clientes, ≥3 servicios, pedidos en varios estados (`programada`, `completada`, `no_show`, `cancelada`). Reaplica en DB limpia o tras truncate controlado.

### 2. Dos reportes (75 min)

Completa `reportes.md`. Ideas:

1. No-shows de los últimos 30 días por cliente.
2. Ingresos estimados (centavos) por servicio en pedidos `completada`.

Cada uno: pregunta → archivo SQL → salida → uso para el dueño.

### 3. Checklist total (45 min)

P1 `er-vitrina.md` · P2 `sql/` + `explain-notas.md` · P3 `migrations/` + `roles.md` · Proyecto seeds + reportes.

### 4. Simulación máquina limpia (45 min)

Sigue solo tu README (sin mirar las lecciones). Anota fricciones y arréglalas.

### 5. Commit de cierre (15 min)

```bash
git add projects/m09-bases-datos
git commit -m "docs(m09): cierre materia seeds y reportes"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Cierre: seeds + reportes de negocio | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `seeds/001_demo.sql` (o ampliado) aplica limpio.
2. `reportes.md` tiene ≥2 reportes con SQL + salida.
3. Otro dev podría recrear la BD solo con tu README (lo simulas tú).

## Errores comunes

- Reportes sin pregunta de negocio.
- Seeds con datos personales reales.
- Marcar el proyecto en la UI sin `reportes.md`.

## Siguiente

Cierra la [ficha M09](../M09-bases-de-datos.md). Siguiente materia disciplinaria según tu plan.
