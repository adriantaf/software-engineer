---
id: L16
materia: M03
orden: 16
titulo: 'Binomial, Pascal y Big-O de funciones propias'
horas: 3
semana: 4
lectura: Rosen Cap. 6.4 (coeficientes binomiales) + repaso complejidad en apuntes
evidencia: complejidad.md (5 funciones) + trianguloPascal fila n en counting.ts
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Relacionar `C(n,k)` con coeficientes binomiales; generar una
      fila de Pascal; redactar análisis Big-O de 5 funciones propias (incluye
      las de `sets`, `relations` o `counting`).


      Cierras conteo con el triángulo de Pascal y abres **P3**: analizar
      complejidad de **tus** funciones con argumento de peor caso.
  - id: s2
    tipo: ejemplo
    titulo: 1. Teorema del binomio
    xp: 10
    cuerpo: |-
      ```ts
      export function filaPascal(n: number): number[] {
        const row = [1];
        for (let k = 1; k <= n; k++) {
          row[k] = (row[k - 1] * (n - k + 1)) / k;
        }
        return row;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Binomial, Pascal y Big-O de funciones propias" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: complejidad.md (5 funciones) + trianguloPascal fila n en counting.ts
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
    pregunta: ¿Es buena práctica en esta lección? “Big-O sin definir qué es `n`."
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
          Relacionar `C(n,k)` con coeficientes binomiales; generar una fila de
          Pascal; redactar análisis Big-O de 5 funciones propias (incluye las
          de…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Código Pascal
    xp: 10
    cuerpo: >-
      ```ts

      export function filaPascal(n: number): number[] {
        const row = [1];
        for (let k = 1; k <= n; k++) {
          row[k] = (row[k - 1] * (n - k + 1)) / k;
        }
        return row;
      }

      ```


      Test: fila 5 = `[1,5,10,10,5,1]`; `filaPascal(n)[k] === nCk(n,k)` para n ≤
      12.
  - id: s7
    tipo: explicacion
    titulo: 3. complejidad.md (P3)
    xp: 10
    cuerpo: >-
      Crea `projects/m03-discretas/complejidad.md` con **5** funciones **tuyas**
      (de este proyecto o escritas para la tarea). Por cada una:


      - Código o firma.

      - **Peor caso** en términos de `n` (tamaño de entrada).

      - Clase Big-O (O, Ω si el libro lo pide) con **justificación** en 3–6
      frases (no solo el nombre).

      - Un ejemplo de entrada que dispara el peor caso.


      Incluye al menos: un bucle simple, un bucle anidado, y algo sobre
      `Set`/`Map`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`filaPascal` verificada contra `nCk`.'
      - '`complejidad.md` con 5 análisis completos (peor caso argumentado).'
      - No confundes `O(2^n)` con `O(n^2)` en tus propias funciones.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Binomial, Pascal y Big-O de funciones propias

**~3 h · Semana 4**

Cierras conteo con el triángulo de Pascal y abres **P3**: analizar complejidad de **tus** funciones con argumento de peor caso.

## Objetivo

Relacionar `C(n,k)` con coeficientes binomiales; generar una fila de Pascal; redactar análisis Big-O de 5 funciones propias (incluye las de `sets`, `relations` o `counting`).

## Pasos

### 1. Teorema del binomio (30 min)

En `conteo.md`: `(x+y)^n = ∑_{k=0}^n C(n,k) x^k y^{n-k}` y fila de Pascal como tabla.

### 2. Código Pascal (40 min)

```ts
export function filaPascal(n: number): number[] {
  const row = [1];
  for (let k = 1; k <= n; k++) {
    row[k] = (row[k - 1] * (n - k + 1)) / k;
  }
  return row;
}
```

Test: fila 5 = `[1,5,10,10,5,1]`; `filaPascal(n)[k] === nCk(n,k)` para n ≤ 12.

### 3. complejidad.md (P3) (80–90 min)

Crea `projects/m03-discretas/complejidad.md` con **5** funciones **tuyas** (de este proyecto o escritas para la tarea). Por cada una:

- Código o firma.
- **Peor caso** en términos de `n` (tamaño de entrada).
- Clase Big-O (O, Ω si el libro lo pide) con **justificación** en 3–6 frases (no solo el nombre).
- Un ejemplo de entrada que dispara el peor caso.

Incluye al menos: un bucle simple, un bucle anidado, y algo sobre `Set`/`Map`.

### 4. Demo opcional (30 min)

**Demo 10** (si aún no llegas a 10 en P1): identidad `C(n,k)=C(n-1,k-1)+C(n-1,k)` por argumento combinatorio.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 6.4 (binomio) |
| Ficha M03 | Criterio P3 |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `filaPascal` verificada contra `nCk`.
2. `complejidad.md` con 5 análisis completos (peor caso argumentado).
3. No confundes `O(2^n)` con `O(n^2)` en tus propias funciones.

## Errores comunes

- Big-O sin definir qué es `n`.
- “Es lineal” porque el gráfico se ve recto en un rango pequeño.
- Pascal con enteros flotantes sin redondeo (usa división entera cuando aplica).

## Siguiente

[L17 — Grafos: modelo y terminología](L17-grafos-modelo-y-terminologia.md)
