---
id: L05
materia: M14
orden: 5
titulo: Adapter para API de calendario externo
horas: 5
semana: 2
lectura: Adapter; integrar API externa tras interfaz de dominio
evidencia: src/calendar/ adapter + fake API + tests
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Adapter + fake vendor + tests del puerto de dominio.


      Algún design partner vivirá en Google Calendar. Hoy aíslas ese JSON raro
      detrás de tu interfaz.
  - id: s2
    tipo: ejemplo
    titulo: 1. Puerto
    xp: 10
    cuerpo: |-
      ```ts
      export interface ExternalCalendar {
        listBusy(from: Date, to: Date): Promise<{ start: Date; end: Date }[]>;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Adapter para API de calendario externo" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: src/calendar/ adapter + fake API + tests
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
      ¿Es buena práctica en esta lección? “Filtrar tipos del vendor a toda la
      app."
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
        texto: Adapter + fake vendor + tests del puerto de dominio.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Vendor feo + Adapter
    xp: 10
    cuerpo: >-
      Simula respuesta `{ items: [{ start: { dateTime: string } }] }` y adapta a
      `Date`.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests + ADR
    xp: 10
    cuerpo: '`adr/adapter-calendar.md` · commit `feat(m14): adapter calendario externo`'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Puerto de dominio (p. ej. `ExternalCalendar`) + adapter sobre un cliente
        “feo” simulado.
      - 'Tests contra el puerto, no contra el JSON crudo del vendor.'
      - 'Commit `feat(m14): adapter calendario externo`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Adapter para API de calendario externo

**~5.0 h · Semana 2**

Algún design partner vivirá en Google Calendar. Hoy aíslas ese JSON raro detrás de tu interfaz.

## Objetivo

Adapter + fake vendor + tests del puerto de dominio.

## Pasos (hazlos en orden)

### 1. Puerto (30 min)

```ts
export interface ExternalCalendar {
  listBusy(from: Date, to: Date): Promise<{ start: Date; end: Date }[]>;
}
```

### 2. Vendor feo + Adapter (70–90 min)

Simula respuesta `{ items: [{ start: { dateTime: string } }] }` y adapta a `Date`.

### 3. Tests + ADR (50 min)

`adr/adapter-calendar.md` · commit `feat(m14): adapter calendario externo`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Adapter: convierte API de terceros a tu puerto de dominio | [Refactoring.Guru — Adapter (ES)](https://refactoring.guru/es/design-patterns/adapter) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Puerto de dominio (p. ej. `ExternalCalendar`) + adapter sobre un cliente “feo” simulado.
2. Tests contra el puerto, no contra el JSON crudo del vendor.
3. Commit `feat(m14): adapter calendario externo`.

## Errores comunes

- Filtrar tipos del vendor a toda la app.
- Adapter sin tests.
- Llamar HTTP real obligatorio (usa fake en memoria).

## Siguiente

[L06 — Decorator para logging de operaciones de pedido](L06-decorator-para-logging-de-operaciones-de-pedido.md)
