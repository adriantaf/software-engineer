---
id: L05
materia: M02
orden: 5
titulo: Arrays y métodos esenciales
horas: 2.5
semana: 2
lectura: EJ cap. 4 (objetos y arrays) — primera mitad
evidencia: src/arrays/ con push/map inmutable + 3 katas sobre arrays
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Tu CLI guardará listas de hábitos y tareas. Casi todo pasa por copiar →
      transformar → persistir.


      **Objetivo de esta lección:** Modelar listas de datos sin mutar por
      accidente y resolver 3 katas centradas en arrays.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Arrays readonly en espíritu
    xp: 10
    cuerpo: |-
      ```ts
      export type Tarea = { id: string; titulo: string; hecha: boolean };

      export function marcarHecha(tareas: Tarea[], id: string): Tarea[] {
        return tareas.map((t) => (t.id === id ? { ...t, hecha: true } : t));
      }

      export function pendientes(tareas: Tarea[]): Tarea[] {
        return tareas.filter((t) => !t.hecha);
      }
      ```

      `src/arrays/lista.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Métodos de consulta
    xp: 10
    cuerpo: |-
      ```ts
      export type Tarea = { id: string; titulo: string; hecha: boolean };

      export function marcarHecha(tareas: Tarea[], id: string): Tarea[] {
        return tareas.map((t) => (t.id === id ? { ...t, hecha: true } : t));
      }

      export function pendientes(tareas: Tarea[]): Tarea[] {
        return tareas.filter((t) => !t.hecha);
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Arrays y métodos esenciales», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `marcarHecha` no muta el array original (prueba con `const antes =
          [...]` y compara).
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Arrays y métodos
          esenciales
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
    pregunta: ¿Es recomendable en esta lección? “Mutar con `.sort()` sin copiar antes."
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
          Modelar listas de datos sin mutar por accidente y resolver 3 katas
          centradas en arrays.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tres katas arrays
    xp: 10
    cuerpo: >-
      Ej.: rotar array, eliminar duplicados, intersección de dos listas
      pequeñas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `marcarHecha` no muta el array original (prueba con `const antes =
        [...]` y compara).
      - Tres katas nuevas en `src/katas/`.
      - ≥10 katas totales en el repo o documentas cuántas faltan para P1.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Arrays y métodos esenciales

**~2.5 h · Semana 2**

Arrays tipados, inmutabilidad práctica y métodos que usarás cada día: `map`, `filter`, `slice`, `includes`.

## Objetivo

Modelar listas de datos sin mutar por accidente y resolver 3 katas centradas en arrays.

## Por qué importa

Tu CLI guardará listas de hábitos y tareas. Casi todo pasa por copiar → transformar → persistir.

## Pasos

### 1. Arrays readonly en espíritu (40 min)

`src/arrays/lista.ts`:

```ts
export type Tarea = { id: string; titulo: string; hecha: boolean };

export function marcarHecha(tareas: Tarea[], id: string): Tarea[] {
  return tareas.map((t) => (t.id === id ? { ...t, hecha: true } : t));
}

export function pendientes(tareas: Tarea[]): Tarea[] {
  return tareas.filter((t) => !t.hecha);
}
```

### 2. Métodos de consulta (30 min)

`src/arrays/estadisticas.ts`: `suma`, `promedio`, `maximo` sobre `number[]` con validación de array vacío (`null` o throw — elige y documenta).

### 3. Tres katas arrays (55 min)

Ej.: rotar array, eliminar duplicados, intersección de dos listas pequeñas.

### 4. Lectura (25 min)

EJ cap. 4 hasta objetos/arrays básicos.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 4 (inicio) |
| TS Handbook | [Everyday Types — Arrays](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `marcarHecha` no muta el array original (prueba con `const antes = [...]` y compara).
2. Tres katas nuevas en `src/katas/`.
3. ≥10 katas totales en el repo o documentas cuántas faltan para P1.

## Errores comunes

- Mutar con `.sort()` sin copiar antes.
- `array[i]` sin comprobar límites en funciones públicas.
- Tipar arrays como `any[]`.

## Siguiente

[L06 — Objetos, interfaces y tipos](L06-objetos-interfaces-y-tipos.md)
