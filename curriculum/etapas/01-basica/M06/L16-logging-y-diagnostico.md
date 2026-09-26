---
id: L16
materia: M06
orden: 16
titulo: Logging, diagnóstico y contratos de error
horas: 5
semana: 4
lectura: "Docs Node console vs debug; CC cap. 7 repaso"
evidencia: "Logger delgado en frontera; semana 4 commit cierre"
---

# L16 — Logging, diagnóstico y contratos de error

**~5 h · Semana 4**

Cierras semana 4: observabilidad mínima sin spam. Logs en el borde; dominio limpio.

## Objetivo

Introducir interfaz `Logger` inyectable; registrar errores y eventos de negocio en adaptadores CLI/tests fake.

## Pasos

### 1. Diseño (45 min)

```ts
export interface Logger {
  info(msg: string, meta?: Record<string, unknown>): void;
  error(msg: string, meta?: Record<string, unknown>): void;
}
```

### 2. Implementaciones (60 min)

`ConsoleLogger`, `NoopLogger` para tests.

### 3. Cableado (90 min)

Solo capa aplicación/CLI loguea Result err con meta (id, código).

### 4. Tests (60 min)

Fake logger cuenta invocaciones en escenarios de fallo.

### 5. Documento operación (45 min)

`OPERACION.md`: qué se loguea, qué no (PII).

### 6. Commit (15 min)

`feat(m06): logging en frontera semana 4`

## Hecho cuando

1. Dominio sin `console.log` suelto.
2. Logger mockeable en tests.
3. OPERACION.md breve.

## Errores comunes

- Log en cada línea.
- Meta con objetos enormes.

## Siguiente

[L17 — Estructura de paquete npm](L17-estructura-paquete-npm.md)
