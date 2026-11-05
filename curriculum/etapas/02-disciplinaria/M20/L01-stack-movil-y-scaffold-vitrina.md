---
id: L01
materia: M20
orden: 1
titulo: Stack móvil y scaffold Vitrina
horas: 5
semana: 1
lectura: Flutter o RN — get started
evidencia: projects/m20-movil/stack.md + repo-url.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Elegir Flutter o RN, documentar SDK, crear scaffold y
      enlazar repo.


      - Flutter vs RN

      - staging URL

      - lint
  - id: s2
    tipo: ejemplo
    titulo: 1. Decide Flutter o RN
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m20-movil/docs
      cat > projects/m20-movil/stack-movil.md << 'EOF'
      # Stack móvil Vitrina
      - Elección: Flutter X.Y  **o** React Native X.Y
      - Por qué: …
      - SDK / JDK: …
      - No cambiar sin ADR
      EOF
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Stack móvil y scaffold Vitrina" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/stack.md + repo-url.md
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

      `mkdir -p projects/m20-movil/docs`
    comandoEsperado:
      - mkdir -p projects/m20-movil/docs
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m20-movil/docs'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Elegir Flutter o RN, documentar SDK, crear scaffold y enlazar repo.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Scaffold app
    xp: 10
    cuerpo: >-
      ```bash

      Flutter:

      flutter create vitrina_app

      React Native:

      npx @react-native-community/cli init VitrinaApp

      ```


      App corre en emulador/dispositivo. Deja el código en submódulo o
      `projects/m20-movil/app/` y enlázalo en README.
  - id: s7
    tipo: ejemplo
    titulo: 3. Evidencia + commit
    xp: 10
    cuerpo: |-
      ```bash
      cat > projects/m20-movil/repo-url.md << 'EOF'
      # Código móvil
      Repo / ruta: …
      Commit scaffold: …
      EOF
      # README m20 apunta a repo-url.md y stack-movil.md
      git add projects/m20-movil
      git commit -m "docs(m20): L01 scaffold stack movil"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existen `projects/m20-movil/stack-movil.md` y
        `projects/m20-movil/repo-url.md`.
      - Scaffold corre en emulador/dispositivo; README enlaza el código.
      - 'Commit `docs(m20): L01 stack-movil-y-scaffold-vitrina`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L01 — Stack móvil y scaffold Vitrina

**~5.0 h · Semana 1**

Un framework, un camino hasta M20 cierre.

## Objetivo

Elegir Flutter o RN, documentar SDK, crear scaffold y enlazar repo.

## Conceptos clave

- Flutter vs RN
- staging URL
- lint

## Pasos (hazlos en orden)

### 1. Decide Flutter o RN (25–35 min)

```bash
mkdir -p projects/m20-movil/docs
cat > projects/m20-movil/stack-movil.md << 'EOF'
# Stack móvil Vitrina
- Elección: Flutter X.Y  **o** React Native X.Y
- Por qué: …
- SDK / JDK: …
- No cambiar sin ADR
EOF
```

### 2. Scaffold app (90–110 min)

```bash
# Flutter:
# flutter create vitrina_app
# React Native:
# npx @react-native-community/cli init VitrinaApp
```

App corre en emulador/dispositivo. Deja el código en submódulo o `projects/m20-movil/app/` y enlázalo en README.

### 3. Evidencia + commit (30 min)

```bash
cat > projects/m20-movil/repo-url.md << 'EOF'
# Código móvil
Repo / ruta: …
Commit scaffold: …
EOF
# README m20 apunta a repo-url.md y stack-movil.md
git add projects/m20-movil
git commit -m "docs(m20): L01 scaffold stack movil"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Flutter o RN — get started | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. Existen `projects/m20-movil/stack-movil.md` y `projects/m20-movil/repo-url.md`.
2. Scaffold corre en emulador/dispositivo; README enlaza el código.
3. Commit `docs(m20): L01 stack-movil-y-scaffold-vitrina`.

## Errores comunes

- Cambiar Flutter↔RN en semana 3 sin ADR.
- Scaffold sin versión de SDK.

## Siguiente

[L02 — Pantalla login contra API staging](L02-pantalla-login-contra-api-staging.md)
