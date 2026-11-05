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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar type guards (`is`) y narrowing con `in`,
      `typeof`, discriminantes; cubrir ramas con tests.


      TypeScript estrecha tipos tras comprobaciones; tú diseñas guards
      reutilizables.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```ts

      export function esPrestado(e: EstadoLibro): e is Extract<EstadoLibro, {
      tipo: "prestado" }> {
        return e.tipo === "prestado";
      }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Narrowing y type guards" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: Type guards user-defined + tests de ramas
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
    pregunta: ¿Es buena práctica en esta lección? “Cast para callar al compilador."
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
          Implementar type guards (`is`) y narrowing con `in`, `typeof`,
          discriminantes; cubrir ramas con tests.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Guards
    xp: 10
    cuerpo: >-
      ```ts

      export function esPrestado(e: EstadoLibro): e is Extract<EstadoLibro, {
      tipo: "prestado" }> {
        return e.tipo === "prestado";
      }

      ```
  - id: s7
    tipo: explicacion
    titulo: 3. API pública
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
