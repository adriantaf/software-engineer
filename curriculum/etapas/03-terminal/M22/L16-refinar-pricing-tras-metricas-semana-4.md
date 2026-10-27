---
id: L16
materia: M22
orden: 16
titulo: Refinar pricing tras métricas semana 4
horas: 5.0
semana: 4
lectura: Lean — aprendizaje acumulado
evidencia: projects/m22-bektor/pricing.md v2
---

# L16 — Refinar pricing tras métricas semana 4

**~5 h · Semana 4**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing.md v2`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Ajustar pricing con nota de versión y evidencia de conversaciones (no intuición sola).

## Por qué empieza así

Preparas P3 final en semana 6; hoy versionas cambios.

Conceptos que debes poder explicar al cerrar:

- Changelog pricing.
- Anclaje.
- Límites Free.
- Trial.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — aprendizaje acumulado_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Añade `projects/m22-bektor/pricing-changelog.md` con v1→v2 y razón (pedido demo #).

### 3. Laboratorio principal (90–120 min)

Relee límites técnicos; alinea con plan Pro si incluirá FAQ IA (M23).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l16 refinar-pricing-tras-m-tricas-semana-4"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — aprendizaje acumulado | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing.md v2`.
2. pricing-changelog.
3. pricing.md v2.
4. Evidencia demo citada.
5. Commit `docs(m22): l16 …` en el historial.

## Errores comunes

- Cambiar precio sin razón.
- Ignorar costo IA.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L17 — Outreach semana 5 — lote de cinco contactos](L17-outreach-semana-5-lote-de-cinco-contactos.md)
