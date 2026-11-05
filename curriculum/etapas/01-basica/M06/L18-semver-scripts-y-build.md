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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Versionar comunica rupturas. Semver es contrato con consumidores.


      **Objetivo de esta lección:** Aplicar semver conscientemente; automatizar
      test+build antes de empaquetar; documentar cambios.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura semver
    xp: 10
    cuerpo: |-
      ```json
      "scripts": {
        "test": "vitest run",
        "build": "tsc",
        "prepack": "npm run test && npm run build"
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Scripts
    xp: 10
    cuerpo: |-
      ```json
      "scripts": {
        "test": "vitest run",
        "build": "tsc",
        "prepack": "npm run test && npm run build"
      }
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Semver, scripts y build», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: Versión coherente con changelog.
      - id: b
        texto: 'Instalar herramientas al azar sin evidencia de Semver, scripts y build'
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: ¿Es recomendable en esta lección? “1.0.0 el día uno sin API estable."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: >-
          Aplicar semver conscientemente; automatizar test+build antes de
          empaquetar; documentar cambios.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: CHANGELOG
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
