---
id: L04
materia: M20
orden: 4
titulo: Errores de validación y flujo 401
horas: 5.0
semana: 1
lectura: Interceptors HTTP
evidencia: commit + nota en auth-storage.md
---

# L04 — Errores de validación y flujo 401

**~5.0 h · Semana 1**

401 → limpiar storage y volver a login.

## Objetivo

Interceptor/wrapper HTTP con 401 global; mensajes de validación legibles.

## Pasos (hazlos en orden)

### 1. Interceptor (70–90 min)

### 2. Prueba (40 min)

Token inválido fuerza login. Evidencia en checklist.

### 3. Commit

`feat(m20): l04 flujo 401`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Interceptors HTTP | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. 401 redirige login (artefacto: `commit`).
2. Loading/error UI (artefacto: `commit`).
3. Commit (artefacto: `commit`).

## Errores comunes

- Stack trace al usuario.
- Ignorar 401.

## Siguiente

[L05 — Lista de citas autenticada](L05-lista-de-citas-autenticada.md)
