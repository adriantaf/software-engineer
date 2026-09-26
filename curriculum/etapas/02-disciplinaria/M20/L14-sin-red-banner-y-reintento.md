---
id: L14
materia: M20
orden: 14
titulo: "Sin red: banner y reintento"
horas: 5.0
semana: 4
lectura: Connectivity plugins
evidencia: captura offline
---

# L14 — Sin red: banner y reintento

**~5.0 h · Semana 4**

Dueño en campo pierde señal a menudo.

## Objetivo

Detectar offline o fallo DNS; banner y botón reintentar.

## Conceptos clave

- offline
- retry

## Pasos (hazlos en orden)

### 1. Banner offline (60–80 min)

```dart
// connectivity_plus / NetInfo → banner "Sin red" + botón Reintentar
```

### 2. Prueba avión (30 min)

```bash
# Activa modo avión → banner visible → reintento al volver
echo "Offline OK $(date -I)" >> projects/m20-movil/demo-login-lista.md
git add projects/m20-movil
git commit -m "feat(m20): L14 banner sin red reintento"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Connectivity plugins | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Banner offline + reintento demostrado (modo avión) (artefacto: `captura offline`).
2. Commit `docs(m20): L14 sin-red-banner-y-reintento`.

## Errores comunes

- Crash sin red.
- Sin botón reintentar.

## Siguiente

[L15 — Timeout, 5xx y mensajes humanos](L15-timeout-5xx-y-mensajes-humanos.md)
