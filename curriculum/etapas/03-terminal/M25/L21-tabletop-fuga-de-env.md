---
id: L21
materia: M25
orden: 21
titulo: Tabletop — fuga de .env
horas: 5.0
semana: 6
lectura: OWASP Reporting + ficha M25
evidencia: projects/m25-ciber/tabletop/env-leak.md
---

# L21 — Tabletop — fuga de .env

**~5 h · Semana 6**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/tabletop/env-leak.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Simulación 30 min: secretos filtrados; pasos; comunicación.

## Por qué empieza así

M26 exige review M25 vigente; tabletop demuestra que no solo leíste OWASP.

Conceptos que debes poder explicar al cerrar:

- Contención
- Rotación credenciales
- Post-mortem blameless

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Reporting + ficha M25_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Escenario tabletop .env (30–40 min)

En `tabletop/env-leak.md` define: quién filtró (gist/chat), qué secrets estaban, alcance (staging vs prod).

### 3. Narrativa ≥30 min de decisión (90–110 min)

Escribe timeline minuto a minuto (T+0 … T+60): detectar, rotar claves Stripe/DB, revocar sesiones, comunicar. Sin copiar tutorial genérico — usa **tus** nombres de servicio.

### 4. Acciones verificables (30–40 min)

Checklist de 8 acciones con dueño=tú y evidencia esperada (issue, rotación documentada).

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l21 tabletop-fuga-de-env"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Reporting + ficha M25 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/tabletop/env-leak.md`.
2. Narrativa ≥30 min equivalente escrita.
3. security-review.md enlaza PRs y tests.
4. Commit `docs(m25): l21 …` en el historial.

## Errores comunes

- Tabletop copiado de blog.
- Review sin pruebas cross-tenant.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L22 — Tabletop — acceso cross-tenant en prod](L22-tabletop-acceso-cross-tenant-en-prod.md)
