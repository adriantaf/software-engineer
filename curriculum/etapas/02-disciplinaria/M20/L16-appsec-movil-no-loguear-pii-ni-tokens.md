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

MASVS logging: nada de tokens en Logcat.

## Objetivo

`docs/logging-policy.md` + grep limpio de logs sensibles.

## Pasos (hazlos en orden)

### 1. Política (30 min)

### 2. Audita logs (80–100 min)

Quita prints de responses con PII.

### 3. Commit

`fix(m20): l16 no log pii tokens`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | OWASP MASVS logging | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Política escrita (artefacto: `projects/m20-movil/logging-policy.md`).
2. Sin token en logs (artefacto: `projects/m20-movil/logging-policy.md`).
3. Commit limpieza si hubo (artefacto: `projects/m20-movil/logging-policy.md`).

## Errores comunes

- console.log(token).
- Sentry con PII.

## Siguiente

[L17 — Firma Android y keystore fuera del repo](L17-firma-android-y-keystore-fuera-del-repo.md)
