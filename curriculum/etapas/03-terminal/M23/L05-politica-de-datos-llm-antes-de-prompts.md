---
id: L05
materia: M23
orden: 5
titulo: Política de datos LLM antes de prompts
horas: 5.0
semana: 2
lectura: Ética/datos + vendor LLM terms
evidencia: projects/m23-ia/politica-datos-llm.md
---

# L05 — Política de datos LLM antes de prompts

**~5 h · Semana 2**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/politica-datos-llm.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Redactar política: qué nunca enviar a LLM, retención logs, filtro tenant, incidentes.

## Por qué empieza así

Regla M23: política **antes** de pegar datos en ChatGPT ‘solo probar’.

Conceptos que debes poder explicar al cerrar:

- PII.
- Retención.
- Tenant scope.
- Incident response.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Ética/datos + vendor LLM terms_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia`.

Completa `projects/m23-ia/politica-datos-llm.md` (≥1 página): prohibidos, permitidos anonimizados, logs, borrado, responsable.

### 3. Laboratorio principal (90–120 min)

Enlaza [hilo seguridad](../../hilos/seguridad.md). Commit antes de cualquier script que llame API.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l05 pol-tica-de-datos-llm-antes-de-prompts"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Ética/datos + vendor LLM terms | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/politica-datos-llm.md`.
2. Política completa.
3. Commit previo a scripts.
4. Enlace seguridad.

## Errores comunes

- Política post-hoc.
- Permitir dumps BD.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Set gold de 10 preguntas FAQ del ICP](L06-set-gold-de-10-preguntas-faq-del-icp.md)
