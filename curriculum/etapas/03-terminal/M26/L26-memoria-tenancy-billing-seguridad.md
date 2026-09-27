---
id: L26
materia: M26
orden: 26
titulo: Memoria — tenancy, billing, seguridad
horas: 5.0
semana: 7
lectura: secciones P2
evidencia: projects/m26-capstone/memoria/tenancy-billing-seguridad.md
---

# L26 — Memoria — tenancy, billing, seguridad

**~5 h · Semana 7**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/memoria/tenancy-billing-seguridad.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Memoria: tenancy + billing + seguridad con evidencias enlazadas.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Narrativa tercero

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _secciones P2_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Outline de narrativa (25–35 min)

En `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`: H2 Tenancy | Billing | Seguridad.

### 3. Escribe para un tercero (100–120 min)

Cada H2: cómo funciona en **tu** producto + 2 evidencias (path test, URL, PR).

Un mentor debe entender sin tu voz en vivo. Enlaza L03, L17–L20, L21–L24.

### 4. Pasa el test del screenshot (25–35 min)

Si quitas tu cara del video, ¿el doc basta? Ajusta. Bitácora semana-07.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l26 memoria-tenancy-billing-seguridad"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | secciones P2 | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/memoria/tenancy-billing-seguridad.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L27 — Registro comercial M22 y trials](L27-registro-comercial-m22-y-trials.md)
