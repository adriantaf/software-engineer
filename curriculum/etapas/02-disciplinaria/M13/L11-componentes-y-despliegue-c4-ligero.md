---
id: L11
materia: M13
orden: 11
titulo: Componentes y despliegue (C4 ligero)
horas: 5
semana: 3
lectura: C4 niveles 1–2; contenedores del piloto
evidencia: diagramas/c4-contenedores.md (contexto + contenedores)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Zoom out: no clases, sino cajas desplegables. Suficiente para M19 sin
      teatro enterprise.


      **Objetivo de esta lección:** `diagramas/c4-contenedores.md` con contexto
      + contenedores del piloto.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Contexto
    xp: 10
    cuerpo: |-
      ```mermaid
      flowchart LR
        Person[Staff/Owner] --> Web[Web app]
        Web --> API[API monolito]
        API --> DB[(PostgreSQL)]
        API --> Mail[Email provider]
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Contenedores
    xp: 10
    cuerpo: >-
      ```mermaid

      flowchart LR
        Person[Staff/Owner] --> Web[Web app]
        Web --> API[API monolito]
        API --> DB[(PostgreSQL)]
        API --> Mail[Email provider]
      ```


      Notas de deploy tentativas: un VPS o PaaS, un proceso Node, un Postgres
      (Docker ok en local).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Componentes y despliegue (C4 ligero)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Componentes y
          despliegue (C4 ligero)
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
    pregunta: ¿Es recomendable en esta lección? “C4 con 25 microservicios inventados."
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
        texto: '`diagramas/c4-contenedores.md` con contexto + contenedores del piloto.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Qué NO dibujas
    xp: 10
    cuerpo: >-
      Sin service mesh, sin cola Kafka “por si acaso”. Si el SRS no lo pide,
      fuera.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Diagrama de contexto (persona + Vitrina + sistemas externos).
      - 'Diagrama de contenedores: Web, API, PostgreSQL (± email).'
      - 'Commit `docs(m13): C4 ligero contexto y contenedores`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Componentes y despliegue (C4 ligero)

**~5.0 h · Semana 3**

Zoom out: no clases, sino cajas desplegables. Suficiente para M19 sin teatro enterprise.

## Objetivo

`diagramas/c4-contenedores.md` con contexto + contenedores del piloto.

## Pasos (hazlos en orden)

### 1. Contexto (40–50 min)

Personas: Owner/Staff. Sistema: Vitrina. Externos: Email o WhatsApp link, (luego) Stripe.

### 2. Contenedores (60–70 min)

```mermaid
flowchart LR
  Person[Staff/Owner] --> Web[Web app]
  Web --> API[API monolito]
  API --> DB[(PostgreSQL)]
  API --> Mail[Email provider]
```

Notas de deploy tentativas: un VPS o PaaS, un proceso Node, un Postgres (Docker ok en local).

### 3. Qué NO dibujas (20 min)

Sin service mesh, sin cola Kafka “por si acaso”. Si el SRS no lo pide, fuera.

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/c4-contenedores.md
git commit -m "docs(m13): C4 ligero contexto y contenedores"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | C4 context/container para un monolito web + DB | [C4 model](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Diagrama de contexto (persona + Vitrina + sistemas externos).
2. Diagrama de contenedores: Web, API, PostgreSQL (± email).
3. Commit `docs(m13): C4 ligero contexto y contenedores`.

## Errores comunes

- C4 con 25 microservicios inventados.
- Olvidar al design partner / usuario del negocio como persona.
- Mezclar nivel clases con nivel contenedores en un solo dibujo ilegible.

## Siguiente

[L12 — Boundaries actualizados y amenazas](L12-boundaries-actualizados-y-amenazas.md)
