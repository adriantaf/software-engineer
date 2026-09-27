---
id: L18
materia: M23
orden: 18
titulo: UI o CLI asistente para owner
horas: 5.0
semana: 5
lectura: UX mínima FAQ
evidencia: projects/m23-ia/faq-asistente/README.md borrador
---

# L18 — UI o CLI asistente para owner

**~5 h · Semana 5**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/faq-asistente/README.md borrador`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Exponer asistente mínimo: owner pregunta política cancelación → respuesta grounded.

## Por qué empieza así

Proyecto materia: asistente scoped por tenant en staging.

Conceptos que debes poder explicar al cerrar:

- UI mínima.
- CLI alternativa.
- Citas fuente.
- Fallback sin alucinar.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _UX mínima FAQ_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/faq-asistente`.

Amplía `projects/m23-ia/faq-asistente/README.md`: cómo probar, credenciales test, ejemplo pregunta/respuesta.

### 3. Laboratorio principal (90–120 min)

Captura o log de sesión **redactado**.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l18 ui-o-cli-asistente-para-owner"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | UX mínima FAQ | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/faq-asistente/README.md borrador`.
2. README uso.
3. Ejemplo Q&A.
4. Staging URL.
5. Commit `docs(m23): l18 …` en el historial.

## Errores comunes

- Prometer auto-agenda.
- Respuesta sin fuente.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L19 — Casos tests-cross-tenant manuales](L19-casos-tests-cross-tenant-manuales.md)
