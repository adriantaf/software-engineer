---
id: L05
materia: M14
orden: 5
titulo: Adapter para API de calendario externo
horas: 5.0
semana: 2
lectura: Adapter; integrar API externa tras interfaz de dominio
evidencia: src/calendar/ adapter + fake API + tests
---

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

[L06 — Decorator para logging de operaciones de cita](L06-decorator-para-logging-de-operaciones-de-cita.md)
