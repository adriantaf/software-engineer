---
id: L21
materia: M18
orden: 21
titulo: "SSRF: superficie en webhooks e integraciones"
horas: 5.0
semana: 6
lectura: SSRF Prevention Cheat Sheet
evidencia: projects/m18-appsec/findings/004-ssrf.md
---

# L21 — SSRF: superficie en webhooks e integraciones

**~5.0 h · Semana 6**

¿La API fetcha URLs controladas por usuario?

## Objetivo

Inventario SSRF (webhooks, previews, imports) + mitigación o N/A justificado.

## Pasos (hazlos en orden)

### 1. Busca fetch/axios a URLs user-controlled (50 min)

### 2. Documenta (60–70 min)

Allowlist, bloqueo link-local. PoC solo local.

### 3. Commit

`docs(m18): l21 superficie ssrf`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | SSRF Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc SSRF con allowlist (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
2. Riesgo nombrado (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
3. Sin escanear terceros (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
4. Commit `docs(m18): L21 ssrf-superficie-en-webhooks-e-integraciones`.

## Errores comunes

- curl a metadata cloud en prod.
- SSRF ‘para probar AWS’ en cuenta ajena.

## Siguiente

[L22 — Subida de archivos segura](L22-subida-de-archivos-segura.md)
