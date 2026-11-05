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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Definir variable aleatoria discreta, implementar muestreo
      Bernoulli y relacionar p con una tasa de conversión.


      Modelas éxito/fracaso (clic, crash, compra) como Bernoulli(p) y comparas
      simulación con media teórica p.
  - id: s2
    tipo: ejemplo
    titulo: 1. Definiciones en nota
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Variables aleatorias y Bernoulli" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/src/bernoulli.ts + notas/bernoulli-conversion.md
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
    titulo: Método
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      Debes producir algo verificable (código, nota, commit) además de leer,
      antes de dar la lección por hecha.
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: 'Verdadero: práctica deliberada + evidencia.'
    explicacionOk: Exacto.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Definir variable aleatoria discreta, implementar muestreo Bernoulli y
          relacionar p con una tasa de conversión.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `src/bernoulli.ts`
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
  - id: s7
    tipo: explicacion
    titulo: 3. Producto
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
