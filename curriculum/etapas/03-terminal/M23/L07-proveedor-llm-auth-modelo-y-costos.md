---
id: L07
materia: M23
orden: 7
titulo: Proveedor LLM — auth, modelo y costos
horas: 5.0
semana: 2
lectura: Docs API LLM oficiales
evidencia: projects/m23-ia/llm-eval/proveedor.md
---

# L07 — Proveedor LLM — auth, modelo y costos

**~5 h · Semana 2**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/proveedor.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Elegir proveedor, anotar modelo, límites rate, precio por 1k tokens, variables entorno.

## Por qué empieza así

Costos ignorados hasta factura es error común del plan.

Conceptos que debes poder explicar al cerrar:

- API key.
- Modelo.
- Rate limit.
- Costo estimado.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Docs API LLM oficiales_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

`projects/m23-ia/llm-eval/proveedor.md`: tabla comparativa si dudaste; decisión final con razón.

### 3. Laboratorio principal (90–120 min)

Plantilla `.env.example` sin secretos; claves solo en entorno local/staging.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l07 proveedor-llm-auth-modelo-y-costos"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Docs API LLM oficiales | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/proveedor.md`.
2. proveedor.md.
3. .env.example.
4. Sin secretos en git.

## Errores comunes

- Key en repo.
- Modelo sin límite tokens.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L08 — Primer script LLM y logs sin PII](L08-primer-script-llm-y-logs-sin-pii.md)
