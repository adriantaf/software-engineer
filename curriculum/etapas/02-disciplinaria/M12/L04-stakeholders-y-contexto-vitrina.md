---
id: L04
materia: M12
orden: 4
titulo: Stakeholders y contexto Vitrina
horas: 5
semana: 1
lectura: SRS plantilla — stakeholders y descripción general
evidencia: srs-borrador.md sección contexto
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Rellenar introducción + descripción general del
      `srs-borrador.md`.


      Cierras elicitación metiendo contexto en el SRS borrador.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lee la plantilla
    xp: 10
    cuerpo: |-
      ```bash
      sed -n '1,80p' projects/m12-srs/plantilla.md
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Stakeholders y contexto Vitrina" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: srs-borrador.md sección contexto
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Olvidar al cliente final (aunque no
      tenga login en MVP)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Rellenar introducción + descripción general del `srs-borrador.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Stakeholders
    xp: 10
    cuerpo: >-
      Para Owner, Staff, Cliente final (indirecto): metas, dolores, acceso a
      datos. Incluye supuesto single-tenant del piloto.
  - id: s7
    tipo: ejemplo
    titulo: 3. Contexto
    xp: 10
    cuerpo: |-
      ```mermaid
      flowchart LR
        Owner --> Panel
        Staff --> Panel
        Panel --> API
        API --> DB
        Guest --> PerfilMenu
        PerfilMenu --> WA[Pedido_WhatsApp]
        WA -. mensaje .-> Owner
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `srs-borrador.md` secciones 1–2 rellenadas (propósito, alcance borrador,
        stakeholders).
      - 'Diagrama de contexto (Mermaid o ASCII): actores ↔ Vitrina.'
      - 'Commit `docs(m12): l04 contexto stakeholders`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Stakeholders y contexto Vitrina

**~5.0 h · Semana 1**

Cierras elicitación metiendo contexto en el SRS borrador.

## Objetivo

Rellenar introducción + descripción general del `srs-borrador.md`.

## Pasos

### 1. Lee la plantilla (30 min)

```bash
sed -n '1,80p' projects/m12-srs/plantilla.md
```

### 2. Stakeholders (60 min)

Para Owner, Staff, Cliente final (indirecto): metas, dolores, acceso a datos. Incluye supuesto single-tenant del piloto.

### 3. Contexto (60 min)

Secciones 1.1–1.3 y 2.1–2.3 del borrador. Diagrama:

```mermaid
flowchart LR
  Owner --> Panel
  Staff --> Panel
  Panel --> API
  API --> DB
  Guest --> PerfilMenu
  PerfilMenu --> WA[Pedido_WhatsApp]
  WA -. mensaje .-> Owner
```

### 4. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md
git commit -m "docs(m12): l04 contexto stakeholders"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Stakeholders owner/staff/cliente; perspectiva del producto piloto | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `srs-borrador.md` secciones 1–2 rellenadas (propósito, alcance borrador, stakeholders).
2. Diagrama de contexto (Mermaid o ASCII): actores ↔ Vitrina.
3. Commit `docs(m12): l04 contexto stakeholders`.

## Errores comunes

- Olvidar al cliente final (aunque no tenga login en MVP).
- Alcance infinito en la intro.
- Stakeholders sin metas.

## Siguiente

[L05 — Formato user story y trazabilidad](L05-formato-user-story-y-trazabilidad.md)
