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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Algún design partner vivirá en Google Calendar. Hoy aíslas ese JSON raro
      detrás de tu interfaz.


      **Objetivo de esta lección:** Adapter + fake vendor + tests del puerto de
      dominio.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Puerto
    xp: 10
    cuerpo: |-
      ```ts
      export interface ExternalCalendar {
        listBusy(from: Date, to: Date): Promise<{ start: Date; end: Date }[]>;
      }
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Vendor feo + Adapter
    xp: 10
    cuerpo: |-
      ```ts
      export interface ExternalCalendar {
        listBusy(from: Date, to: Date): Promise<{ start: Date; end: Date }[]>;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Adapter para API de calendario externo», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Adapter para API de
          calendario externo
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
      ¿Es recomendable en esta lección? “Filtrar tipos del vendor a toda la
      app."
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
        texto: Adapter + fake vendor + tests del puerto de dominio.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests + ADR
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
