---
id: L03
materia: M23
orden: 3
titulo: Export de ejemplo y borrador pipeline
horas: 5
semana: 1
lectura: Reproducibilidad jobs métricas
evidencia: projects/m23-ia/metricas/export-ejemplo.csv + pipeline.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Generar CSV de ejemplo (ficticio o anonimizado) y documentar
      pipeline extracción → agregación → export.


      P1 entrega artefactos que M26 puede operar; hoy es diseño ejecutable.


      Conceptos que debes poder explicar al cerrar:


      - Pipeline.

      - CSV.

      - Job schedule (idea).

      - Idempotencia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l03 export-de-ejemplo-y-borrador-pipeline"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Export de ejemplo y borrador pipeline" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m23-ia/metricas/export-ejemplo.csv + pipeline.md
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Generar CSV de ejemplo (ficticio o anonimizado) y documentar pipeline
          extracción → agregación → export.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m23-ia/metricas`.


      Exporta muestra a `projects/m23-ia/metricas/export-ejemplo.csv` (≥5 filas,
      columnas tenant_id + métricas).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Borrador `projects/m23-ia/metricas/pipeline.md`: pasos, herramienta,
      frecuencia, owner, enlace script.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m23-ia/metricas/export-ejemplo.csv +
        pipeline.md`.
      - CSV ejemplo.
      - pipeline.md borrador.
      - Script ejecutable o instrucción clara.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Export de ejemplo y borrador pipeline

**~5 h · Semana 1**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/metricas/export-ejemplo.csv + pipeline.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Generar CSV de ejemplo (ficticio o anonimizado) y documentar pipeline extracción → agregación → export.

## Por qué empieza así

P1 entrega artefactos que M26 puede operar; hoy es diseño ejecutable.

Conceptos que debes poder explicar al cerrar:

- Pipeline.
- CSV.
- Job schedule (idea).
- Idempotencia.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Reproducibilidad jobs métricas_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/metricas`.

Exporta muestra a `projects/m23-ia/metricas/export-ejemplo.csv` (≥5 filas, columnas tenant_id + métricas).

### 3. Laboratorio principal (90–120 min)

Borrador `projects/m23-ia/metricas/pipeline.md`: pasos, herramienta, frecuencia, owner, enlace script.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l03 export-de-ejemplo-y-borrador-pipeline"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Reproducibilidad jobs métricas | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/metricas/export-ejemplo.csv + pipeline.md`.
2. CSV ejemplo.
3. pipeline.md borrador.
4. Script ejecutable o instrucción clara.
5. Commit `docs(m23): l03 …` en el historial.

## Errores comunes

- CSV con nombres.
- Pipeline ‘manual cuando quiera’.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L04 — Cierre semana 1 métricas — P1 avance](L04-cierre-semana-1-metricas-p1-avance.md)
