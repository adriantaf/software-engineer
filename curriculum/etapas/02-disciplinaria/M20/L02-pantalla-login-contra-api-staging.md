---
id: L02
materia: M20
orden: 2
titulo: Pantalla login contra API staging
horas: 5.0
semana: 1
lectura: HTTP client + auth API
evidencia: projects/m20-movil/demo-login-lista.md (inicio)
---

# L02 — Pantalla login contra API staging

**~5.0 h · Semana 1**

Misma auth que la web: nada de mock eterno.

## Objetivo

Login UI → `POST /auth/login` staging/local documentado.

## Pasos (hazlos en orden)

### 1. Config API URL (30 min)

Flavor dev/staging. No hardcode prod secrets.

### 2. Pantalla login (90–110 min)

Email/password; maneja errores red.

### 3. Commit

`feat(m20): l02 login contra api`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | HTTP client + auth API | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Login feliz (artefacto: `projects/m20-movil/demo-login-lista.md (inicio)`).
2. 401 mensaje humano (artefacto: `projects/m20-movil/demo-login-lista.md (inicio)`).
3. HTTPS.
4. Commit `docs(m20): L02 pantalla-login-contra-api-staging`.

## Errores comunes

- localhost en release.
- Password en logs.

## Siguiente

[L03 — Secure storage de token o sesión](L03-secure-storage-de-token-o-sesion.md)
