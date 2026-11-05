---
id: L18
materia: M06
orden: 18
titulo: 'Semver, scripts y build'
horas: 5
semana: 5
lectura: semver.org; npm version docs
evidencia: CHANGELOG o sección Releases; scripts prepublishOnly
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Aplicar semver conscientemente; automatizar test+build antes
      de empaquetar; documentar cambios.


      Versionar comunica rupturas. Semver es contrato con consumidores.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura semver
    xp: 10
    cuerpo: |-
      ```json
      "scripts": {
        "test": "vitest run",
        "build": "tsc",
        "prepack": "npm run test && npm run build"
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Semver, scripts y build" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: CHANGELOG o sección Releases; scripts prepublishOnly
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es buena práctica en esta lección? “1.0.0 el día uno sin API estable."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Aplicar semver conscientemente; automatizar test+build antes de
          empaquetar; documentar cambios.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Scripts
    xp: 10
    cuerpo: |-
      ```json
      "scripts": {
        "test": "vitest run",
        "build": "tsc",
        "prepack": "npm run test && npm run build"
      }
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. CHANGELOG
    xp: 10
    cuerpo: 'Formato Keep a Changelog lite: Unreleased, 0.1.0 inicial.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Versión coherente con changelog.
      - '`prepack`/`prepublishOnly` evita pack roto.'
      - Tarball local instalable en proyecto de prueba (`npm i ../...tgz`).
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L18 — Semver, scripts y build

**~5 h · Semana 5**

Versionar comunica rupturas. Semver es contrato con consumidores.

## Objetivo

Aplicar semver conscientemente; automatizar test+build antes de empaquetar; documentar cambios.

## Pasos

### 1. Lectura semver (30 min)

MAJOR.MINOR.PATCH con ejemplos de tu API.

### 2. Scripts (60 min)

```json
"scripts": {
  "test": "vitest run",
  "build": "tsc",
  "prepack": "npm run test && npm run build"
}
```

### 3. CHANGELOG (90 min)

Formato Keep a Changelog lite: Unreleased, 0.1.0 inicial.

### 4. Simular release (60 min)

```bash
npm version patch -m "chore(m06): release %s"
npm pack
```

Inspecciona tarball.

### 5. Política API (30 min)

README sección **Estabilidad**: qué es público vs experimental.

## Hecho cuando

1. Versión coherente con changelog.
2. `prepack`/`prepublishOnly` evita pack roto.
3. Tarball local instalable en proyecto de prueba (`npm i ../...tgz`).

## Errores comunes

- 1.0.0 el día uno sin API estable.
- Olvidar bump en package.json.

## Siguiente

[L19 — README, API pública y ejemplos](L19-readme-api-y-ejemplos.md)
