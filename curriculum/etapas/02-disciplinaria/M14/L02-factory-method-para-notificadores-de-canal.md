---
id: L02
materia: M14
orden: 2
titulo: Factory Method para notificadores de canal
horas: 5
semana: 1
lectura: Factory Method; email vs WhatsApp link
evidencia: src/notify/ factory + tests + ADR
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El piloto avisará por email o link de WhatsApp. El service de pedidos no
      debe importar detalles de cada canal.


      **Objetivo de esta lección:** Factory Method (o factory function tipada)
      para notificadores + tests + ADR.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Interfaz común
    xp: 10
    cuerpo: >-
      ```ts

      export type Notifier = { send(to: string, body: string): Promise<void> };

      ```


      Stubs: `EmailNotifier`, `WhatsAppLinkNotifier` (concatena
      `https://wa.me/...`).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Factory
    xp: 10
    cuerpo: |-
      ```ts
      export function createNotifier(channel: "email" | "whatsapp"): Notifier {
        switch (channel) {
          case "email": return new EmailNotifier();
          case "whatsapp": return new WhatsAppLinkNotifier();
        }
      }
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Factory Method para notificadores de canal», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Factory Method para
          notificadores de ca…
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
      ¿Es recomendable en esta lección? “Clase `XFactory` que solo hace `return
      new X()`."
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
        texto: >-
          Factory Method (o factory function tipada) para notificadores + tests
          + ADR.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests
    xp: 10
    cuerpo: >-
      Assert de comportamiento observable (p. ej. mock de send, o retorno del
      link).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Factory crea al menos 2 notificadores (email / whatsapp-link) detrás de
        una interfaz.
      - >-
        ≥2 tests: el cliente pide canal y recibe el tipo correcto sin `new`
        concreto.
      - 'Commit `feat(m14): factory method notificadores`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L02 — Factory Method para notificadores de canal

**~5.0 h · Semana 1**

El piloto avisará por email o link de WhatsApp. El service de pedidos no debe importar detalles de cada canal.

## Objetivo

Factory Method (o factory function tipada) para notificadores + tests + ADR.

## Pasos (hazlos en orden)

### 1. Interfaz común (30–40 min)

```ts
export type Notifier = { send(to: string, body: string): Promise<void> };
```

Stubs: `EmailNotifier`, `WhatsAppLinkNotifier` (concatena `https://wa.me/...`).

### 2. Factory (50–60 min)

```ts
export function createNotifier(channel: "email" | "whatsapp"): Notifier {
  switch (channel) {
    case "email": return new EmailNotifier();
    case "whatsapp": return new WhatsAppLinkNotifier();
  }
}
```

### 3. Tests (40–50 min)

Assert de comportamiento observable (p. ej. mock de send, o retorno del link).

### 4. ADR (25 min) + commit

`adr/factory-notifiers.md` · `feat(m14): factory method notificadores`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Patrones de diseño* — GoF / Refactoring.Guru ES | Factory Method: crear notificadores sin acoplar al cliente | [Refactoring.Guru — Factory Method (ES)](https://refactoring.guru/es/design-patterns/factory-method) |
| Catálogo | Entrada de esta materia | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

Marca la lección **solo si**:

1. Factory crea al menos 2 notificadores (email / whatsapp-link) detrás de una interfaz.
2. ≥2 tests: el cliente pide canal y recibe el tipo correcto sin `new` concreto.
3. Commit `feat(m14): factory method notificadores`.

## Errores comunes

- Clase `XFactory` que solo hace `return new X()`.
- WhatsApp = enviar mensajes reales (hoy: deep-link o stub).
- Factory que conoce SMTP y HTML a la vez sin interfaz.

## Siguiente

[L03 — Singleton: cuándo NO usarlo](L03-singleton-cuando-no-usarlo.md)
