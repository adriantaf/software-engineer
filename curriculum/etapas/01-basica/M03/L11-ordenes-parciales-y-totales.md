---
id: L11
materia: M03
orden: 11
titulo: Órdenes parciales y totales
horas: 2.5
semana: 3
lectura: 'Rosen Cap. 9.6 — orden parcial, orden total, diagrama de Hasse (intro)'
evidencia: 'apuntes/ordenes.md + matrizRelacion() + test divisibilidad en {2,4,6,12}'
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      No todo es equivalencia: el orden importa para colas de prioridad,
      dependencias y DAGs.


      **Objetivo de esta lección:** Definir orden parcial (reflexivo,
      antisimétrico, transitivo) y orden total; construir matriz de relación;
      ejemplo de divisibilidad.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Apuntes
    xp: 10
    cuerpo: |-
      ```ts
      export function matrizRelacion<A>(
        r: Relacion<A>,
        elementos: A[],
      ): number[][] {
        const n = elementos.length;
        const idx = new Map(elementos.map((e, i) => [e, i]));
        const m = Array.from({ length: n }, () => Array(n).fill(0));
        for (const [a, b] of r) {
          const i = idx.get(a)!;
          const j = idx.get(b)!;
          m[i][j] = 1;
        }
        return m;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Diagrama
    xp: 10
    cuerpo: |-
      ```ts
      export function matrizRelacion<A>(
        r: Relacion<A>,
        elementos: A[],
      ): number[][] {
        const n = elementos.length;
        const idx = new Map(elementos.map((e, i) => [e, i]));
        const m = Array.from({ length: n }, () => Array(n).fill(0));
        for (const [a, b] of r) {
          const i = idx.get(a)!;
          const j = idx.get(b)!;
          m[i][j] = 1;
        }
        return m;
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Órdenes parciales y totales», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`ordenes.md` con definiciones y Hasse de divisores de 12.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Órdenes parciales y
          totales
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
      ¿Es recomendable en esta lección? “Llamar “orden” a una relación no
      transitiva."
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
          Definir orden parcial (reflexivo, antisimétrico, transitivo) y orden
          total; construir matriz de relación; ejemplo de divisibilidad.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Matriz de relación (P2 parcial)
    xp: 10
    cuerpo: >-
      En `src/relations.ts`: Test: relación “divide” en `{2,4,6,12}`; verifica
      antisimétrica y transitiva con tus predicados de L09.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`ordenes.md` con definiciones y Hasse de divisores de 12.'
      - '`matrizRelacion` con test coherente con la relación elegida.'
      - >-
        Distingues parcial vs total con un ejemplo de cada uno en el mismo
        conjunto finito.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Órdenes parciales y totales

**~2.5 h · Semana 3**

No todo es equivalencia: el orden importa para colas de prioridad, dependencias y DAGs.

## Objetivo

Definir orden parcial (reflexivo, antisimétrico, transitivo) y orden total; construir matriz de relación; ejemplo de divisibilidad.

## Pasos

### 1. Apuntes (40 min)

`projects/m03-discretas/apuntes/ordenes.md`:

- Orden parcial `(A, ≤)`.
- Orden total: además, ∀a,b ∈ A, a ≤ b ∨ b ≤ a.
- Ejemplo: divisibilidad en divisores de 12 vs inclusión de subconjuntos de `{a,b}`.

### 2. Diagrama (30 min)

Dibuja diagrama de Hasse (a mano, foto o ASCII) para divisores de 12 con `|`.

### 3. Matriz de relación (P2 parcial) (60 min)

En `src/relations.ts`:

```ts
export function matrizRelacion<A>(
  r: Relacion<A>,
  elementos: A[],
): number[][] {
  const n = elementos.length;
  const idx = new Map(elementos.map((e, i) => [e, i]));
  const m = Array.from({ length: n }, () => Array(n).fill(0));
  for (const [a, b] of r) {
    const i = idx.get(a)!;
    const j = idx.get(b)!;
    m[i][j] = 1;
  }
  return m;
}
```

Test: relación “divide” en `{2,4,6,12}`; verifica antisimétrica y transitiva con tus predicados de L09.

### 4. Comparación (20 min)

¿Es `≤` en ℝ un orden total? ¿Y divisibilidad en ℤ⁺? Respuesta corta en `ordenes.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 9.6 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `ordenes.md` con definiciones y Hasse de divisores de 12.
2. `matrizRelacion` con test coherente con la relación elegida.
3. Distingues parcial vs total con un ejemplo de cada uno en el mismo conjunto finito.

## Errores comunes

- Llamar “orden” a una relación no transitiva.
- Hasse con todas las aristas redundantes (incluir reflexivos).
- Matriz sin orden fijo de elementos (documenta el orden de filas/columnas).

## Siguiente

[L12 — Inducción matemática](L12-induccion-matematica.md)
