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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Modelar listas de datos sin mutar por accidente y resolver 3
      katas centradas en arrays.


      Tu CLI guardará listas de hábitos y tareas. Casi todo pasa por copiar →
      transformar → persistir.
  - id: s2
    tipo: ejemplo
    titulo: 1. Arrays readonly en espíritu
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Arrays y métodos esenciales" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/arrays/ con push/map inmutable + 3 katas sobre arrays
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
      ¿Es buena práctica en esta lección? “Mutar con `.sort()` sin copiar
      antes."
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
          Modelar listas de datos sin mutar por accidente y resolver 3 katas
          centradas en arrays.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Métodos de consulta
    xp: 10
    cuerpo: >-
      `src/arrays/estadisticas.ts`: `suma`, `promedio`, `maximo` sobre
      `number[]` con validación de array vacío (`null` o throw — elige y
      documenta).
  - id: s7
    tipo: explicacion
    titulo: 3. Tres katas arrays
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
