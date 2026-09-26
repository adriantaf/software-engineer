---
id: L31
materia: M26
orden: 31
titulo: README capstone índice maestro
horas: 5.0
semana: 8
lectura: README proyecto
evidencia: projects/m26-capstone/README.md
---

# L31 — README capstone índice maestro

**~5 h · Semana 8**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/README.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

README capstone como índice maestro de toda la evidencia.

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Prod URL
- Repos

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _README proyecto_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Estructura del README (25–35 min)

En `projects/m26-capstone/README.md`: Prod URL | Staging | Demo video | Memoria | Seguridad | Comercial | Cómo correr tests.

### 3. Índice maestro clickeable (90–110 min)

Links relativos a **todos** los artefactos clave (alcance, demos, billing, security-review, egreso-checklist).

Un evaluador entra solo por este archivo.

### 4. Smoke del índice (25–35 min)

Abre 5 links al azar; arregla rotos. Bitácora semana-08.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l31 readme-capstone-ndice-maestro"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | README proyecto | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/README.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L32 — Cierre integrador y handoff v1.1](L32-cierre-integrador-y-handoff-v1-1.md)
