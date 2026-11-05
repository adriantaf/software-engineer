---
id: L18
materia: M20
orden: 18
titulo: Build release APK o artefacto
horas: 5
semana: 5
lectura: Release build oficial
evidencia: projects/m20-movil/build-evidence.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.

      - release
      - minify opcional
  - id: s2
    tipo: ejemplo
    titulo: 1. Build release
    xp: 10
    cuerpo: |-
      ```bash
      # Flutter: flutter build apk --release
      # RN: cd android && ./gradlew assembleRelease
      ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Build release APK o artefacto" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/build-evidence.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*`
    comandoEsperado:
      - ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: ls -lh **/app-release.apk 2>/dev/null || ls -lh
      **/outputs/apk/release/*
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta artefacto
    xp: 10
    cuerpo: |-
      ```bash
      cat >> projects/m20-movil/build-evidence.md << 'EOF'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m20-movil/build-evidence.md` con artefacto release e
        instalación.
      - 'Commit `docs(m20): L18 build-release-apk-o-artefacto`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
