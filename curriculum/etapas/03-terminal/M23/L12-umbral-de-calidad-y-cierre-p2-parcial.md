---
id: L12
materia: M23
orden: 12
titulo: Umbral de calidad y cierre P2 parcial
horas: 5.0
semana: 3
lectura: Quality gate FAQ
evidencia: projects/m23-ia/llm-eval/resumen-evaluacion.md
---

# L12 — Umbral de calidad y cierre P2 parcial

**~5 h · Semana 3**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/resumen-evaluacion.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Comparar v1 vs v2; decidir si cumples umbral o documentas deuda para semana 5–6.

## Por qué empieza así

P2 exige rúbrica + resultados tabulados; hoy cierras el gate numérico.

Conceptos que debes poder explicar al cerrar:

- Umbral.
- Deuda.
- Costo por eval.
- Go/no-go RAG.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Quality gate FAQ_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

`projects/m23-ia/llm-eval/resumen-evaluacion.md`: tabla versiones, % correcto, costo tokens estimado, decisión.

### 3. Laboratorio principal (90–120 min)

Si no alcanzas umbral, lista 3 acciones (más docs tenant, RAG, bajar temperatura).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l12 umbral-de-calidad-y-cierre-p2-parcial"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Quality gate FAQ | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/resumen-evaluacion.md`.
2. Resumen v1/v2.
3. Umbral evaluado.
4. Decisión documentada.
5. Commit `docs(m23): l12 …` en el historial.

## Errores comunes

- Declarar éxito sin CSV.
- Ignorar costos.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L13 — Diseño RAG por tenant — chunking y almacén](L13-diseno-rag-por-tenant-chunking-y-almacen.md)
