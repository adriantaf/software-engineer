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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir orden parcial (reflexivo, antisimétrico, transitivo)
      y orden total; construir matriz de relación; ejemplo de divisibilidad.


      No todo es equivalencia: el orden importa para colas de prioridad,
      dependencias y DAGs.
  - id: s2
    tipo: ejemplo
    titulo: 1. Apuntes
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Órdenes parciales y totales" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          apuntes/ordenes.md + matrizRelacion() + test divisibilidad en
          {2,4,6,12}
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
      ¿Es buena práctica en esta lección? “Llamar “orden” a una relación no
      transitiva."
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
          Definir orden parcial (reflexivo, antisimétrico, transitivo) y orden
          total; construir matriz de relación; ejemplo de divisibilidad.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Diagrama
    xp: 10
    cuerpo: >-
      Dibuja diagrama de Hasse (a mano, foto o ASCII) para divisores de 12 con
      `|`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Matriz de relación (P2 parcial)
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
