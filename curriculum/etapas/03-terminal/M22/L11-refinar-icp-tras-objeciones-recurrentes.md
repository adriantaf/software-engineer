---
id: L11
materia: M22
orden: 11
titulo: Refinar ICP tras objeciones recurrentes
horas: 5.0
semana: 3
lectura: Lean — segmento y niche
evidencia: projects/m22-bektor/icp.md revisión
---

# L11 — Refinar ICP tras objeciones recurrentes

**~5 h · Semana 3**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/icp.md revisión`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Revisar ICP: ¿sigues en el sub-vertical? Ajustar **mensaje**, no segmento, salvo evidencia fuerte.

## Por qué empieza así

Cambiar ICP cada semana es anti-patrón; aquí solo permites ajuste de mensaje o criterio de calificación.

Conceptos que debes poder explicar al cerrar:

- Calificación lead.
- Disqualify.
- Mensaje.
- Evidencia 6 demos.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — segmento y niche_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Añade a `projects/m22-bektor/icp.md` sección **Calificación**: 3 preguntas antes de demo.

### 3. Laboratorio principal (90–120 min)

Resume objeciones 1–6 en `projects/m22-bektor/bitacora-m22.md`. Confirma por escrito: mantienes sub-vertical Sí/No + razón.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l11 refinar-icp-tras-objeciones-recurrentes"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — segmento y niche | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/icp.md revisión`.
2. ICP revisado.
3. Objeciones resumidas.
4. Decisión segmento explícita.
5. Commit `docs(m22): l11 …` en el historial.

## Errores comunes

- Cambiar ICP sin 10 conversaciones.
- Mezclar verticales en outreach.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L12 — Pricing Free/Pro — borrador defendible](L12-pricing-free-pro-borrador-defendible.md)
