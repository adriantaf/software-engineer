---
id: L26
materia: M18
orden: 26
titulo: Secretos, .env y rotación
horas: 5.0
semana: 7
lectura: Secrets Management Cheat Sheet
evidencia: projects/m18-appsec/secrets-rotation.md
---

# L26 — Secretos, .env y rotación

**~5.0 h · Semana 7**

Historial git no debe tener SESSION_SECRET real.

## Objetivo

Inventario secretos; rotación documentada; grep limpio.

## Pasos (hazlos en orden)

### 1. Busca fugas (50 min)

`git log -p | rg -i 'password|secret|api_key' | head` (cuidado output).

### 2. Proceso rotación (60–70 min)

`docs/rotacion-secretos.md` pasos staging.

### 3. Commit

`docs(m18): l26 secretos rotacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Secrets Management Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Inventario sin valores (artefacto: `projects/m18-appsec/secrets-rotation.md`).
2. grep historial ejecutado (artefacto: `projects/m18-appsec/secrets-rotation.md`).
3. Plan rotación (artefacto: `projects/m18-appsec/secrets-rotation.md`).
4. Commit `docs(m18): L26 secretos-env-y-rotacion`.

## Errores comunes

- Pegar secretos en issue.
- Rotar sin probar logout.

## Siguiente

[L27 — Cabeceras de seguridad con Helmet o equivalente](L27-cabeceras-de-seguridad-con-helmet-o-equivalente.md)
