---
id: L07
materia: M04
orden: 7
titulo: Esperanza y varianza en código
horas: 5
semana: 2
lectura: 'Walpole cap. 5 (E[X], Var) · OpenStax Ch. 4–5'
evidencia: projects/m04-stats/src/stats-basic.ts + notas/esperanza-varianza.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Calculas E[X] y Var(X) por definición en casos discretos y verificas con
      simulación; conectas varianza con “ruido” en métricas.


      **Objetivo de esta lección:** Implementar `media`, `varianzaMuestral` y
      comprobar E[X]=np, Var(X)=np(1−p) para Binomial vía Monte Carlo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Estadísticos
    xp: 10
    cuerpo: |-
      ```ts
      export function media(xs: number[]): number {
        return xs.reduce((a, b) => a + b, 0) / xs.length;
      }

      export function varianzaMuestral(xs: number[]): number {
        const m = media(xs);
        return xs.reduce((s, x) => s + (x - m) ** 2, 0) / (xs.length - 1);
      }
      ```

      `src/stats-basic.ts` (reutiliza funciones de la ficha M04):
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Verificación Binomial
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): media varianza y binomial L07"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Esperanza y varianza en código», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: '`stats-basic.ts` con media y varianza muestral.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Esperanza y varianza en
          código
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
          Implementar `media`, `varianzaMuestral` y comprobar E[X]=np,
          Var(X)=np(1−p) para Binomial vía Monte Carlo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Nota
    xp: 10
    cuerpo: >-
      `notas/esperanza-varianza.md`: por qué dos features con la misma media
      pueden tener diferente riesgo (varianza en ingresos diarios).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`stats-basic.ts` con media y varianza muestral.'
      - Comparación teórica vs simulada documentada.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Esperanza y varianza en código

**~5 h · Semana 2**

Calculas E[X] y Var(X) por definición en casos discretos y verificas con simulación; conectas varianza con “ruido” en métricas.

## Objetivo

Implementar `media`, `varianzaMuestral` y comprobar E[X]=np, Var(X)=np(1−p) para Binomial vía Monte Carlo.

## Pasos

### 1. Estadísticos (50 min)

`src/stats-basic.ts` (reutiliza funciones de la ficha M04):

```ts
export function media(xs: number[]): number {
  return xs.reduce((a, b) => a + b, 0) / xs.length;
}

export function varianzaMuestral(xs: number[]): number {
  const m = media(xs);
  return xs.reduce((s, x) => s + (x - m) ** 2, 0) / (xs.length - 1);
}
```

### 2. Verificación Binomial (50 min)

Simula 20_000 valores `binomial(50, 0.2)`; compara media y varianza muestral con 10 y 50×0.2×0.8.

### 3. Nota (40 min)

`notas/esperanza-varianza.md`: por qué dos features con la misma media pueden tener diferente riesgo (varianza en ingresos diarios).

### 4. Lectura (90 min)

Walpole: esperanza y varianza de variables discretas.

### 5. Commit

```bash
git commit -am "feat(m04): media varianza y binomial L07"
```

## Hecho cuando

1. `stats-basic.ts` con media y varianza muestral.
2. Comparación teórica vs simulada documentada.
3. Commit.

## Siguiente

[L08 — Normal, z-scores y preview del TCL](L08-normal-intuicion-y-clt.md)
