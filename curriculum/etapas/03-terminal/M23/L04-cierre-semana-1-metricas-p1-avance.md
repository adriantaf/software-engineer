---
id: L04
materia: M23
orden: 4
titulo: Cierre semana 1 métricas — P1 avance
horas: 5.0
semana: 1
lectura: Repaso definiciones + privacidad
evidencia: projects/m23-ia/metricas/semana-01.md
---

# L04 — Cierre semana 1 métricas — P1 avance

**~5 h · Semana 1**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/metricas/semana-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Consolidar semana métricas; revisar que export cumple política futura LLM.

## Por qué empieza así

Semana 1 cierra base numérica antes de tocar APIs externas.

Conceptos que debes poder explicar al cerrar:

- Revisión pares (mentor).
- Checklist P1.
- Documentación.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Repaso definiciones + privacidad_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/metricas`.

`projects/m23-ia/metricas/semana-01.md`: checklist P1 parcial + preguntas abiertas.

### 3. Laboratorio principal (90–120 min)

Anticipa `projects/m23-ia/politica-datos-llm.md` con 3 bullets qué **nunca** sale a LLM.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l04 cierre-semana-1-m-tricas-p1-avance"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Repaso definiciones + privacidad | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/metricas/semana-01.md`.
2. semana-01.md.
3. Checklist P1.
4. Bullets política LLM.
5. Commit `docs(m23): l04 …` en el historial.

## Errores comunes

- Marcar P1 completo sin pipeline.
- Export sin revisar PII.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Política de datos LLM antes de prompts](L05-politica-de-datos-llm-antes-de-prompts.md)
