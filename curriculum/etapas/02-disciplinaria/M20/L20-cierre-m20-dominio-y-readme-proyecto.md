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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - README

      - dominio


      **Objetivo de esta lección:** Verificar P1–P3, criterios dominio, enlaces
      evidencia.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: README índice proyecto
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit cierre
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m20-movil
      git commit -m "docs(m20): L20 cierre dominio readme"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M20 — dominio y README proyecto», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M20 — dominio y
          README proyecto
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: 'Verificar P1–P3, criterios dominio, enlaces evidencia.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git add projects/m20-movil`
    comandoEsperado:
      - git add projects/m20-movil
    explicacionError: 'Esperado: git add projects/m20-movil'
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M20
    xp: 25
    enunciado: >-
      Cierra **Aplicaciones móviles** con evidencia real en el repo. Marca la
      rúbrica solo si puedes demostrar cada criterio (si no está en git, no
      cuenta).
    entregables:
      - 'P1: App cliente: login + lista de pedidos'
      - 'P2: Estados vacíos/error + storage seguro de sesión'
      - 'P3: Build instalable (APK o equivalente)'
      - 'Proyecto: App móvil de Vitrina conectada al backend'
      - projects/m20-movil/README.md índice
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          `projects/m20-movil/README.md` índice enlaza stack, auth-storage,
          demo, build, logging, release.
      - id: r3
        criterio: 'Commit `docs(m20): L20 cierre-m20-dominio-y-readme-proyecto`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m20-movil/README.md` índice enlaza stack, auth-storage, demo,
        build, logging, release.
      - 'Commit `docs(m20): L20 cierre-m20-dominio-y-readme-proyecto`.'
    siguiente: Materia M20 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
