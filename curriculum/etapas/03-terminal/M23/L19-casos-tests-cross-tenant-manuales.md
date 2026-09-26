---
id: L19
materia: M23
orden: 19
titulo: Casos tests-cross-tenant manuales
horas: 5.0
semana: 5
lectura: QA seguridad producto
evidencia: projects/m23-ia/rag/tests-cross-tenant.md
---

# L19 — Casos tests-cross-tenant manuales

**~5 h · Semana 5**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/rag/tests-cross-tenant.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Documentar casos: tenant A pregunta política B → no chunks B en contexto/respuesta.

## Por qué empieza así

P3 y criterio egreso: evidencia reproducible de aislamiento.

Conceptos que debes poder explicar al cerrar:

- Cross-tenant.
- Context dump.
- Assertion.
- Evidencia log.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _QA seguridad producto_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/rag`.

`projects/m23-ia/rag/tests-cross-tenant.md`: ≥4 casos, pasos, resultado esperado, evidencia (log CI o captura redacted).

### 3. Laboratorio principal (90–120 min)

Pregunta A sobre ‘política cancelación’ debe citar solo A.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l19 casos-tests-cross-tenant-manuales"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | QA seguridad producto | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/rag/tests-cross-tenant.md`.
2. ≥4 casos.
3. Evidencia adjunta/enlace.
4. Pasos reproducibles.
5. Commit `docs(m23): l19 …` en el historial.

## Errores comunes

- Solo ‘parece ok’.
- Test sin tenant B ingestado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L20 — Test automatizado cross-tenant en CI](L20-test-automatizado-cross-tenant-en-ci.md)
