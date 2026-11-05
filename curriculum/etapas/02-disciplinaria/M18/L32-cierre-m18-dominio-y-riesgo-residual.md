---
id: L32
materia: M18
orden: 32
titulo: Cierre M18 — dominio y riesgo residual
horas: 5
semana: 8
lectura: Repaso completo M18
evidencia: projects/m18-appsec/informe-appsec.md final + README
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Riesgo residual explícito > “somos seguros”. Cierra P1–P3 y handoff a
      M19/M25.


      **Objetivo de esta lección:** `projects/m18-appsec/informe-appsec.md`
      final + README con residual top-3 y criterios de dominio.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría de evidencias
    xp: 10
    cuerpo: >-
      ```bash

      ls -la projects/m18-appsec projects/m18-appsec/docs
      projects/m18-appsec/findings projects/m18-appsec/ci
      projects/m18-appsec/pocs

      test -f projects/m18-appsec/threat-model-v1.md && echo P1=ok

      wc -l projects/m18-appsec/findings-table.md

      test -f projects/m18-appsec/ci/ci-appsec.yml && echo P3=ok

      test -f projects/m18-appsec/docs/auth-inventario.md && echo auth=ok

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Residual + handoff
    xp: 10
    cuerpo: >-
      ```bash

      printf "\n## Riesgo residual (cierre)\n| Riesgo | Dueño | Fecha revisión
      |\n|--------|-------|----------------|\n| … | | |\n\n## Handoff\n- M19:
      secrets en PaaS, HTTPS, backups\n- M25: retest en trial\n" >>
      projects/m18-appsec/informe-appsec.md

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M18 — dominio y riesgo residual», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M18 — dominio y
          riesgo residual
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `ls -la projects/m18-appsec projects/m18-appsec/docs
      projects/m18-appsec/findings projects/m18-appsec/ci
      projects/m18-appsec/pocs`
    comandoEsperado:
      - >-
        ls -la projects/m18-appsec projects/m18-appsec/docs
        projects/m18-appsec/findings projects/m18-appsec/ci
        projects/m18-appsec/pocs
      - >-
        git add projects/m18-appsec/README.md
        projects/m18-appsec/informe-appsec.md
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: ls -la projects/m18-appsec projects/m18-appsec/docs
      projects/m18-appsec/findings projects/m18-appsec/ci
      projects/m18-appsec/pocs
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
          `projects/m18-appsec/informe-appsec.md` final + README con residual
          top-3 y criterios de dominio.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M18
    xp: 25
    enunciado: >-
      Cierra **Seguridad del software (AppSec)** con evidencia real en el repo.
      Marca la rúbrica solo si puedes demostrar cada criterio (si no está en
      git, no cuenta).
    entregables:
      - 'P1: Threat model STRIDE de Vitrina (documento)'
      - 'P2: Reproducir y corregir ≥5 hallazgos OWASP en tu app'
      - 'P3: Checklist Secure SDLC en CI (audit, secrets, headers)'
      - 'Proyecto: Informe AppSec + PR de hardening con tests de regresión'
      - projects/m18-appsec/informe-appsec.md final + README
    rubrica:
      - id: r1
        criterio: 'Marca la lección solo si:'
      - id: r2
        criterio: >-
          Informe final (artefacto: `projects/m18-appsec/informe-appsec.md
          final`).
      - id: r3
        criterio: >-
          P1–P3 verificables (artefacto: `projects/m18-appsec/informe-appsec.md
          final`).
      - id: r4
        criterio: 'Commit `docs(m18): L32 cierre-m18-dominio-y-riesgo-residual`.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Informe final (artefacto: `projects/m18-appsec/informe-appsec.md
        final`).
      - >-
        P1–P3 verificables (artefacto: `projects/m18-appsec/informe-appsec.md
        final`).
      - 'Commit `docs(m18): L32 cierre-m18-dominio-y-riesgo-residual`.'
    siguiente: Materia M18 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L32 — Cierre M18 — dominio y riesgo residual

**~5.0 h · Semana 8**

Riesgo residual explícito > “somos seguros”. Cierra P1–P3 y handoff a M19/M25.

## Objetivo

`projects/m18-appsec/informe-appsec.md` final + README con residual top-3 y criterios de dominio.

## Pasos

### 1. Auditoría de evidencias (40–50 min)

```bash
ls -la projects/m18-appsec projects/m18-appsec/docs projects/m18-appsec/findings projects/m18-appsec/ci projects/m18-appsec/pocs
test -f projects/m18-appsec/threat-model-v1.md && echo P1=ok
wc -l projects/m18-appsec/findings-table.md
test -f projects/m18-appsec/ci/ci-appsec.yml && echo P3=ok
test -f projects/m18-appsec/docs/auth-inventario.md && echo auth=ok
```
### 2. Residual + handoff (50–60 min)

```bash
printf "\n## Riesgo residual (cierre)\n| Riesgo | Dueño | Fecha revisión |\n|--------|-------|----------------|\n| … | | |\n\n## Handoff\n- M19: secrets en PaaS, HTTPS, backups\n- M25: retest en trial\n" >> projects/m18-appsec/informe-appsec.md
```
### 3. README final (20–30 min)

Actualiza `projects/m18-appsec/README.md`: P1/P2/P3 ✅, enlace informe, residual.

```bash
git add projects/m18-appsec/README.md projects/m18-appsec/informe-appsec.md
git commit -m "docs(m18): l32 cierre dominio residual"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Repaso completo M18 | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Informe final (artefacto: `projects/m18-appsec/informe-appsec.md final`).
2. P1–P3 verificables (artefacto: `projects/m18-appsec/informe-appsec.md final`).
3. Commit `docs(m18): L32 cierre-m18-dominio-y-riesgo-residual`.

## Errores comunes

- Marcar dominio sin tests.
- Deploy público sin headers.

## Siguiente

Materia siguiente / refuerzo: [M19 — Nube/DevOps](../M19-nube-devops.md) y [hilo seguridad](../../../hilos/seguridad.md).
