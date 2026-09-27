---
id: L02
materia: M14
orden: 2
titulo: Factory Method para notificadores de canal
horas: 5.0
semana: 1
lectura: Factory Method; email vs WhatsApp link
evidencia: src/notify/ factory + tests + ADR
---

# L02 — Factory Method para notificadores de canal

**~5.0 h · Semana 1**

El piloto avisará por email o link de WhatsApp. El service de citas no debe importar detalles de cada canal.

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
