---
id: L22
materia: M22
orden: 22
titulo: Síntesis comercial para backlog M21
horas: 5.0
semana: 6
lectura: Lean — aprendizaje → producto
evidencia: projects/m22-bektor/handoff-producto.md
---

# L22 — Síntesis comercial para backlog M21

**~5 h · Semana 6**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/handoff-producto.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Traducir aprendizajes comerciales en ≥5 issues priorizados para Agenda Ops (M21 backlog).

## Por qué empieza así

El hilo Ops/SaaS cierra loop gestión ↔ mercado.

Conceptos que debes poder explicar al cerrar:

- Backlog.
- Prioridad.
- Issue template.
- Demo feedback.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — aprendizaje → producto_.

Traduce a Agenda Ops: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

`projects/m22-bektor/handoff-producto.md`: tabla aprendizaje → issue sugerido → prioridad.

### 3. Laboratorio principal (90–120 min)

Crea o enlaza issues reales en repo producto. Notifica en `projects/m21-proyectos/board.md`.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l22 s-ntesis-comercial-para-backlog-m21"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — aprendizaje → producto | [producto-saas (Agenda Ops)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/handoff-producto.md`.
2. ≥5 issues sugeridos.
3. Enlaces GitHub.
4. board.md actualizado.

## Errores comunes

- Lista deseos sin issues.
- Features sin origen demo.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L23 — Pitch final 60s y práctica grabada](L23-pitch-final-60s-y-practica-grabada.md)
