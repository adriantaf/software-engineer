---
id: L10
materia: M06
orden: 10
titulo: Narrowing y type guards
horas: 5
semana: 3
lectura: TS Handbook — Narrowing
evidencia: Type guards user-defined + tests de ramas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      TypeScript estrecha tipos tras comprobaciones; tú diseñas guards
      reutilizables.


      **Objetivo de esta lección:** Implementar type guards (`is`) y narrowing
      con `in`, `typeof`, discriminantes; cubrir ramas con tests.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```ts

      export function esPrestado(e: EstadoLibro): e is Extract<EstadoLibro, {
      tipo: "prestado" }> {
        return e.tipo === "prestado";
      }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Guards
    xp: 10
    cuerpo: >-
      ```ts

      export function esPrestado(e: EstadoLibro): e is Extract<EstadoLibro, {
      tipo: "prestado" }> {
        return e.tipo === "prestado";
      }

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Narrowing y type guards», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: ≥2 type guards reutilizables.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Narrowing y type guards
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
    pregunta: ¿Es recomendable en esta lección? “Cast para callar al compilador."
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
          Implementar type guards (`is`) y narrowing con `in`, `typeof`,
          discriminantes; cubrir ramas con tests.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: API pública
    xp: 10
    cuerpo: >-
      Funciones que aceptan union y devuelven Result o throw según política
      (unifica criterio).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - ≥2 type guards reutilizables.
      - Sin `as` salvo casos documentados.
      - Tests por discriminante.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Narrowing y type guards

**~5 h · Semana 3**

TypeScript estrecha tipos tras comprobaciones; tú diseñas guards reutilizables.

## Objetivo

Implementar type guards (`is`) y narrowing con `in`, `typeof`, discriminantes; cubrir ramas con tests.

## Pasos

### 1. Lectura (60 min)

Handbook Narrowing completo (secciones principales).

### 2. Guards (90 min)

```ts
export function esPrestado(e: EstadoLibro): e is Extract<EstadoLibro, { tipo: "prestado" }> {
  return e.tipo === "prestado";
}
```

### 3. API pública (90 min)

Funciones que aceptan union y devuelven Result o throw según política (unifica criterio).

### 4. Tests por rama (60 min)

Cada variante del union tiene ≥1 test.

### 5. Elimina casts (30 min)

Busca `as` innecesarios; reemplaza por guards.

## Hecho cuando

1. ≥2 type guards reutilizables.
2. Sin `as` salvo casos documentados.
3. Tests por discriminante.

## Errores comunes

- Cast para callar al compilador.
- Guard incorrecto (mentira al tipo system).

## Siguiente

[L11 — Generics: funciones y contenedores](L11-generics-funciones-y-contenedores.md)
