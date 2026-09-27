---
id: L15
materia: M20
orden: 15
titulo: Timeout, 5xx y mensajes humanos
horas: 5.0
semana: 4
lectura: HTTP timeouts
evidencia: nota en demo doc
---

# L15 — Timeout, 5xx y mensajes humanos

**~5.0 h · Semana 4**

No todo es ‘algo salió mal’.

## Objetivo

Configurar timeout cliente; distinguir 5xx de error usuario.

## Conceptos clave

- timeout
- 5xx

## Pasos (hazlos en orden)

### 1. Timeouts y 5xx (60–80 min)

```ts
// timeout 10–15s → mensaje "El servidor no respondió"
// 502/503 → "Estamos reiniciando — reintenta"
```

### 2. Nota + commit (30 min)

```bash
cat >> projects/m20-movil/demo-login-lista.md << 'EOF'
## Timeouts / 5xx
Mensajes humanos documentados; no stack traces al usuario.
EOF
git add projects/m20-movil
git commit -m "feat(m20): L15 timeout 5xx mensajes humanos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | HTTP timeouts | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Timeouts/5xx muestran mensajes humanos (sin stack traces).
2. Commit `docs(m20): L15 timeout-5xx-y-mensajes-humanos`.

## Errores comunes

- Mostrar stack trace al usuario.
- Timeout infinito.

## Siguiente

[L16 — AppSec móvil: no loguear PII ni tokens](L16-appsec-movil-no-loguear-pii-ni-tokens.md)
