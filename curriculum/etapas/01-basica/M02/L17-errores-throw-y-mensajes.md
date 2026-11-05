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
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      “Error” sin contexto mata la confianza en tu CLI. La semana 5 es calidad
      de ingeniería, no solo features.


      **Objetivo de esta lección:** Robustecer `loadEstado` ante JSON inválido y
      centralizar formato de errores en la CLI.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: AppError
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

      `src/errores/app-error.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Parse JSON seguro
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Errores, throw y mensajes», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          Archivo corrupto → mensaje accionable, no stack trace crudo al usuario
          final.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Errores, throw y
          mensajes
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
    pregunta: ¿Es recomendable en esta lección? “`throw "string"` en vez de `Error`."
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
          Robustecer `loadEstado` ante JSON inválido y centralizar formato de
          errores en la CLI.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: EJ cap. 8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
