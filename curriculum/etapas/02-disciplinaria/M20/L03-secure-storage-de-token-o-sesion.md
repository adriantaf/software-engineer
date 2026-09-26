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

JWT en SharedPreferences plano es hallazgo M18.

## Objetivo

Persistir access token con flutter_secure_storage o equivalente RN; documentar qué guardas.

## Conceptos clave

- secure storage
- no password disk

## Pasos (hazlos en orden)

### 1. Elige secure storage (30 min)

```bash
# Flutter: flutter_secure_storage
# RN: react-native-keychain / expo-secure-store
cat > projects/m20-movil/auth-storage.md << 'EOF'
# Auth storage
API: …  Dónde vive el token/sesión: Keychain/Keystore
Nunca: SharedPreferences / AsyncStorage en claro
EOF
```

### 2. Implementa save/read/clear (80–100 min)

```ts
// pseudocódigo RN
await Keychain.setGenericPassword('session', token);
// NUNCA console.log(token)
```

Tras login guarda; al logout borra.

### 3. Commit (15 min)

```bash
git add projects/m20-movil
git commit -m "feat(m20): L03 secure storage sesion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Keychain / Keystore vía lib oficial | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/auth-storage.md` + implementación Keychain/Keystore (no texto claro).
2. Commit `docs(m20): L03 secure-storage-de-token-o-sesion`.

## Errores comunes

- Token en SharedPreferences/AsyncStorage en claro.
- Loguear el token.

## Siguiente

[L04 — Errores de validación y flujo 401](L04-errores-de-validacion-y-flujo-401.md)
