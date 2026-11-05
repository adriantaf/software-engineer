---
id: L15
materia: M19
orden: 15
titulo: Runbook completo de producción
horas: 5
semana: 4
lectura: SRE runbook lite
evidencia: projects/m19-ops/runbook.md completo
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - runbook

      - handoff


      **Objetivo de esta lección:** Unificar deploy, rollback, backup, restore,
      URLs, secretos (referencias), health.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Runbook completo
    xp: 10
    cuerpo: >-
      ```bash

      wc -l projects/m19-ops/runbook.md

      rg -n "Rollback|Backup|Health|Secrets" projects/m19-ops/runbook.md

      ```


      Completa `projects/m19-ops/runbook.md`: deploy, rollback, logs, backup,
      restore, contactos, URLs (sin secretos).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m19-ops/runbook.md
      git commit -m "docs(m19): L15 runbook produccion completo"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Runbook completo de producción», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Runbook completo de
          producción
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

      `git add projects/m19-ops/runbook.md`
    comandoEsperado:
      - git add projects/m19-ops/runbook.md
      - 'git commit -m "docs(m19): L15 runbook produccion completo"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m19-ops/runbook.md'
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
          Unificar deploy, rollback, backup, restore, URLs, secretos
          (referencias), health.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: terminal
    titulo: Segundo comando
    xp: 15
    enunciado: |-
      Ahora el siguiente comando de la secuencia:

      `git commit -m "docs(m19): L15 runbook produccion completo"`
    comandoEsperado:
      - 'git commit -m "docs(m19): L15 runbook produccion completo"'
    explicacionError: 'Esperado: git commit -m "docs(m19): L15 runbook produccion completo"'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/runbook.md` completo (deploy, rollback, backup,
        restore, URLs).
      - 'Commit `docs(m19): L15 runbook-completo-de-produccion`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Runbook completo de producción

**~5.0 h · Semana 4**

Proyecto único M19.

## Objetivo

Unificar deploy, rollback, backup, restore, URLs, secretos (referencias), health.

## Conceptos clave

- runbook
- handoff

## Pasos (hazlos en orden)

### 1. Runbook completo (70–90 min)

Completa `projects/m19-ops/runbook.md`: deploy, rollback, logs, backup, restore, contactos, URLs (sin secretos).

```bash
wc -l projects/m19-ops/runbook.md
rg -n "Rollback|Backup|Health|Secrets" projects/m19-ops/runbook.md
```

### 2. Commit (15 min)

```bash
git add projects/m19-ops/runbook.md
git commit -m "docs(m19): L15 runbook produccion completo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | SRE runbook lite | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m19-ops/runbook.md` completo (deploy, rollback, backup, restore, URLs).
2. Commit `docs(m19): L15 runbook-completo-de-produccion`.

## Errores comunes

- Runbook genérico de internet.
- Faltan URLs o dueños.

## Siguiente

[L16 — Cierre M19 — checklist pre-demo M22](L16-cierre-m19-checklist-pre-demo-m22.md)
