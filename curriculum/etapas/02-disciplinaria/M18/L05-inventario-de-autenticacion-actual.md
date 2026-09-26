---
id: L05
materia: M18
orden: 5
titulo: Inventario de autenticación actual
horas: 5.0
semana: 2
lectura: OWASP A07 + Authentication Cheat Sheet
evidencia: projects/m18-appsec/auth-inventory.md
---

# L05 — Inventario de autenticación actual

**~5.0 h · Semana 2**

Antes de endurecer, documentas qué hay en M17.

## Objetivo

`docs/auth-inventario.md`: mecanismo, almacenamiento token/sesión, endpoints auth.

## Pasos (hazlos en orden)

### 1. Inspección código (60–80 min)

Dónde se hashea, dónde se setea cookie, refresh o no.

### 2. Tabla riesgos (40–50 min)

localStorage vs cookie; falta rotación; logout incompleto.

### 3. Commit

`docs(m18): l05 inventario autenticacion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A07 + Authentication Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Inventario con endpoints reales (artefacto: `projects/m18-appsec/auth-inventory.md`).
2. Público vs autenticado claro (artefacto: `projects/m18-appsec/auth-inventory.md`).
3. Sin passwords en el doc (artefacto: `projects/m18-appsec/auth-inventory.md`).
4. Commit `docs(m18): L05 inventario-de-autenticacion-actual`.

## Errores comunes

- Inventario teórico sin abrir el código.
- Loguear tokens en dev.

## Siguiente

[L06 — Hashing de contraseñas con bcrypt o argon2](L06-hashing-de-contrasenas-con-bcrypt-o-argon2.md)
