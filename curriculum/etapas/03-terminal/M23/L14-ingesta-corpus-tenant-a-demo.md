---
id: L14
materia: M23
orden: 14
titulo: Ingesta corpus tenant A (demo)
horas: 5.0
semana: 4
lectura: Docs markdown políticas negocio
evidencia: projects/m23-ia/rag/corpus/tenant-a/
---

# L14 — Ingesta corpus tenant A (demo)

**~5 h · Semana 4**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/rag/corpus/tenant-a/`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Ingestar ≥3 documentos markdown de políticas ficticias del tenant A demo.

## Por qué empieza así

Necesitas corpus separado antes de probar cross-tenant.

Conceptos que debes poder explicar al cerrar:

- Corpus.
- Markdown.
- Metadatos.
- Sin PII real.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Docs markdown políticas negocio_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/rag/corpus`.

Crea `projects/m23-ia/rag/corpus/tenant-a/*.md` (horarios, cancelación, servicios). Script ingesta documentado o manual con hashes.

### 3. Laboratorio principal (90–120 min)

Registra versión corpus en `projects/m23-ia/rag/corpus/README.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l14 ingesta-corpus-tenant-a-demo"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Docs markdown políticas negocio | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/rag/corpus/tenant-a/`.
2. ≥3 docs tenant A.
3. README corpus.
4. Sin PII real.
5. Commit `docs(m23): l14 …` en el historial.

## Errores comunes

- PDF escaneado sin OCR plan.
- Mezclar A y B en carpeta.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L15 — Ingesta corpus tenant B y contraste](L15-ingesta-corpus-tenant-b-y-contraste.md)
