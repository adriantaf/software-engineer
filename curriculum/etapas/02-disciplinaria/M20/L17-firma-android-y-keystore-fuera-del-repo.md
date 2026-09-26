---
id: L17
materia: M20
orden: 17
titulo: Firma Android y keystore fuera del repo
horas: 5.0
semana: 5
lectura: Android signing / iOS profiles
evidencia: projects/m20-movil/build-evidence.md (prep)
---

# L17 — Firma Android y keystore fuera del repo

**~5.0 h · Semana 5**

Keystore ≠ git.

## Objetivo

Keystore local + `.gitignore`; doc de firmado en `build-evidence.md` borrador.

## Pasos (hazlos en orden)

### 1. Genera keystore (50–60 min)

### 2. Config signing (70–90 min)

Sin passwords en repo.

### 3. Commit

`docs(m20): l17 keystore fuera repo`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Android signing / iOS profiles | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Keystore fuera git (artefacto: `projects/m20-movil/build-evidence.md (prep)`).
2. gitignore (artefacto: `projects/m20-movil/build-evidence.md (prep)`).
3. Doc comando (artefacto: `projects/m20-movil/build-evidence.md (prep)`).
4. Commit `docs(m20): L17 firma-android-y-keystore-fuera-del-repo`.

## Errores comunes

- Keystore commiteado.
- Password en gradle commiteado.

## Siguiente

[L18 — Build release APK o artefacto](L18-build-release-apk-o-artefacto.md)
