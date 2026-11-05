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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Escribir funciones genéricas (`mapResult`, `findById`) y un
      contenedor tipado simple con tests.


      Los generics expresan estructuras sin perder tipo: repositorios,
      utilidades, colecciones.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```ts

      export function findById<T extends { id: string }>(items: T[], id:
      string): T | undefined {
        return items.find((x) => x.id === id);
      }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Generics: funciones y contenedores" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: src/generics/ con funciones reutilizables testeadas
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
    pregunta: >-
      ¿Es buena práctica en esta lección? “Generic `T` sin constraint cuando
      accedes a `.id`."
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
          Escribir funciones genéricas (`mapResult`, `findById`) y un contenedor
          tipado simple con tests.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Utilidades
    xp: 10
    cuerpo: >-
      ```ts

      export function findById<T extends { id: string }>(items: T[], id:
      string): T | undefined {
        return items.find((x) => x.id === id);
      }

      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Repositorio genérico
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
