---
id: L12
materia: M03
orden: 12
titulo: Inducción matemática
horas: 3
semana: 3
lectura: 'Rosen Cap. 5.1 — inducción simple, hipótesis inductiva, paso inductivo'
evidencia: demos.md Demo 8–9 (sumatorio y otra) + src/induction.ts (suma 1..n verificada)
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Formular correctamente base e hipótesis inductiva; demostrar
      dos identidades por inducción; relacionar con función recursiva en TS.


      Cierras la semana 3 con el método que usarás para algoritmos recursivos y
      estructuras.
  - id: s2
    tipo: ejemplo
    titulo: 1. Plantilla de inducción
    xp: 10
    cuerpo: |-
      ```ts
      export function sumaHasta(n: number): number {
        if (n <= 0) return 0;
        return n + sumaHasta(n - 1);
      }

      export function sumaFormula(n: number): number {
        return (n * (n + 1)) / 2;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Inducción matemática" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: >-
          demos.md Demo 8–9 (sumatorio y otra) + src/induction.ts (suma 1..n
          verificada)
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
      ¿Es buena práctica en esta lección? ““Asumir” `P(k+1)` en lugar de
      derivarlo de `P(k)`."
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
          Formular correctamente base e hipótesis inductiva; demostrar dos
          identidades por inducción; relacionar con función recursiva en TS.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Sumatorio clásico
    xp: 10
    cuerpo: >-
      **Demo 8:** `∑_{i=1}^n i = n(n+1)/2` para `n ∈ ℕ` (con tu convención de
      ℕ).


      Prueba completa en `demos.md`.
  - id: s7
    tipo: explicacion
    titulo: 3. Segunda inducción
    xp: 10
    cuerpo: |-
      **Demo 9:** elige una de:

      - `2^n > n` para `n ≥ 1`.
      - `3 | (4^n − 1)` para `n ≥ 1`.
      - Número de regiones con rectas (si el libro lo trae).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Dos demostraciones por inducción (Demo 8 y 9) bien estructuradas.
      - Tests de suma recursiva vs fórmula pasan.
      - Identificas en tu Demo 8 dónde usas la HI explícitamente.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Inducción matemática

**~3 h · Semana 3**

Cierras la semana 3 con el método que usarás para algoritmos recursivos y estructuras.

## Objetivo

Formular correctamente base e hipótesis inductiva; demostrar dos identidades por inducción; relacionar con función recursiva en TS.

## Pasos

### 1. Plantilla de inducción (20 min)

En `apuntes/induccion.md`, escribe la plantilla:

1. **Base:** `P(1)` o `P(0)` según el enunciado.
2. **Hipótesis inductiva (HI):** suponer `P(k)`.
3. **Paso:** demostrar `P(k+1)` usando HI.
4. **Conclusión:** por inducción, ∀n …

### 2. Sumatorio clásico (50–60 min)

**Demo 8:** `∑_{i=1}^n i = n(n+1)/2` para `n ∈ ℕ` (con tu convención de ℕ).

Prueba completa en `demos.md`.

### 3. Segunda inducción (50 min)

**Demo 9:** elige una de:

- `2^n > n` para `n ≥ 1`.
- `3 | (4^n − 1)` para `n ≥ 1`.
- Número de regiones con rectas (si el libro lo trae).

### 4. Código recursivo (40 min)

`src/induction.ts`:

```ts
export function sumaHasta(n: number): number {
  if (n <= 0) return 0;
  return n + sumaHasta(n - 1);
}

export function sumaFormula(n: number): number {
  return (n * (n + 1)) / 2;
}
```

Tests: para `n = 0..50`, `sumaHasta(n) === sumaFormula(n)`. Comenta en el apunte: la prueba por inducción garantiza la igualdad; el test solo muestrea.

### 5. Retro semana 3 (15 min)

¿Cuántas demos llevas en `demos.md`? (objetivo P1: 10 al final del módulo).

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 5.1 |
| Apuntes | `induccion.md` |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. Dos demostraciones por inducción (Demo 8 y 9) bien estructuradas.
2. Tests de suma recursiva vs fórmula pasan.
3. Identificas en tu Demo 8 dónde usas la HI explícitamente.

## Errores comunes

- “Asumir” `P(k+1)` en lugar de derivarlo de `P(k)`.
- Base incorrecta (empezar en 1 cuando el enunciado es para 0).
- Inducción fuerte sin necesidad (está bien, pero justifica).

## Siguiente

[L13 — Conteo: regla del producto y la suma](L13-conteo-reglas-producto-y-suma.md)
