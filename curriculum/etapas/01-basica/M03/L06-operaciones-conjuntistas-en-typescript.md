---
id: L06
materia: M03
orden: 6
titulo: Operaciones conjuntistas en TypeScript
horas: 3
semana: 2
lectura: 'Rosen Cap. 2.2 — unión, intersección, diferencia, complemento (respecto a U)'
evidencia: 'src/sets.ts con ∪, ∩, \, ⊆, tests Vitest'
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Implementas las operaciones que Rosen define y las pruebas contra ejemplos
      finitos.


      **Objetivo de esta lección:** Implementar unión, intersección, diferencia,
      subconjunto y complemento relativo a un universo `U`; cubrir con tests.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Especificación
    xp: 10
    cuerpo: |-
      ```ts
      export function union<T>(a: Set<T>, b: Set<T>): Set<T> {
        return new Set([...a, ...b]);
      }

      export function interseccion<T>(a: Set<T>, b: Set<T>): Set<T> {
        return new Set([...a].filter((x) => b.has(x)));
      }

      export function diferencia<T>(a: Set<T>, b: Set<T>): Set<T> {
        return new Set([...a].filter((x) => !b.has(x)));
      }

      export function esSubconjunto<T>(a: Set<T>, b: Set<T>): boolean {
        for (const x of a) if (!b.has(x)) return false;
        return true;
      }

      export function complemento<T>(a: Set<T>, universo: Set<T>): Set<T> {
        return diferencia(universo, a);
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: >-
      ```ts

      export function union<T>(a: Set<T>, b: Set<T>): Set<T> {
        return new Set([...a, ...b]);
      }


      export function interseccion<T>(a: Set<T>, b: Set<T>): Set<T> {
        return new Set([...a].filter((x) => b.has(x)));
      }


      export function diferencia<T>(a: Set<T>, b: Set<T>): Set<T> {
        return new Set([...a].filter((x) => !b.has(x)));
      }


      export function esSubconjunto<T>(a: Set<T>, b: Set<T>): boolean {
        for (const x of a) if (!b.has(x)) return false;
        return true;
      }


      export function complemento<T>(a: Set<T>, universo: Set<T>): Set<T> {
        return diferencia(universo, a);
      }

      ```


      `projects/m03-discretas/src/sets.ts`: Añade `iguales(a,b)` por
      cardinalidad y doble inclusión si quieres rigor extra.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Operaciones conjuntistas en TypeScript», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`sets.ts` exporta las operaciones listadas y `npm test` pasa.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Operaciones
          conjuntistas en TypeScript
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
    pregunta: ¿Es recomendable en esta lección? “Complemento sin universo explícito."
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
          Implementar unión, intersección, diferencia, subconjunto y complemento
          relativo a un universo `U`; cubrir con tests.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests
    xp: 10
    cuerpo: >-
      `sets.test.ts`: al menos 2 casos por función, incluyendo conjuntos vacíos
      y `U` finito pequeño.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`sets.ts` exporta las operaciones listadas y `npm test` pasa.'
      - 'Manejas `∅` sin errores (unión con vacío, complemento de vacío).'
      - '`esSubconjunto` coincide con definición (∀x ∈ A → x ∈ B).'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Operaciones conjuntistas en TypeScript

**~3 h · Semana 2**

Implementas las operaciones que Rosen define y las pruebas contra ejemplos finitos.

## Objetivo

Implementar unión, intersección, diferencia, subconjunto y complemento relativo a un universo `U`; cubrir con tests.

## Pasos

### 1. Especificación (20 min)

En `apuntes/conjuntos.md`, añade sección **Operaciones** con definiciones:

- `A ∪ B = {x | x ∈ A ∨ x ∈ B}`
- `A ∩ B = {x | x ∈ A ∧ x ∈ B}`
- `A − B = {x | x ∈ A ∧ x ∉ B}`
- `Ā` respecto a `U`: `U − A`

### 2. Implementación (70–80 min)

`projects/m03-discretas/src/sets.ts`:

```ts
export function union<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a, ...b]);
}

export function interseccion<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a].filter((x) => b.has(x)));
}

export function diferencia<T>(a: Set<T>, b: Set<T>): Set<T> {
  return new Set([...a].filter((x) => !b.has(x)));
}

export function esSubconjunto<T>(a: Set<T>, b: Set<T>): boolean {
  for (const x of a) if (!b.has(x)) return false;
  return true;
}

export function complemento<T>(a: Set<T>, universo: Set<T>): Set<T> {
  return diferencia(universo, a);
}
```

Añade `iguales(a,b)` por cardinalidad y doble inclusión si quieres rigor extra.

### 3. Tests (40–50 min)

`sets.test.ts`: al menos 2 casos por función, incluyendo conjuntos vacíos y `U` finito pequeño.

```bash
npm test
```

### 4. Ejemplo aplicado (20 min)

Dado `U = {1..10}`, `A = pares`, `B = múltiplos de 3`, calcula a mano `|A ∩ B|` y verifica con tu código (construye los `Set` en un test o script `tsx`).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 2.2 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `sets.ts` exporta las operaciones listadas y `npm test` pasa.
2. Manejas `∅` sin errores (unión con vacío, complemento de vacío).
3. `esSubconjunto` coincide con definición (∀x ∈ A → x ∈ B).

## Errores comunes

- Complemento sin universo explícito.
- Mutar el `Set` de entrada al calcular unión.
- `filter` sobre `b` en intersección cuando deberías iterar el más pequeño (eficiencia: opcional, pero documenta).

## Siguiente

[L07 — Leyes de conjuntos y pruebas](L07-leyes-de-conjuntos-y-pruebas.md)
