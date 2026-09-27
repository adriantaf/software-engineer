---
id: L24
materia: M26
orden: 24
titulo: Hardening final pre-demo pública
horas: 5.0
semana: 6
lectura: checklist M25
evidencia: projects/m26-capstone/hardening-final.md
---

# L24 — Hardening final pre-demo pública

**~5 h · Semana 6**

Capstone: SaaS multi-tenant en producción. Hoy entregas **`projects/m26-capstone/hardening-final.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M26.

## Objetivo

Hardening final pre-demo pública (headers, secretos, errores).

## Por qué empieza así

M26 es el cierre del plan: SaaS multi-tenant real, no portafolio de tutoriales.

Conceptos que debes poder explicar al cerrar:

- Secrets
- TLS

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _checklist M25_.

Marca en `projects/m26-capstone/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección.

### 2. Checklist pre-demo (30–40 min)

En `projects/m26-capstone/hardening-final.md` tabla: headers | secretos | errores | rate-limit | cross-tenant CI | cada uno con link evidencia.

### 3. Cierra los rojos (100–120 min)

Todo ítem rojo → fix o waiver. Re-verifica:

```bash
curl -sI "https://TU-PROD-O-STAGING" | rg -i "strict-transport|content-security|x-frame"
```

### 4. Go/no-go demo pública (20–30 min)

Frase explícita + fecha. Bitácora semana-06.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m26): l24 hardening-final-pre-demo-p-blica"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Memoria propia + producto-saas + egreso | checklist M25 | [Rúbrica de egreso](../../../egreso.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M26](../../../bibliografia.md#m26-proyecto-integrador) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m26-capstone/hardening-final.md`.
2. Commit en git con mensaje docs(m26).
3. Bitácora de la semana actualizada.

## Errores comunes

- Un solo tenant de mentira.
- Stripe solo en localhost sin webhook desplegado.
- Memoria genérica sin tu tenancy real.

## Siguiente

[L25 — Memoria — arquitectura y diagramas](L25-memoria-arquitectura-y-diagramas.md)
