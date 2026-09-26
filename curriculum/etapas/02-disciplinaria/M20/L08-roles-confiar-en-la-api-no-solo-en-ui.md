---
id: L08
materia: M20
orden: 8
titulo: "Roles: confiar en la API, no solo en UI"
horas: 5.0
semana: 2
lectura: RBAC móvil
evidencia: nota rbac en demo-login-lista.md
---

# L08 — Roles: confiar en la API, no solo en UI

**~5.0 h · Semana 2**

Ocultar botón ≠ autorización.

## Objetivo

Staff no ejecuta acción owner aunque parchee la UI; demo + nota.

## Pasos (hazlos en orden)

### 1. Lee rol de `/me` (40 min)

### 2. UI condicional + prueba API (80–100 min)

Forzar llamada staff a endpoint owner → 403 manejado.

### 3. Commit

`feat(m20): l08 roles confiar api`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | RBAC móvil | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Prueba rol documentada (artefacto: `nota rbac en demo-login-lista.md`).
2. 403 UX (artefacto: `nota rbac en demo-login-lista.md`).
3. Sin lógica secreta solo UI (artefacto: `nota rbac en demo-login-lista.md`).
4. Commit `docs(m20): L08 roles-confiar-en-la-api-no-solo-en-ui`.

## Errores comunes

- Admin hardcoded en app.
- Ignorar 403.

## Siguiente

[L09 — Pantalla detalle de cita](L09-pantalla-detalle-de-cita.md)
