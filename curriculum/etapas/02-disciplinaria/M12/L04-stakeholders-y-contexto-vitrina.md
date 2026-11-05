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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras elicitación metiendo contexto en el SRS borrador.


      **Objetivo de esta lección:** Rellenar introducción + descripción general
      del `srs-borrador.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lee la plantilla
    xp: 10
    cuerpo: |-
      ```bash
      sed -n '1,80p' projects/m12-srs/plantilla.md
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Stakeholders
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Stakeholders y contexto Vitrina», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Stakeholders y contexto
          Vitrina
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Olvidar al cliente final (aunque no
      tenga login en MVP)."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
        texto: Rellenar introducción + descripción general del `srs-borrador.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Contexto
    xp: 10
    cuerpo: 'Secciones 1.1–1.3 y 2.1–2.3 del borrador. Diagrama:'
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
