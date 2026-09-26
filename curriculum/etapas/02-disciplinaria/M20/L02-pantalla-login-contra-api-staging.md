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

Misma API que web M17.

## Objetivo

Implementar login email/password contra HTTPS M19; errores claros sin stack trace.

## Conceptos clave

- POST login
- 401 UX
- timeout

## Pasos (hazlos en orden)

### 1. Config API URL (30–40 min)

```dart
// Flutter ejemplo — adapta a RN
const apiBase = String.fromEnvironment('API_BASE', defaultValue: 'http://10.0.2.2:3000');
```

```bash
# Dev: apunta a staging M19 o local documentado en demo-login-lista.md
```

### 2. Pantalla login (90–110 min)

Email/password → `POST /auth/login`. Muestra error de red/credenciales.

```bash
# Prueba contra staging:
curl -sS -X POST "$API_BASE/auth/login" -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"***"}'
```

### 3. Commit (15 min)

```bash
echo "## Login" > projects/m20-movil/demo-login-lista.md
git add projects/m20-movil
git commit -m "feat(m20): L02 login contra api staging"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | HTTP client + auth API | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Login UI contra API documentada en `projects/m20-movil/demo-login-lista.md`.
2. Errores de red/credenciales visibles (artefacto: `projects/m20-movil/demo-login-lista.md (inicio)`).
3. Commit `docs(m20): L02 pantalla-login-contra-api-staging`.

## Errores comunes

- Mock eterno que nunca pega a staging.
- Hardcodear secrets de prod.

## Siguiente

[L03 — Secure storage de token o sesión](L03-secure-storage-de-token-o-sesion.md)
