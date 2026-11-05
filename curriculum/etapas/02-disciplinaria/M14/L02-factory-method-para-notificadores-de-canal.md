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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Factory Method (o factory function tipada) para
      notificadores + tests + ADR.


      El piloto avisará por email o link de WhatsApp. El service de pedidos no
      debe importar detalles de cada canal.
  - id: s2
    tipo: ejemplo
    titulo: 1. Interfaz común
    xp: 10
    cuerpo: |-
      ```ts
      export type Notifier = { send(to: string, body: string): Promise<void> };
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Factory Method para notificadores de canal" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: src/notify/ factory + tests + ADR
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
      ¿Es buena práctica en esta lección? “Clase `XFactory` que solo hace
      `return new X()`."
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
        texto: >-
          Factory Method (o factory function tipada) para notificadores + tests
          + ADR.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Factory
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
  - id: s7
    tipo: explicacion
    titulo: 3. Tests
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
