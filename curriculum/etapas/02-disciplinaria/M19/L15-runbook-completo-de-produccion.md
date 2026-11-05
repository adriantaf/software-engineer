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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Unificar deploy, rollback, backup, restore, URLs, secretos
      (referencias), health.


      - runbook

      - handoff
  - id: s2
    tipo: ejemplo
    titulo: 1. Runbook completo
    xp: 10
    cuerpo: |-
      ```bash
      wc -l projects/m19-ops/runbook.md
      rg -n "Rollback|Backup|Health|Secrets" projects/m19-ops/runbook.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Runbook completo de producción" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m19-ops/runbook.md completo
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

      `git add projects/m19-ops/runbook.md`
    comandoEsperado:
      - git add projects/m19-ops/runbook.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m19-ops/runbook.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Unificar deploy, rollback, backup, restore, URLs, secretos
          (referencias), health.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m19-ops/runbook.md
      git commit -m "docs(m19): L15 runbook produccion completo"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `projects/m19-ops/runbook.md` completo (deploy, rollback, backup,
        restore, URLs).
      - 'Commit `docs(m19): L15 runbook-completo-de-produccion`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
