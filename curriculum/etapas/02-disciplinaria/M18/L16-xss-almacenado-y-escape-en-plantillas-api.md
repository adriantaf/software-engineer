---
id: L16
materia: M18
orden: 16
titulo: XSS almacenado y escape en plantillas/API
horas: 5.0
semana: 4
lectura: DOM XSS + stored XSS
evidencia: commit fix + findings/002 actualizado
---

# L16 — XSS almacenado y escape en plantillas/API

**~5.0 h · Semana 4**

Notas de cita/cliente son candidatas clásicas.

## Objetivo

PoC stored XSS o fix escape/encoding; no confiar solo en CSP aún.

## Pasos (hazlos en orden)

### 1. Inserta payload (50 min)

Guarda `<script>` en nota (seed/test user).

### 2. Verifica render (50–60 min)

¿Ejecuta? Fix con escape del framework. Test.

### 3. Commit

`fix(m18): l16 xss almacenado escape`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | DOM XSS + stored XSS | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥2 filas en findings-table (artefacto: `commit fix`).
2. Fix committed (artefacto: `commit fix`).
3. Test o verificación manual repetible (artefacto: `commit fix`).

## Errores comunes

- strip_tags inventado.
- innerHTML con input usuario.

## Siguiente

[L17 — IDOR en citas y recursos por ID](L17-idor-en-citas-y-recursos-por-id.md)
