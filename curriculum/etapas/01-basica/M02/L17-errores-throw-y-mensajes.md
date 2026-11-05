---
id: L17
materia: M02
orden: 17
titulo: 'Errores, throw y mensajes'
horas: 2.5
semana: 5
lectura: EJ cap. 8 (bugs y errores)
evidencia: src/errores/ con AppError + loadEstado validando JSON
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Robustecer `loadEstado` ante JSON inválido y centralizar
      formato de errores en la CLI.


      “Error” sin contexto mata la confianza en tu CLI. La semana 5 es calidad
      de ingeniería, no solo features.
  - id: s2
    tipo: ejemplo
    titulo: 1. AppError
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Errores, throw y mensajes" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/errores/ con AppError + loadEstado validando JSON
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
    pregunta: ¿Es buena práctica en esta lección? “`throw "string"` en vez de `Error`."
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
          Robustecer `loadEstado` ante JSON inválido y centralizar formato de
          errores en la CLI.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Parse JSON seguro
    xp: 10
    cuerpo: >-
      En `archivo-json.ts` (katas o habits): captura `SyntaxError`, lanza
      `AppError` con código `JSON_INVALIDO` y ruta en el mensaje.
  - id: s7
    tipo: explicacion
    titulo: 3. EJ cap. 8
    xp: 10
    cuerpo: Lee bugs y errores; **1 ejercicio** relacionado con try/catch.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        Archivo corrupto → mensaje accionable, no stack trace crudo al usuario
        final.
      - '`AppError` usado al menos en dos sitios.'
      - Nota en README habits sobre códigos de error.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
