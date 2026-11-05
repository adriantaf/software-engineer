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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El SRS habla RF-xx; las stories alimentan pero no sustituyen.


      **Objetivo de esta lección:** Completar §3.1 Requisitos funcionales del
      borrador.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Deriva RF
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md
      git commit -m "docs(m12): l10 requisitos funcionales"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Fuera de alcance
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs/srs-borrador.md
      git commit -m "docs(m12): l10 requisitos funcionales"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Requisitos funcionales en SRS», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Requisitos funcionales
          en SRS
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

      `git add projects/m12-srs/srs-borrador.md`
    comandoEsperado:
      - git add projects/m12-srs/srs-borrador.md
      - 'git commit -m "docs(m12): l10 requisitos funcionales"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m12-srs/srs-borrador.md'
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
        texto: Completar §3.1 Requisitos funcionales del borrador.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
