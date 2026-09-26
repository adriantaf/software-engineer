---
id: L18
materia: M20
orden: 18
titulo: Build release APK o artefacto
horas: 5.0
semana: 5
lectura: Release build oficial
evidencia: projects/m20-movil/build-evidence.md
---

# L18 — Build release APK o artefacto

**~5.0 h · Semana 5**

Emulador no basta para P3.

## Objetivo

Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.

## Conceptos clave

- release
- minify opcional

## Pasos (hazlos en orden)

### 1. Build release (80–110 min)

```bash
# Flutter: flutter build apk --release
# RN: cd android && ./gradlew assembleRelease
ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
```

### 2. Documenta artefacto (30 min)

```bash
cat >> projects/m20-movil/build-evidence.md << 'EOF'
## Release
Fecha: …  Hash/archivo: app-release.apk  Instalado en dispositivo: sí/no
EOF
git add projects/m20-movil/build-evidence.md
git commit -m "docs(m20): L18 build release apk"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Release build oficial | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/build-evidence.md` con artefacto release e instalación.
2. Commit `docs(m20): L18 build-release-apk-o-artefacto`.

## Errores comunes

- Solo debug APK como ‘release’.
- Artefacto no instalado en dispositivo.

## Siguiente

[L19 — Release notes y demo cruzada con web](L19-release-notes-y-demo-cruzada-con-web.md)
