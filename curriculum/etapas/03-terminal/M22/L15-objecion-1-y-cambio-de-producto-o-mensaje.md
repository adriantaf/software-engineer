---
id: L15
materia: M22
orden: 15
titulo: Objeción #1 y cambio de producto o mensaje
horas: 5.0
semana: 4
lectura: Lean — build-measure-learn en producto
evidencia: projects/m22-bektor/objeciones-sintesis.md
---

# L15 — Objeción #1 y cambio de producto o mensaje

**~5 h · Semana 4**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/objeciones-sintesis.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Identificar objeción más frecuente y documentar cambio en mensaje **o** issue en backlog Vitrina.

## Por qué empieza así

Criterio dominio: nombrar objeción #1 y qué cambiaste.

Conceptos que debes poder explicar al cerrar:

- Objeción.
- Backlog producto.
- Mensaje.
- Trazabilidad M21.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — build-measure-learn en producto_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Crea `projects/m22-bektor/objeciones-sintesis.md` con ranking top 3 objeciones.

### 3. Laboratorio principal (90–120 min)

Abre issue en repo producto **o** entrada en `projects/m21-proyectos/roadmap-trimestre.md` si el fix es producto. Enlaza en demo fichas.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l15 objeci-n-1-y-cambio-de-producto-o-mensaj"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — build-measure-learn en producto | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/objeciones-sintesis.md`.
2. Top 3 objeciones.
3. Cambio mensaje/producto enlazado.
4. Issue o roadmap.
5. Commit `docs(m22): l15 …` en el historial.

## Errores comunes

- Quejarse sin acción.
- Objeción inventada sin demos.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L16 — Refinar pricing tras métricas semana 4](L16-refinar-pricing-tras-metricas-semana-4.md)
