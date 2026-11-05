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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `media`, `varianzaMuestral` y comprobar E[X]=np,
      Var(X)=np(1−p) para Binomial vía Monte Carlo.


      Calculas E[X] y Var(X) por definición en casos discretos y verificas con
      simulación; conectas varianza con “ruido” en métricas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Estadísticos
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Esperanza y varianza en código" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/src/stats-basic.ts + notas/esperanza-varianza.md
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
          Implementar `media`, `varianzaMuestral` y comprobar E[X]=np,
          Var(X)=np(1−p) para Binomial vía Monte Carlo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Verificación Binomial
    xp: 10
    cuerpo: >-
      Simula 20_000 valores `binomial(50, 0.2)`; compara media y varianza
      muestral con 10 y 50×0.2×0.8.
  - id: s7
    tipo: explicacion
    titulo: 3. Nota
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
