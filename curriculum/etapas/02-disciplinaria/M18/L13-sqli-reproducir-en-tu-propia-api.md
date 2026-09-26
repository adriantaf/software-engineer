---
id: L13
materia: M18
orden: 13
titulo: "SQLi: reproducir en tu propia API"
horas: 5.0
semana: 4
lectura: OWASP A03 Injection + SQLi Prevention
evidencia: projects/m18-appsec/findings/001-sqli.md
---

# L13 — SQLi: reproducir en tu propia API

**~5.0 h · Semana 4**

Solo contra tu API. Busca concatenación SQL en búsquedas de cliente/cita.

## Objetivo

PoC SQLi o “no reproducible con ORM” con evidencia de query parametrizada.

## Pasos (hazlos en orden)

### 1. Caza (60 min)

`rg` de SQL string concat / `$query` peligrosos.

### 2. PoC (60–80 min)

Payload en campo búsqueda; captura en `pocs/sqli.md`. Si ORM puro: documenta intento fallido.

### 3. Commit

`docs(m18): l13 poc sqli`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A03 Injection + SQLi Prevention | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Finding documentado o prueba de mitigación (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
2. Solo tu entorno (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
3. Sin PII en el reporte (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
4. Commit `docs(m18): L13 sqli-reproducir-en-tu-propia-api`.

## Errores comunes

- SQLi en producción de terceros.
- Drop table en staging compartido.

## Siguiente

[L14 — Mitigar SQLi: queries parametrizadas y permisos DB](L14-mitigar-sqli-queries-parametrizadas-y-permisos-db.md)
