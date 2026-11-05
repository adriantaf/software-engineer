---
id: L13
materia: M06
orden: 13
titulo: Errores como diseño (CC cap. 7)
horas: 5
semana: 4
lectura: Código limpio cap. 7 (manejo de errores)
evidencia: Jerarquía o catálogo de errores de dominio; sin catch vacíos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los errores son flujo de control y UX para quien llama tu API. Tragar
      excepciones es deuda.


      **Objetivo de esta lección:** Aplicar CC cap. 7: excepciones con contexto,
      límites claros, sin `catch {}`; definir errores de dominio expresivos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```ts
      export class LibroNoEncontradoError extends Error {
        constructor(public readonly id: string) {
          super(`Libro no encontrado: ${id}`);
          this.name = "LibroNoEncontradoError";
        }
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Auditoría
    xp: 10
    cuerpo: |-
      ```ts
      export class LibroNoEncontradoError extends Error {
        constructor(public readonly id: string) {
          super(`Libro no encontrado: ${id}`);
          this.name = "LibroNoEncontradoError";
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
      Al terminar «Errores como diseño (CC cap. 7)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Cero `catch` vacíos.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Errores como diseño (CC
          cap. 7)
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
    pregunta: ¿Es recomendable en esta lección? “String errors everywhere."
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
          Aplicar CC cap. 7: excepciones con contexto, límites claros, sin
          `catch {}`; definir errores de dominio expresivos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Catálogo de errores
    xp: 10
    cuerpo: O union de errores si prefieres sin excepciones (prepara L14).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Cero `catch` vacíos.
      - Errores nombrados con contexto.
      - Tests demuestran fallos esperados.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L13 — Errores como diseño (CC cap. 7)

**~5 h · Semana 4**

Los errores son flujo de control y UX para quien llama tu API. Tragar excepciones es deuda.

## Objetivo

Aplicar CC cap. 7: excepciones con contexto, límites claros, sin `catch {}`; definir errores de dominio expresivos.

## Pasos

### 1. Lectura (60 min)

CC cap. 7. Anota reglas sobre checked vs unchecked (adaptado a TS).

### 2. Auditoría (45 min)

Busca `catch`, `throw new Error("error")` genéricos.

### 3. Catálogo de errores (90 min)

```ts
export class LibroNoEncontradoError extends Error {
  constructor(public readonly id: string) {
    super(`Libro no encontrado: ${id}`);
    this.name = "LibroNoEncontradoError";
  }
}
```

O union de errores si prefieres sin excepciones (prepara L14).

### 4. Refactor llamadas (90 min)

Mensajes con datos; logs en frontera, no en cada línea.

### 5. Tests de error (45 min)

`expect(() => ...).toThrow(LibroNoEncontradoError)` o equivalente Result.

## Hecho cuando

1. Cero `catch` vacíos.
2. Errores nombrados con contexto.
3. Tests demuestran fallos esperados.

## Errores comunes

- String errors everywhere.
- Loguear y re-lanzar sin añadir info.

## Siguiente

[L14 — Patrón Result tipado](L14-patron-result-tipado.md)
