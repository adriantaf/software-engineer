---
id: L17
materia: M18
orden: 17
titulo: IDOR en citas y recursos por ID
horas: 5.0
semana: 5
lectura: OWASP A01 Broken Access Control
evidencia: projects/m18-appsec/findings/003-idor.md
---

# L17 — IDOR en citas y recursos por ID

**~5.0 h · Semana 5**

`GET /citas/:id` sin comprobar dueño = IDOR.

## Objetivo

PoC cross-user + fix autorización + test automatizado.

## Pasos (hazlos en orden)

### 1. Dos usuarios (30 min)

Owner A y B (o staff) con citas distintas.

### 2. PoC (50–60 min)

Token A pide id de B. Documenta status code.

### 3. Fix + test (60–80 min)

Filtro por negocio/usuario. Test 403/404.

### 4. Commit

`fix(m18): l17 idor citas`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A01 Broken Access Control | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. PoC con dos usuarios (artefacto: `projects/m18-appsec/findings/003-idor.md`).
2. Impacto descrito (artefacto: `projects/m18-appsec/findings/003-idor.md`).
3. Ruta exacta (artefacto: `projects/m18-appsec/findings/003-idor.md`).
4. Commit `docs(m18): L17 idor-en-citas-y-recursos-por-id`.

## Errores comunes

- Probar en datos de design partner real.
- Autorización solo en front.

## Siguiente

[L18 — Autorización por rol owner vs staff](L18-autorizacion-por-rol-owner-vs-staff.md)
