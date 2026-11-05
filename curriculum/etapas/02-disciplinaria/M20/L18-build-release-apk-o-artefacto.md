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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - release

      - minify opcional


      **Objetivo de esta lección:** Generar APK/AAB o IPA test; SHA commit y
      dispositivo prueba.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Build release
    xp: 10
    cuerpo: |-
      ```bash
      # Flutter: flutter build apk --release
      # RN: cd android && ./gradlew assembleRelease
      ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta artefacto
    xp: 10
    cuerpo: |-
      ```bash
      # Flutter: flutter build apk --release
      # RN: cd android && ./gradlew assembleRelease
      ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Build release APK o artefacto», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Build release APK o
          artefacto
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*`
    comandoEsperado:
      - ls -lh **/app-release.apk 2>/dev/null || ls -lh **/outputs/apk/release/*
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: ls -lh **/app-release.apk 2>/dev/null || ls -lh
      **/outputs/apk/release/*
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: Generar APK/AAB o IPA test; SHA commit y dispositivo prueba.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Artefacto no instalado en dispositivo."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m20-movil/build-evidence.md` con artefacto release e
        instalación.
      - 'Commit `docs(m20): L18 build-release-apk-o-artefacto`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
