---
id: L02
materia: M23
orden: 2
titulo: Consulta agregada por tenant_id sin PII
horas: 5
semana: 1
lectura: SQL agregaciones + minimización datos
evidencia: projects/m23-ia/metricas/query-agregada.sql
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El pipeline P1 debe ser reproducible y seguro para compartir export de
      ejemplo.


      Conceptos que debes poder explicar al cerrar:


      - GROUP BY tenant_id.

      - Minimización.

      - Vistas.

      - Anonimización.


      **Objetivo de esta lección:** Escribir SQL o script que agrupe por
      `tenant_id` sin columnas de PII en SELECT.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l02 consulta-agregada-por-tenant-id-sin-pii"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l02 consulta-agregada-por-tenant-id-sin-pii"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Consulta agregada por tenant_id sin PII», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Consulta agregada por
          tenant_id sin PII
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
          Escribir SQL o script que agrupe por `tenant_id` sin columnas de PII
          en SELECT.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: >-
      Prohibido SELECT de teléfono, nombre, notas clínicas. Comentario en
      archivo explica fuente tablas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/metricas/query-agregada.sql`.'
      - Query/script existe.
      - Sin PII en output.
      - Comentario fuente.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Consulta agregada por tenant_id sin PII

**~5 h · Semana 1**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/metricas/query-agregada.sql`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Escribir SQL o script que agrupe por `tenant_id` sin columnas de PII en SELECT.

## Por qué empieza así

El pipeline P1 debe ser reproducible y seguro para compartir export de ejemplo.

Conceptos que debes poder explicar al cerrar:

- GROUP BY tenant_id.
- Minimización.
- Vistas.
- Anonimización.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _SQL agregaciones + minimización datos_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/metricas`.

Crea `projects/m23-ia/metricas/query-agregada.sql` (o `.ts` script) contra schema Vitrina o fixture documentado.

### 3. Laboratorio principal (90–120 min)

Prohibido SELECT de teléfono, nombre, notas clínicas. Comentario en archivo explica fuente tablas.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l02 consulta-agregada-por-tenant-id-sin-pii"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | SQL agregaciones + minimización datos | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/metricas/query-agregada.sql`.
2. Query/script existe.
3. Sin PII en output.
4. Comentario fuente.
5. Commit `docs(m23): l02 …` en el historial.

## Errores comunes

- Dump crudo clientes.
- tenant_id del cliente HTTP.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L03 — Export de ejemplo y borrador pipeline](L03-export-de-ejemplo-y-borrador-pipeline.md)
