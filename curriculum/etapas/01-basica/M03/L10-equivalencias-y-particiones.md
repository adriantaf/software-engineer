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
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Probar que `≡ (mod m)` es relación de equivalencia; calcular
      clases de equivalencia en un conjunto finito.


      Una relación de equivalencia **parte** el conjunto en clases disjuntas. Es
      el modelo de `=` en tipos, congruencias y componentes conexas (más
      adelante en grafos).
  - id: s2
    tipo: ejemplo
    titulo: 1. Definición
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Equivalencias y particiones" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          demos.md Demo 7 (equivale a mod n) + clasesDeEquivalencia() en
          relations.ts
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
      ¿Es buena práctica en esta lección? “Clases que se solapan (error al
      definir representante)."
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
          Probar que `≡ (mod m)` es relación de equivalencia; calcular clases de
          equivalencia en un conjunto finito.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Demostración
    xp: 10
    cuerpo: >-
      **Demo 7** en `demos.md`: en `ℤ` (o en `ℕ` con cuidado), `a ≡ b (mod m)`
      iff `m | (a−b)` es equivalencia. Prueba las tres propiedades (m fijo ≥ 2).
  - id: s7
    tipo: explicacion
    titulo: 3. Clases en finito
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
