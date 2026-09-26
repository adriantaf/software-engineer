---
id: L23
materia: M23
orden: 23
titulo: README asistente FAQ y límites producto
horas: 5.0
semana: 6
lectura: Soporte y expectativas
evidencia: projects/m23-ia/faq-asistente/README.md final
---

# L23 — README asistente FAQ y límites producto

**~5 h · Semana 6**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/faq-asistente/README.md final`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Finalizar README: qué hace, qué no hace, escalación humana, privacidad.

## Por qué empieza así

Proyecto P3 FAQ integrado; soporte necesita límites claros.

Conceptos que debes poder explicar al cerrar:

- Scope.
- No-go.
- Soporte.
- Privacidad.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Soporte y expectativas_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/faq-asistente`.

README final en `projects/m23-ia/faq-asistente/`: secciones Scope, Limits, Privacy, Runbook incidencia.

### 3. Laboratorio principal (90–120 min)

Enlaza código/endpoint staging.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l23 readme-asistente-faq-y-l-mites-producto"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Soporte y expectativas | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/faq-asistente/README.md final`.
2. README final.
3. Limits claros.
4. Enlace código.
5. Commit `docs(m23): l23 …` en el historial.

## Errores comunes

- ‘IA mágica’.
- Sin escalación humana.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L24 — Cierre M23 — P1–P3, dominio y handoff M26](L24-cierre-m23-p1-p3-dominio-y-handoff-m26.md)
