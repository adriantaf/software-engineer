---
id: L02
materia: M22
orden: 2
titulo: ICP único — sub-vertical fijado por escrito
horas: 5.0
semana: 1
lectura: Lean — segmento inicial + anti-patterns
evidencia: projects/m22-bektor/icp.md
---

# L02 — ICP único — sub-vertical fijado por escrito

**~5 h · Semana 1**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/icp.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Elegir **un** sub-vertical (barbería, clínica dental, taller…) en Ensenada o alrededores y documentar por qué encaja con Vitrina.

## Por qué empieza así

Cambiar de ICP cada semana invalida demos y pricing; la materia exige disciplina de 6 semanas.

Conceptos que debes poder explicar al cerrar:

- ICP.
- Dolor operativo.
- Willingness to pay (hipótesis).
- Canal de contacto.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — segmento inicial + anti-patterns_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

En `projects/m22-bektor/icp.md`: perfil del dueño, tamaño del negocio, dolor (pedido abandonados, doble reserva), herramientas actuales, por qué **no** marketplace.

### 3. Laboratorio principal (90–120 min)

Compromiso: **no cambiar** sub-vertical hasta fin de M22 salvo pivote documentado al final.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l02 icp-nico-sub-vertical-fijado-por-escrito"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — segmento inicial + anti-patterns | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/icp.md`.
2. icp.md completo.
3. Sub-vertical único.
4. Dolor medible descrito.
5. Commit `docs(m22): l02 …` en el historial.

## Errores comunes

- ICP ‘cualquier negocio’.
- Sin geografía/canal.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L03 — Oferta SaaS en un párrafo](L03-oferta-saas-en-un-parrafo.md)
