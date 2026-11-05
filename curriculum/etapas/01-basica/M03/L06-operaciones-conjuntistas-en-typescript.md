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
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar unión, intersección, diferencia, subconjunto y
      complemento relativo a un universo `U`; cubrir con tests.


      Implementas las operaciones que Rosen define y las pruebas contra ejemplos
      finitos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Especificación
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Operaciones conjuntistas en TypeScript" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: 'src/sets.ts con ∪, ∩, \, ⊆, tests Vitest'
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
    pregunta: ¿Es buena práctica en esta lección? “Complemento sin universo explícito."
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
          Implementar unión, intersección, diferencia, subconjunto y complemento
          relativo a un universo `U`; cubrir con tests.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
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


      Añade `iguales(a,b)` por cardinalidad y doble inclusión si quieres rigor
      extra.
  - id: s7
    tipo: ejemplo
    titulo: 3. Tests
    xp: 10
    cuerpo: |-
      ```bash
      npm test
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`sets.ts` exporta las operaciones listadas y `npm test` pasa.'
      - 'Manejas `∅` sin errores (unión con vacío, complemento de vacío).'
      - '`esSubconjunto` coincide con definición (∀x ∈ A → x ∈ B).'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
