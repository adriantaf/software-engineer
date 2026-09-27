---
id: L20
materia: M23
orden: 20
titulo: Test automatizado cross-tenant en CI
horas: 5.0
semana: 5
lectura: Vitest/Jest en repo producto
evidencia: projects/m23-ia/rag/ci-evidencia.md
---

# L20 — Test automatizado cross-tenant en CI

**~5 h · Semana 5**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/rag/ci-evidencia.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Automatizar al menos un test que falle si retrieval devuelve chunk de otro tenant.

## Por qué empieza así

Manual no escala; CI evita regresión antes de M26.

Conceptos que debes poder explicar al cerrar:

- Test auto.
- Fixture dos tenants.
- CI verde.
- Regression.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Vitest/Jest en repo producto_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/rag`.

`projects/m23-ia/rag/ci-evidencia.md`: enlace workflow o comando local, commit SHA, salida test PASS.

### 3. Laboratorio principal (90–120 min)

Si aún no hay CI, script `npm test -- rag-isolation` documentado.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l20 test-automatizado-cross-tenant-en-ci"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Vitest/Jest en repo producto | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/rag/ci-evidencia.md`.
2. Test automatizado.
3. ci-evidencia.md.
4. Enlace commit.

## Errores comunes

- Solo test manual.
- Skip en CI.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L21 — Feature flag IA y alineación pricing M22](L21-feature-flag-ia-y-alineacion-pricing-m22.md)
