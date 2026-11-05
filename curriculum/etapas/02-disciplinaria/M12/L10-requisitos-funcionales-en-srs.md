---
id: L10
materia: M12
orden: 10
titulo: Requisitos funcionales en SRS
horas: 5
semana: 3
lectura: plantilla.md — requisitos funcionales
evidencia: srs-borrador.md funcionales
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Completar §3.1 Requisitos funcionales del borrador.

      El SRS habla RF-xx; las stories alimentan pero no sustituyen.
  - id: s2
    tipo: ejemplo
    titulo: 1. Deriva RF
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md
      git commit -m "docs(m12): l10 requisitos funcionales"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Requisitos funcionales en SRS" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: srs-borrador.md funcionales
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

      `git add projects/m12-srs/srs-borrador.md`
    comandoEsperado:
      - git add projects/m12-srs/srs-borrador.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m12-srs/srs-borrador.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Completar §3.1 Requisitos funcionales del borrador.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Fuera de alcance
    xp: 10
    cuerpo: §4 con bullets concretos (no “todo lo demás”).
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md
      git commit -m "docs(m12): l10 requisitos funcionales"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Tabla §3.1 con ≥8 RF derivados de Must/Should.
      - Cada RF tiene criterio de aceptación o enlace a US.
      - 'Commit `docs(m12): l10 requisitos funcionales`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L10 — Requisitos funcionales en SRS

**~5.0 h · Semana 3**

El SRS habla RF-xx; las stories alimentan pero no sustituyen.

## Objetivo

Completar §3.1 Requisitos funcionales del borrador.

## Pasos

### 1. Deriva RF (90–110 min)

| ID | Descripción | Prioridad | Criterio / US |
|----|-------------|-----------|---------------|
| RF-01 | Owner autenticado gestiona clientes | Alta | US-0x |

Cubre clientes, pedidos, agenda, auth, roles básicos.

### 2. Fuera de alcance (30 min)

§4 con bullets concretos (no “todo lo demás”).

### 3. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md
git commit -m "docs(m12): l10 requisitos funcionales"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | RF-xx con prioridad y criterio; trazabilidad a US | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla §3.1 con ≥8 RF derivados de Must/Should.
2. Cada RF tiene criterio de aceptación o enlace a US.
3. Commit `docs(m12): l10 requisitos funcionales`.

## Errores comunes

- Copiar stories verbatim sin IDs RF.
- RF sin prioridad.
- Mezclar RNF en la tabla funcional.

## Siguiente

[L11 — SRS v1, freeze y P3](L11-srs-v1-freeze-y-p3.md)
