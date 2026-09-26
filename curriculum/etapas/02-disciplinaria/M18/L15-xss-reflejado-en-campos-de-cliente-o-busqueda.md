---
id: L15
materia: M18
orden: 15
titulo: XSS reflejado en campos de cliente o búsqueda
horas: 5.0
semana: 4
lectura: XSS Prevention Cheat Sheet
evidencia: projects/m18-appsec/findings/002-xss-reflected.md
---

# L15 — XSS reflejado en campos de cliente o búsqueda

**~5.0 h · Semana 4**

Busca reflejo de input en HTML.

## Objetivo

PoC XSS reflejado en tu UI o evidencia de escape; entrada en tabla hallazgos.

## Pasos (hazlos en orden)

### 1. Prueba (70–90 min)

Payloads simples en nombre/búsqueda. Solo tu staging.

### 2. Documenta (40 min)

`pocs/xss-reflected.md` con pasos y resultado.

### 3. Commit

`docs(m18): l15 poc xss reflejado`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | XSS Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. PoC documentada (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
2. Contexto identificado (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
3. Sin atacar usuarios reales (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
4. Commit `docs(m18): L15 xss-reflejado-en-campos-de-cliente-o-busqueda`.

## Errores comunes

- XSS persistente en prod sin aviso.
- Confiar en ‘React escapa todo’.

## Siguiente

[L16 — XSS almacenado y escape en plantillas/API](L16-xss-almacenado-y-escape-en-plantillas-api.md)
