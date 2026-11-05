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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Desplegar API+front o API primero en staging con build
      reproducible.


      - deploy

      - staging

      - build
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige PaaS y despliega
    xp: 10
    cuerpo: |-
      ```bash
      # ejemplo genérico — sustituye por CLI real
      # fly launch / render blueprint / railway up
      curl -sS https://TU-STAGING.example/health
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Deploy staging en PaaS" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: URL staging
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

      `curl -sS https://TU-STAGING.example/health`
    comandoEsperado:
      - 'curl -sS https://TU-STAGING.example/health'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: curl -sS https://TU-STAGING.example/health'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Desplegar API+front o API primero en staging con build reproducible.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Documenta URL
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p projects/m17-vitrina/docs

      echo "Staging: https://TU-STAGING.example" >
      projects/m17-vitrina/docs/deploy.md

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
