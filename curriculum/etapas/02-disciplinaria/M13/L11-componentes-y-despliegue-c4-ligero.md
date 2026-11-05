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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `diagramas/c4-contenedores.md` con contexto + contenedores
      del piloto.


      Zoom out: no clases, sino cajas desplegables. Suficiente para M19 sin
      teatro enterprise.
  - id: s2
    tipo: ejemplo
    titulo: 1. Contexto
    xp: 10
    cuerpo: |-
      ```mermaid
      flowchart LR
        Person[Staff/Owner] --> Web[Web app]
        Web --> API[API monolito]
        API --> DB[(PostgreSQL)]
        API --> Mail[Email provider]
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Componentes y despliegue (C4 ligero)" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: diagramas/c4-contenedores.md (contexto + contenedores)
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
    pregunta: ¿Es buena práctica en esta lección? “C4 con 25 microservicios inventados."
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
        texto: '`diagramas/c4-contenedores.md` con contexto + contenedores del piloto.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Contenedores
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
  - id: s7
    tipo: explicacion
    titulo: 3. Qué NO dibujas
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
