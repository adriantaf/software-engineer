---
id: L16
materia: M13
orden: 16
titulo: ADR auth y sesión
horas: 5.0
semana: 4
lectura: Sesión vs JWT; cookie HttpOnly; roles owner/staff
evidencia: adr/003-auth-sesion.md
---

# L16 — ADR auth y sesión

**~5.0 h · Semana 4**

Cierras la decisión que L07 dibujó: cómo autenticamos el piloto.

## Objetivo

`adr/003-auth-sesion.md` coherente con `secuencia-auth.md` y boundaries.

## Pasos (hazlos en orden)

### 1. Alternativas (40 min)

Tabla: sesión servidor / JWT cookie / JWT bearer. Elige una para el piloto.

### 2. ADR (70–90 min)

Incluye: hash de passwords, expiración, logout, roles, rechazo de “rol en query string”.

### 3. Sincroniza diagrama (30 min)

Si cambió el mecanismo, actualiza `secuencia-auth.md`.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno
git commit -m "docs(m13): ADR 003 auth y sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Decisión de autenticación/sesión y roles del piloto | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR 003 elige mecanismo (p. ej. cookie de sesión) con consecuencias.
2. Roles owner/staff y dónde se autorizan (API) quedan escritos.
3. Commit `docs(m13): ADR 003 auth y sesion`.

## Errores comunes

- JWT en localStorage “porque tutorial” sin amenazas.
- Roles solo en el front.
- ADR que contradice secuencia-auth sin actualizarla.

## Siguiente

[L17 — Índice del paquete de diseño](L17-indice-del-paquete-de-diseno.md)
