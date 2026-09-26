---
id: L16
materia: M20
orden: 16
titulo: "AppSec móvil: no loguear PII ni tokens"
horas: 5.0
semana: 4
lectura: OWASP MASVS logging
evidencia: projects/m20-movil/logging-policy.md
---

# L16 — AppSec móvil: no loguear PII ni tokens

**~5.0 h · Semana 4**

Un logcat filtrado filtra tokens.

## Objetivo

Revisar print/debug; política de logs en dev vs release.

## Conceptos clave

- PII
- tokens
- crash reports

## Pasos (hazlos en orden)

### 1. Política de logging (50–60 min)

```bash
cat > projects/m20-movil/logging-policy.md << 'EOF'
# Logging móvil
Prohibido: tokens, passwords, teléfonos completos, bodies de auth.
Permitido: request id, status code, ruta sin query sensible.
EOF
rg -n "console\\.(log|debug)|print\\(|Log\\." projects/m20-movil/app 2>/dev/null | head || true
```

### 2. Commit (15 min)

```bash
git add projects/m20-movil/logging-policy.md
git commit -m "docs(m20): L16 logging policy appsec"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | OWASP MASVS logging | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m20-movil/logging-policy.md`; sin logs de tokens/PII en código revisado.
2. Commit `docs(m20): L16 appsec-movil-no-loguear-pii-ni-tokens`.

## Errores comunes

- `console.log` del Bearer token.
- Telemetría con teléfono completo.

## Siguiente

[L17 — Firma Android y keystore fuera del repo](L17-firma-android-y-keystore-fuera-del-repo.md)
