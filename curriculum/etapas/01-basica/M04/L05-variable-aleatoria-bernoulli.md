---
id: L05
materia: M04
orden: 5
titulo: Variables aleatorias y Bernoulli
horas: 5
semana: 2
lectura: Walpole cap. 5 (Bernoulli) · OpenStax Ch. 4 (Discrete RV)
evidencia: projects/m04-stats/src/bernoulli.ts + notas/bernoulli-conversion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Modelas éxito/fracaso (clic, crash, compra) como Bernoulli(p) y comparas
      simulación con media teórica p.


      **Objetivo de esta lección:** Definir variable aleatoria discreta,
      implementar muestreo Bernoulli y relacionar p con una tasa de conversión.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Definiciones en nota
    xp: 10
    cuerpo: |-
      ```ts
      export function bernoulli(p: number): 0 | 1 {
        return Math.random() < p ? 1 : 0;
      }

      export function simularBernoulli(n: number, p: number) {
        const xs: number[] = [];
        for (let i = 0; i < n; i++) xs.push(bernoulli(p));
        const media = xs.reduce((a, b) => a + b, 0) / n;
        return { xs, media };
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`src/bernoulli.ts`'
    xp: 10
    cuerpo: >-
      ```ts

      export function bernoulli(p: number): 0 | 1 {
        return Math.random() < p ? 1 : 0;
      }


      export function simularBernoulli(n: number, p: number) {
        const xs: number[] = [];
        for (let i = 0; i < n; i++) xs.push(bernoulli(p));
        const media = xs.reduce((a, b) => a + b, 0) / n;
        return { xs, media };
      }

      ```


      Compara media simulada con p para p = 0.07 (conversión típica) y n =
      50_000.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Variables aleatorias y Bernoulli», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`bernoulli.ts` con simulación y comparación p vs media muestral.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Variables aleatorias y
          Bernoulli
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Práctica deliberada
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      Además de leer, debes producir algo verificable (código, nota, commit o
      ejercicio) antes de dar la lección por hecha.
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: 'Verdadero: sin evidencia no hay progreso real.'
    explicacionOk: Exacto.
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
          Definir variable aleatoria discreta, implementar muestreo Bernoulli y
          relacionar p con una tasa de conversión.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Producto
    xp: 10
    cuerpo: >-
      Escribe: si mañana lanzas un botón, ¿qué supuesto Bernoulli estás
      haciendo? ¿Qué violaría el modelo (mismo usuario muchas veces)?
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`bernoulli.ts` con simulación y comparación p vs media muestral.'
      - Nota con definición y párrafo de producto.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L05 — Variables aleatorias y Bernoulli

**~5 h · Semana 2**

Modelas éxito/fracaso (clic, crash, compra) como Bernoulli(p) y comparas simulación con media teórica p.

## Objetivo

Definir variable aleatoria discreta, implementar muestreo Bernoulli y relacionar p con una tasa de conversión.

## Pasos

### 1. Definiciones en nota (30 min)

`notas/bernoulli-conversion.md`: PMF de Bernoulli, soporte {0,1}, parámetro p.

### 2. `src/bernoulli.ts` (60 min)

```ts
export function bernoulli(p: number): 0 | 1 {
  return Math.random() < p ? 1 : 0;
}

export function simularBernoulli(n: number, p: number) {
  const xs: number[] = [];
  for (let i = 0; i < n; i++) xs.push(bernoulli(p));
  const media = xs.reduce((a, b) => a + b, 0) / n;
  return { xs, media };
}
```

Compara media simulada con p para p = 0.07 (conversión típica) y n = 50_000.

### 3. Producto (40 min)

Escribe: si mañana lanzas un botón, ¿qué supuesto Bernoulli estás haciendo? ¿Qué violaría el modelo (mismo usuario muchas veces)?

### 4. Lectura (90 min)

Walpole cap. 5 (inicio, Bernoulli). OpenStax Ch. 4 discrete random variables.

### 5. Commit

```bash
git commit -am "feat(m04): Bernoulli y conversión L05"
```

## Hecho cuando

1. `bernoulli.ts` con simulación y comparación p vs media muestral.
2. Nota con definición y párrafo de producto.
3. Commit.

## Siguiente

[L06 — Distribución binomial: fórmula vs simulación](L06-distribucion-binomial.md)
