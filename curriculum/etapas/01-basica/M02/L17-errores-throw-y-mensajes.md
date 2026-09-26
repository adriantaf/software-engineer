---
id: L17
materia: M02
orden: 17
titulo: Errores, throw y mensajes
horas: 2.5
semana: 5
lectura: "EJ cap. 8 (bugs y errores)"
evidencia: "src/errores/ con AppError + loadEstado validando JSON"
---

# L17 — Errores, throw y mensajes

**~2.5 h · Semana 5**

Errores como información: clases custom, `cause`, y mensajes que un humano puede actuar.

## Objetivo

Robustecer `loadEstado` ante JSON inválido y centralizar formato de errores en la CLI.

## Por qué importa

“Error” sin contexto mata la confianza en tu CLI. La semana 5 es calidad de ingeniería, no solo features.

## Pasos

### 1. AppError (40 min)

`src/errores/app-error.ts`:

```ts
export class AppError extends Error {
  constructor(
    message: string,
    readonly code: string,
    options?: { cause?: unknown }
  ) {
    super(message, options);
    this.name = "AppError";
  }
}
```

### 2. Parse JSON seguro (50 min)

En `archivo-json.ts` (katas o habits): captura `SyntaxError`, lanza `AppError` con código `JSON_INVALIDO` y ruta en el mensaje.

### 3. EJ cap. 8 (50 min)

Lee bugs y errores; **1 ejercicio** relacionado con try/catch.

### 4. CLI (20 min)

Imprime `AppError` como `codigo: mensaje` en stderr.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 8 |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. Archivo corrupto → mensaje accionable, no stack trace crudo al usuario final.
2. `AppError` usado al menos en dos sitios.
3. Nota en README habits sobre códigos de error.

## Errores comunes

- `throw "string"` en vez de `Error`.
- Loggear stack en producción CLI sin flag `--verbose`.
- Mezclar `Result` y excepciones sin criterio (elige borde: parse → Result, I/O → throw está bien).

## Siguiente

[L18 — Validación y código legible](L18-validacion-y-codigo-legible.md)
