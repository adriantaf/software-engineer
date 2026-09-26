---
id: L03
materia: M20
orden: 3
titulo: Secure storage de token o sesión
horas: 5.0
semana: 1
lectura: Keychain / Keystore vía lib oficial
evidencia: projects/m20-movil/auth-storage.md
---

# L03 — Secure storage de token o sesión

**~5.0 h · Semana 1**

Keychain/Keystore — no SharedPreferences en claro.

## Objetivo

`auth-storage.md` + implementación secure storage.

## Pasos (hazlos en orden)

### 1. Elige API (30 min)

flutter_secure_storage / Keychain RN.

### 2. Implementa (80–100 min)

Guarda/lee/borra token. Nunca loguees el valor.

### 3. Doc (20 min)

### 4. Commit

`feat(m20): l03 secure storage`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Keychain / Keystore vía lib oficial | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. auth-storage.md (artefacto: `projects/m20-movil/auth-storage.md`).
2. código referenciado (artefacto: `projects/m20-movil/auth-storage.md`).
3. sin password claro (artefacto: `projects/m20-movil/auth-storage.md`).
4. Commit `docs(m20): L03 secure-storage-de-token-o-sesion`.

## Errores comunes

- Token en logs.
- AsyncStorage plano.

## Siguiente

[L04 — Errores de validación y flujo 401](L04-errores-de-validacion-y-flujo-401.md)
