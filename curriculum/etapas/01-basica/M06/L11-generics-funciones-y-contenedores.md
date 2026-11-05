---
id: L11
materia: M06
orden: 11
titulo: 'Generics: funciones y contenedores'
horas: 5
semana: 3
lectura: TS Handbook — Generics
evidencia: src/generics/ con funciones reutilizables testeadas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los generics expresan estructuras sin perder tipo: repositorios,
      utilidades, colecciones.


      **Objetivo de esta lección:** Escribir funciones genéricas (`mapResult`,
      `findById`) y un contenedor tipado simple con tests.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```ts

      export function findById<T extends { id: string }>(items: T[], id:
      string): T | undefined {
        return items.find((x) => x.id === id);
      }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Utilidades
    xp: 10
    cuerpo: >-
      ```ts

      export function findById<T extends { id: string }>(items: T[], id:
      string): T | undefined {
        return items.find((x) => x.id === id);
      }

      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Generics: funciones y contenedores», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: ≥2 funciones genéricas con constraints.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Generics: funciones y
          contenedores
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
    pregunta: >-
      ¿Es recomendable en esta lección? “Generic `T` sin constraint cuando
      accedes a `.id`."
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
          Escribir funciones genéricas (`mapResult`, `findById`) y un contenedor
          tipado simple con tests.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Repositorio genérico
    xp: 10
    cuerpo: >-
      `RepositorioEnMemoria<T extends Identificable>` si no rompe claridad del
      dominio.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - ≥2 funciones genéricas con constraints.
      - Tests instancian tipos distintos.
      - Sin `any`.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Generics: funciones y contenedores

**~5 h · Semana 3**

Los generics expresan estructuras sin perder tipo: repositorios, utilidades, colecciones.

## Objetivo

Escribir funciones genéricas (`mapResult`, `findById`) y un contenedor tipado simple con tests.

## Pasos

### 1. Lectura (60 min)

Handbook Generics: constraints, `extends`.

### 2. Utilidades (120 min)

```ts
export function findById<T extends { id: string }>(items: T[], id: string): T | undefined {
  return items.find((x) => x.id === id);
}
```

### 3. Repositorio genérico (opcional, 90 min)

`RepositorioEnMemoria<T extends Identificable>` si no rompe claridad del dominio.

### 4. Tests (60 min)

Varias instancias de `T` (libro, usuario mock).

## Hecho cuando

1. ≥2 funciones genéricas con constraints.
2. Tests instancian tipos distintos.
3. Sin `any`.

## Errores comunes

- Generic `T` sin constraint cuando accedes a `.id`.
- Sobre-generalizar el dominio entero.

## Siguiente

[L12 — Generics en APIs del dominio](L12-generics-en-apis-del-dominio.md)
