---
id: L14
materia: M13
orden: 14
titulo: ADR persistencia y modelo de datos
horas: 5
semana: 4
lectura: Elección Postgres + acceso a datos; modelo MVP
evidencia: adr/002-persistencia.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Pedidos con rangos de tiempo, FKs, reportes simples, posible tenant_id
      luego.


      **Objetivo de esta lección:** `adr/002-persistencia.md` alineado a M09 y
      al diagrama de clases.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Escribe el ADR
    xp: 10
    cuerpo: '```markdown # ADR 002 — PostgreSQL + migraciones versionadas'
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «ADR persistencia y modelo de datos», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de ADR persistencia y
          modelo de datos
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Elegir DB por moda sin relación al
      reporte de pedidos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: '`adr/002-persistencia.md` alineado a M09 y al diagrama de clases.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? ““Usaremos un ORM” sin decir cuál ni migración."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        ADR 002 elige Postgres (o justifica excepción) y cómo migrarás (SQL
        files / herramienta).
      - Alternativas rechazadas (p. ej. Mongo “porque JSON”) con motivo.
      - 'Commit `docs(m13): ADR 002 persistencia`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — ADR persistencia y modelo de datos

**~5.0 h · Semana 4**

Vitrina vive de consultas de agenda y FKs. Hoy firmas cómo persistir.

## Objetivo

`adr/002-persistencia.md` alineado a M09 y al diagrama de clases.

## Pasos (hazlos en orden)

### 1. Escribe el ADR (90–110 min)

```markdown
# ADR 002 — PostgreSQL + migraciones versionadas

## Contexto
Pedidos con rangos de tiempo, FKs, reportes simples, posible tenant_id luego.

## Decisión
PostgreSQL; migraciones SQL (o Prisma migrate — elige una) en repo.

## Consecuencias
+ Constraints e índices reales
+ Coincide con M09
− Ops de backups (M19)
```

Incluye acceso: Repository en infra (M14), no SQL en controllers.

### 2. Actualiza índice ADR (15 min)

### 3. Commit (15 min)

```bash
git add projects/m13-diseno/adr
git commit -m "docs(m13): ADR 002 persistencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Decisión de persistencia: Postgres, migraciones, acceso | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR 002 elige Postgres (o justifica excepción) y cómo migrarás (SQL files / herramienta).
2. Alternativas rechazadas (p. ej. Mongo “porque JSON”) con motivo.
3. Commit `docs(m13): ADR 002 persistencia`.

## Errores comunes

- Elegir DB por moda sin relación al reporte de pedidos.
- “Usaremos un ORM” sin decir cuál ni migración.
- Contradecir cardinalidades de L06 sin actualizar clases.

## Siguiente

[L15 — Extensibilidad tenant_id sin implementar](L15-extensibilidad-tenant-id-sin-implementar.md)
