---
id: L20
materia: M20
orden: 20
titulo: Cierre M20 — dominio y README proyecto
horas: 5
semana: 5
lectura: Repaso M20
evidencia: projects/m20-movil/README.md índice
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Verificar P1–P3, criterios dominio, enlaces evidencia.

      - README
      - dominio
  - id: s2
    tipo: ejemplo
    titulo: 1. README índice proyecto
    xp: 10
    cuerpo: >-
      ```bash

      ls projects/m20-movil

      # README debe enlazar: stack-movil.md, auth-storage.md,
      demo-login-lista.md,

      # build-evidence.md, logging-policy.md, release-notes.md, repo-url.md

      rg -n "stack-movil|auth-storage|demo-login|build-evidence"
      projects/m20-movil/README.md

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M20 — dominio y README proyecto" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m20-movil/README.md índice
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

      `ls projects/m20-movil`
    comandoEsperado:
      - ls projects/m20-movil
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: ls projects/m20-movil'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Verificar P1–P3, criterios dominio, enlaces evidencia.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Commit cierre
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "docs(m20): L20 cierre dominio readme"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m20-movil/README.md` índice enlaza stack, auth-storage, demo,
        build, logging, release.
      - 'Commit `docs(m20): L20 cierre-m20-dominio-y-readme-proyecto`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L20 — Cierre M20 — dominio y README proyecto

**~5.0 h · Semana 5**

Cierras materia móvil antes de emprendimiento M22.

## Objetivo

Verificar P1–P3, criterios dominio, enlaces evidencia.

## Conceptos clave

- README
- dominio

## Pasos (hazlos en orden)

### 1. README índice proyecto (50–60 min)

```bash
ls projects/m20-movil
# README debe enlazar: stack-movil.md, auth-storage.md, demo-login-lista.md,
# build-evidence.md, logging-policy.md, release-notes.md, repo-url.md
rg -n "stack-movil|auth-storage|demo-login|build-evidence" projects/m20-movil/README.md
```

### 2. Commit cierre (15 min)

```bash
git add projects/m20-movil
git commit -m "docs(m20): L20 cierre dominio readme"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Flutter o React Native (stack elegido) | Repaso M20 | [Flutter get started](https://docs.flutter.dev/get-started/install) |
| Catálogo | Entrada de esta materia | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m20-movil/README.md` índice enlaza stack, auth-storage, demo, build, logging, release.
2. Commit `docs(m20): L20 cierre-m20-dominio-y-readme-proyecto`.

## Errores comunes

- README sin enlaces a evidencias.
- Código móvil sin URL/ruta.

## Siguiente

Etapa terminal: [M21 — Admin. proyectos](../../03-terminal/M21-admin-proyectos.md).
