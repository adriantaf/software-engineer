---
id: L15
materia: M23
orden: 15
titulo: Ingesta corpus tenant B y contraste
horas: 5.0
semana: 4
lectura: Aislamiento datos desde diseño
evidencia: projects/m23-ia/rag/corpus/tenant-b/
---

# L15 — Ingesta corpus tenant B y contraste

**~5 h · Semana 4**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/rag/corpus/tenant-b/`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Segundo corpus claramente distinto (tenant B) para pruebas cross-tenant.

## Por qué empieza así

Demo obligatoria A no ve B empieza con datos separados.

Conceptos que debes poder explicar al cerrar:

- Separación física.
- IDs distintos.
- Políticas opuestas (test).

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Aislamiento datos desde diseño_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/rag/corpus`.

Corpus `projects/m23-ia/rag/corpus/tenant-b/` con política cancelación **distinta** a A (facilita detectar fuga).

### 3. Laboratorio principal (90–120 min)

Tabla comparación A vs B en `projects/m23-ia/rag/corpus/README.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l15 ingesta-corpus-tenant-b-y-contraste"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Aislamiento datos desde diseño | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/rag/corpus/tenant-b/`.
2. Corpus B ≥3 docs.
3. Política distinta.
4. README comparativo.
5. Commit `docs(m23): l15 …` en el historial.

## Errores comunes

- Mismo texto A/B.
- tenant_id solo en comentario.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L16 — Implementación retrieval con WHERE tenant_id](L16-implementacion-retrieval-con-where-tenant-id.md)
