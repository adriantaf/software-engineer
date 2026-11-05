---
id: L15
materia: M03
orden: 15
titulo: Principio de inclusión-exclusión
horas: 2.5
semana: 4
lectura: Rosen Cap. 6.2 — inclusión-exclusión para dos y tres conjuntos
evidencia: conteo.md problema |A∪B| + demo o cálculo verificado
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Aplicar `|A ∪ B| = |A| + |B| − |A ∩ B|` y la versión de tres
      conjuntos; resolver un problema de conteo con intersección no vacía.


      Cuando los casos **no** son disjuntos, la regla de la suma falla;
      inclusion-exclusión corrige el doble conteo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Fórmulas
    xp: 10
    cuerpo: |-
      ```ts
      export function cardinalidad<T>(a: Set<T>): number {
        return a.size;
      }

      export function unionSize<T>(a: Set<T>, b: Set<T>): number {
        return union(a, b).size;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Principio de inclusión-exclusión" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: conteo.md problema |A∪B| + demo o cálculo verificado
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
      ¿Es buena práctica en esta lección? “Sumar `|A|` y `|B|` sin restar
      intersección."
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
          Aplicar `|A ∪ B| = |A| + |B| − |A ∩ B|` y la versión de tres
          conjuntos; resolver un problema de conteo con intersección no vacía.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Problema tipo encuesta
    xp: 10
    cuerpo: >-
      Ejemplo clásico: estudiantes que estudian idioma A, idioma B, ambos —
      calcula solo A, solo B, ninguno si te dan totales. Adapta números propios;
      muestra cada región del Venn.
  - id: s7
    tipo: ejemplo
    titulo: 3. Con conjuntos en código
    xp: 10
    cuerpo: |-
      ```ts
      export function cardinalidad<T>(a: Set<T>): number {
        return a.size;
      }

      export function unionSize<T>(a: Set<T>, b: Set<T>): number {
        return union(a, b).size;
      }
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Problema resuelto con fórmula 2 o 3 conjuntos y Venn.
      - Verificación con `Set` en TS coincide con el cálculo a mano.
      - Explicas qué se “resta dos veces” sin inclusion-exclusión.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — Principio de inclusión-exclusión

**~2.5 h · Semana 4**

Cuando los casos **no** son disjuntos, la regla de la suma falla; inclusion-exclusión corrige el doble conteo.

## Objetivo

Aplicar `|A ∪ B| = |A| + |B| − |A ∩ B|` y la versión de tres conjuntos; resolver un problema de conteo con intersección no vacía.

## Pasos

### 1. Fórmulas (30 min)

En `conteo.md`, escribe las fórmulas para 2 y 3 conjuntos y un diagrama de Venn comentado.

### 2. Problema tipo encuesta (60–70 min)

Ejemplo clásico: estudiantes que estudian idioma A, idioma B, ambos — calcula solo A, solo B, ninguno si te dan totales. Adapta números propios; muestra cada región del Venn.

### 3. Con conjuntos en código (40 min)

Usa `sets.ts` con universo finito etiquetado:

```ts
export function cardinalidad<T>(a: Set<T>): number {
  return a.size;
}

export function unionSize<T>(a: Set<T>, b: Set<T>): number {
  return union(a, b).size;
}
```

Verifica numéricamente tu problema del paso 2.

### 4. Rosen (30 min)

Un ejercicio 6.2 adicional.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 6.2 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. Problema resuelto con fórmula 2 o 3 conjuntos y Venn.
2. Verificación con `Set` en TS coincide con el cálculo a mano.
3. Explicas qué se “resta dos veces” sin inclusion-exclusión.

## Errores comunes

- Sumar `|A|` y `|B|` sin restar intersección.
- Tres conjuntos: olvidar términos `+|A∩B∩C|` o signos alternos.
- Universo no acotado en problemas de “al menos uno”.

## Siguiente

[L16 — Binomial, Pascal y Big-O de funciones propias](L16-binomial-y-complejidad.md)
