---
id: L22
materia: M17
orden: 22
titulo: Deploy staging en PaaS
horas: 5
semana: 6
lectura: Docs PaaS elegido
evidencia: URL staging
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - deploy

      - staging

      - build


      **Objetivo de esta lección:** Desplegar API+front o API primero en staging
      con build reproducible.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige PaaS y despliega
    xp: 10
    cuerpo: >-
      ```bash

      # ejemplo genérico — sustituye por CLI real

      # fly launch / render blueprint / railway up

      curl -sS https://TU-STAGING.example/health

      ```


      Fly/Render/Railway/etc. Build desde Dockerfile o buildpack. Secrets en el
      panel, no en git.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Documenta URL
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m17-vitrina/docs

      echo "Staging: https://TU-STAGING.example" >
      projects/m17-vitrina/docs/deploy.md

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Deploy staging en PaaS», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Deploy staging en PaaS
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

      `curl -sS https://TU-STAGING.example/health`
    comandoEsperado:
      - 'curl -sS https://TU-STAGING.example/health'
      - mkdir -p projects/m17-vitrina/docs
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: curl -sS https://TU-STAGING.example/health'
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
        texto: Desplegar API+front o API primero en staging con build reproducible.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m17-vitrina/docs/deploy.md
      git commit -m "docs(m17): L22 deploy staging paas"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`projects/m17-vitrina/docs/deploy.md` incluye URL staging alcanzable.'
      - 'Commit `docs(m17): L22 deploy-staging-en-paas`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L22 — Deploy staging en PaaS

**~5.0 h · Semana 6**

Piloto invisible no es piloto.

## Objetivo

Desplegar API+front o API primero en staging con build reproducible.

## Conceptos clave

- deploy
- staging
- build

## Pasos (hazlos en orden)

### 1. Elige PaaS y despliega (90–120 min)

Fly/Render/Railway/etc. Build desde Dockerfile o buildpack. Secrets en el panel, no en git.

```bash
# ejemplo genérico — sustituye por CLI real
# fly launch / render blueprint / railway up
curl -sS https://TU-STAGING.example/health
```

### 2. Documenta URL (30 min)

```bash
mkdir -p projects/m17-vitrina/docs
echo "Staging: https://TU-STAGING.example" > projects/m17-vitrina/docs/deploy.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/deploy.md
git commit -m "docs(m17): L22 deploy staging paas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Docs PaaS elegido | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/deploy.md` incluye URL staging alcanzable.
2. Commit `docs(m17): L22 deploy-staging-en-paas`.

## Errores comunes

- URL staging solo en chat, no en `docs/deploy.md`.
- Secrets en variables del Dockerfile.

## Siguiente

[L23 — HTTPS y health checks](L23-https-y-health-checks.md)
