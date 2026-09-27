---
id: L11
materia: M23
orden: 11
titulo: Prompt v2 — iteración medida
horas: 5.0
semana: 3
lectura: Error analysis sobre v1
evidencia: projects/m23-ia/llm-eval/prompt-v2.txt + notas
---

# L11 — Prompt v2 — iteración medida

**~5 h · Semana 3**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/prompt-v2.txt + notas`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Analizar fallos v1, ajustar prompt v2, documentar hipótesis de mejora.

## Por qué empieza así

Iteración sin análisis es adivinar; registra **por qué** cambiaste cada frase.

Conceptos que debes poder explicar al cerrar:

- Error analysis.
- Changelog prompt.
- Temperatura.
- Grounding.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Error analysis sobre v1_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

`projects/m23-ia/llm-eval/prompt-v2-changelog.md`: fallos v1 → cambio v2.

### 3. Laboratorio principal (90–120 min)

Archivo `prompt-v2.txt`. Re-ejecuta eval → `resultados-v2.csv`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l11 prompt-v2-iteraci-n-medida"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Error analysis sobre v1 | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/prompt-v2.txt + notas`.
2. prompt-v2 + changelog.
3. resultados-v2.csv.
4. Hipótesis por cambio.
5. Commit `docs(m23): l11 …` en el historial.

## Errores comunes

- v2 sin comparar v1.
- Subir temperatura sin razón.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L12 — Umbral de calidad y cierre P2 parcial](L12-umbral-de-calidad-y-cierre-p2-parcial.md)
