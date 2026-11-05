---
id: L10
materia: M03
orden: 10
titulo: Equivalencias y particiones
horas: 2.5
semana: 3
lectura: 'Rosen Cap. 9.5 — relaciones de equivalencia, clases, particiones'
evidencia: demos.md Demo 7 (equivale a mod n) + clasesDeEquivalencia() en relations.ts
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Una relación de equivalencia **parte** el conjunto en clases disjuntas. Es
      el modelo de `=` en tipos, congruencias y componentes conexas (más
      adelante en grafos).


      **Objetivo de esta lección:** Probar que `≡ (mod m)` es relación de
      equivalencia; calcular clases de equivalencia en un conjunto finito.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Definición
    xp: 10
    cuerpo: |-
      ```ts
      export function clasesDeEquivalencia<A>(
        r: Relacion<A>,
        universo: Set<A>,
      ): Set<Set<A>> {
        // Encuentra clases por representante: para cada x no visitado, clase = { y | (x,y)∈R }
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Demostración
    xp: 10
    cuerpo: |-
      ```ts
      export function clasesDeEquivalencia<A>(
        r: Relacion<A>,
        universo: Set<A>,
      ): Set<Set<A>> {
        // Encuentra clases por representante: para cada x no visitado, clase = { y | (x,y)∈R }
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Equivalencias y particiones», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: Demo 7 completa en `demos.md`.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Equivalencias y
          particiones
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
      ¿Es recomendable en esta lección? “Clases que se solapan (error al definir
      representante)."
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
          Probar que `≡ (mod m)` es relación de equivalencia; calcular clases de
          equivalencia en un conjunto finito.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Clases en finito
    xp: 10
    cuerpo: >-
      En `A = {0,1,…,11}`, `m = 4`: lista clases `[0]`, `[1]`, … sin repetir
      representantes.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Demo 7 completa en `demos.md`.
      - '`clasesDeEquivalencia` pasa test modular pequeño.'
      - 'Dibujas la partición de `{0..11}` mod 4.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Equivalencias y particiones

**~2.5 h · Semana 3**

Una relación de equivalencia **parte** el conjunto en clases disjuntas. Es el modelo de `=` en tipos, congruencias y componentes conexas (más adelante en grafos).

## Objetivo

Probar que `≡ (mod m)` es relación de equivalencia; calcular clases de equivalencia en un conjunto finito.

## Pasos

### 1. Definición (20 min)

En `relaciones.md`: relación de equivalencia = reflexiva + simétrica + transitiva. Teorema: particiona `A` en clases disjuntas cuya unión es `A`.

### 2. Demostración (50–60 min)

**Demo 7** en `demos.md`: en `ℤ` (o en `ℕ` con cuidado), `a ≡ b (mod m)` iff `m | (a−b)` es equivalencia. Prueba las tres propiedades (m fijo ≥ 2).

### 3. Clases en finito (40 min)

En `A = {0,1,…,11}`, `m = 4`: lista clases `[0]`, `[1]`, … sin repetir representantes.

### 4. Implementación (50 min)

```ts
export function clasesDeEquivalencia<A>(
  r: Relacion<A>,
  universo: Set<A>,
): Set<Set<A>> {
  // Encuentra clases por representante: para cada x no visitado, clase = { y | (x,y)∈R }
}
```

Asume `r` ya es equivalencia (documenta). Tests con `mod 3` en `{0,1,2,3,4,5}`.

### 5. Puente conceptual (15 min)

Una frase: cómo esto se parece a “agrupar usuarios con el mismo rol” o “nodos en la misma componente”.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 9.5 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. Demo 7 completa en `demos.md`.
2. `clasesDeEquivalencia` pasa test modular pequeño.
3. Dibujas la partición de `{0..11}` mod 4.

## Errores comunes

- Clases que se solapan (error al definir representante).
- Usar `mod` en TS con negativos sin normalizar (documenta convención).
- Confundir clase con conjunto de todos los pares.

## Siguiente

[L11 — Órdenes parciales y totales](L11-ordenes-parciales-y-totales.md)
