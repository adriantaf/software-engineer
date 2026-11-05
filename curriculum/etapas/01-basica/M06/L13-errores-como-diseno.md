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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Aplicar CC cap. 7: excepciones con contexto, límites claros,
      sin `catch {}`; definir errores de dominio expresivos.


      Los errores son flujo de control y UX para quien llama tu API. Tragar
      excepciones es deuda.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Errores como diseño (CC cap. 7)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Jerarquía o catálogo de errores de dominio; sin catch vacíos
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
    pregunta: ¿Es buena práctica en esta lección? “String errors everywhere."
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
          Aplicar CC cap. 7: excepciones con contexto, límites claros, sin
          `catch {}`; definir errores de dominio expresivos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Auditoría
    xp: 10
    cuerpo: 'Busca `catch`, `throw new Error("error")` genéricos.'
  - id: s7
    tipo: ejemplo
    titulo: 3. Catálogo de errores
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
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Cero `catch` vacíos.
      - Errores nombrados con contexto.
      - Tests demuestran fallos esperados.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
