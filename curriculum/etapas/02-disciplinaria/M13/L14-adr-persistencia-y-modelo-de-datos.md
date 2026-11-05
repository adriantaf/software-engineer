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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `adr/002-persistencia.md` alineado a M09 y al diagrama de
      clases.


      Pedidos con rangos de tiempo, FKs, reportes simples, posible tenant_id
      luego.
  - id: s2
    tipo: ejemplo
    titulo: 1. Escribe el ADR
    xp: 10
    cuerpo: |-
      ```markdown
      ADR 002 — PostgreSQL + migraciones versionadas
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "ADR persistencia y modelo de datos" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: adr/002-persistencia.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Elegir DB por moda sin relación al
      reporte de pedidos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: '`adr/002-persistencia.md` alineado a M09 y al diagrama de clases.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
