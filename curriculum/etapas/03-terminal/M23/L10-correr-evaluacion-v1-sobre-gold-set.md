---
id: L10
materia: M23
orden: 10
titulo: Correr evaluación v1 sobre gold set
horas: 5.0
semana: 3
lectura: Batch eval reproducible
evidencia: projects/m23-ia/llm-eval/resultados-v1.csv
---

# L10 — Correr evaluación v1 sobre gold set

**~5 h · Semana 3**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/resultados-v1.csv`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Ejecutar evaluación completa v1; tabular pregunta, respuesta modelo, score rúbrica.

## Por qué empieza así

Resultados versionados permiten auditoría y mejora.

Conceptos que debes poder explicar al cerrar:

- Batch.
- CSV resultados.
- Reproducibilidad.
- Version tag.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Batch eval reproducible_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

Genera `projects/m23-ia/llm-eval/resultados-v1.csv`. Documenta comando exacto en `projects/m23-ia/llm-eval/README.md`.

### 3. Laboratorio principal (90–120 min)

No pegues API key en README.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l10 correr-evaluaci-n-v1-sobre-gold-set"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Batch eval reproducible | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/resultados-v1.csv`.
2. resultados-v1.csv 10 filas.
3. README comando.
4. prompt-v1 referenciado.
5. Commit `docs(m23): l10 …` en el historial.

## Errores comunes

- Eval parcial sin commit.
- Editar gold para ‘pasar’.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Prompt v2 — iteración medida](L11-prompt-v2-iteracion-medida.md)
