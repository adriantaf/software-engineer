---
id: L08
materia: M18
orden: 8
titulo: Threat model v1 post-autenticación (P1)
horas: 5.0
semana: 2
lectura: Repaso STRIDE semanas 1–2
evidencia: projects/m18-appsec/threat-model-v1.md
---

# L08 — Threat model v1 post-autenticación (P1)

**~5.0 h · Semana 2**

P1: threat model v1 revisado tras endurecer auth.

## Objetivo

`threat-model-v1.md` (o sección v1) con cambios vs v0 y residual risk auth.

## Pasos (hazlos en orden)

### 1. Diff v0→v1 (40 min)

Qué amenazas bajaron de severidad.

### 2. Redacción P1 (80–100 min)

Incluye supuestos de staging. Enlace inventario + ADR.

### 3. README P1 (15 min)

### 4. Commit

`docs(m18): l08 threat model v1 p1`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Repaso STRIDE semanas 1–2 | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. threat-model-v1.md completo (artefacto: `projects/m18-appsec/threat-model-v1.md`).
2. Tabla amenaza-control (artefacto: `projects/m18-appsec/threat-model-v1.md`).
3. Listo para marcar P1 en UI (artefacto: `projects/m18-appsec/threat-model-v1.md`).
4. Commit `docs(m18): L08 threat-model-v1-post-autenticacion-p1`.

## Errores comunes

- Renombrar v0 sin cambios.
- Omitir auth en el modelo.

## Siguiente

[L09 — Cookies Secure, HttpOnly y SameSite](L09-cookies-secure-httponly-y-samesite.md)
