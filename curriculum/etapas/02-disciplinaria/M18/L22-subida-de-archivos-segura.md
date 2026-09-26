---
id: L22
materia: M18
orden: 22
titulo: Subida de archivos segura
horas: 5.0
semana: 6
lectura: File Upload Cheat Sheet
evidencia: projects/m18-appsec/findings/005-upload.md
---

# L22 — Subida de archivos segura

**~5.0 h · Semana 6**

Si no hay uploads, documenta N/A; si hay, endurece.

## Objetivo

Política: tipos MIME, tamaño, path traversal, no ejecutar en mismo origen.

## Pasos (hazlos en orden)

### 1. Inventario (30 min)

### 2. Controles o N/A (80–100 min)

Evidencia en `docs/uploads.md`.

### 3. Commit

`docs(m18): l22 uploads seguros`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | File Upload Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Checklist o prueba real (artefacto: `projects/m18-appsec/findings/005-upload.md`).
2. Ruta almacenamiento (artefacto: `projects/m18-appsec/findings/005-upload.md`).
3. Sin ejecución de uploads (artefacto: `projects/m18-appsec/findings/005-upload.md`).
4. Commit `docs(m18): L22 subida-de-archivos-segura`.

## Errores comunes

- Guardar en `public/` con nombre usuario.
- Confiar en extensión.

## Siguiente

[L23 — Deserialización y JSON peligroso](L23-deserializacion-y-json-peligroso.md)
