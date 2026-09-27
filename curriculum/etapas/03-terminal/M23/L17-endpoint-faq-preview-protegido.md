---
id: L17
materia: M23
orden: 17
titulo: Endpoint faq-preview protegido
horas: 5.0
semana: 5
lectura: API interna admin
evidencia: projects/m23-ia/faq-asistente/endpoint.md
---

# L17 — Endpoint faq-preview protegido

**~5 h · Semana 5**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/faq-asistente/endpoint.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Diseñar o implementar POST interno faq-preview auth owner/staff con rate limit.

## Por qué empieza así

Semana 5 entrega superficie controlada antes de UI pulida.

Conceptos que debes poder explicar al cerrar:

- AuthZ.
- Rate limit.
- Preview vs prod.
- Logging redacted.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _API interna admin_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/faq-asistente`.

Documenta en `projects/m23-ia/faq-asistente/endpoint.md` ruta, roles, body, respuesta, errores.

### 3. Laboratorio principal (90–120 min)

Enlaza PR repo producto si existe. Sin endpoint público anónimo.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l17 endpoint-faq-preview-protegido"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | API interna admin | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/faq-asistente/endpoint.md`.
2. endpoint.md.
3. Roles definidos.
4. Rate limit mencionado.
5. Commit `docs(m23): l17 …` en el historial.

## Errores comunes

- Endpoint público.
- Sin auth.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L18 — UI o CLI asistente para owner](L18-ui-o-cli-asistente-para-owner.md)
