---
id: L06
materia: M04
orden: 6
titulo: 'Distribución binomial: fórmula vs simulación'
horas: 5
semana: 2
lectura: Walpole cap. 5 (Binomial) · OpenStax Ch. 4
evidencia: projects/m04-stats/src/binomial.ts + notas/binomial-ab-test.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cuentas éxitos en n ensayos independientes: simulas Binomial(n,p) y
      contrastas con la PMF teórica en un caso pequeño.


      **Objetivo de esta lección:** Implementar “n Bernoullis” y calcular P(X =
      k) con coeficiente binomial para n ≤ 20; interpretar n como tamaño de
      muestra de usuarios.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Simulación
    xp: 10
    cuerpo: >-
      ```ts

      import { bernoulli } from "./bernoulli";


      export function binomial(n: number, p: number): number {
        let s = 0;
        for (let i = 0; i < n; i++) s += bernoulli(p);
        return s;
      }


      export function factorial(n: number): number {
        let f = 1;
        for (let i = 2; i <= n; i++) f *= i;
        return f;
      }


      export function pmfBinomial(n: number, p: number, k: number): number {
        const comb = factorial(n) / (factorial(k) * factorial(n - k));
        return comb * Math.pow(p, k) * Math.pow(1 - p, n - k);
      }

      ```


      `src/binomial.ts`: Histograma manual: 10_000 valores de `binomial(20,
      0.3)` agrupados por k.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: A/B sin heroísmo
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): binomial sim y PMF L06"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Distribución binomial: fórmula vs simulación», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Simulación + al menos un k con PMF teórica comparada.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Distribución binomial:
          fórmula vs simul…
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
          Implementar “n Bernoullis” y calcular P(X = k) con coeficiente
          binomial para n ≤ 20; interpretar n como tamaño de muestra de
          usuarios.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Lectura
    xp: 10
    cuerpo: 'Walpole: Binomial. OpenStax: binomial distribution.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Simulación + al menos un k con PMF teórica comparada.
      - Nota A/B cautelosa.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L06 — Distribución binomial: fórmula vs simulación

**~5 h · Semana 2**

Cuentas éxitos en n ensayos independientes: simulas Binomial(n,p) y contrastas con la PMF teórica en un caso pequeño.

## Objetivo

Implementar “n Bernoullis” y calcular P(X = k) con coeficiente binomial para n ≤ 20; interpretar n como tamaño de muestra de usuarios.

## Pasos

### 1. Simulación (60 min)

`src/binomial.ts`:

```ts
import { bernoulli } from "./bernoulli";

export function binomial(n: number, p: number): number {
  let s = 0;
  for (let i = 0; i < n; i++) s += bernoulli(p);
  return s;
}

export function factorial(n: number): number {
  let f = 1;
  for (let i = 2; i <= n; i++) f *= i;
  return f;
}

export function pmfBinomial(n: number, p: number, k: number): number {
  const comb = factorial(n) / (factorial(k) * factorial(n - k));
  return comb * Math.pow(p, k) * Math.pow(1 - p, n - k);
}
```

Histograma manual: 10_000 valores de `binomial(20, 0.3)` agrupados por k.

### 2. A/B sin heroísmo (45 min)

`notas/binomial-ab-test.md`: “100 usuarios, 12 conversiones en A vs 15 en B” — ¿qué puedes decir **sin** aún hacer test formal? (Solo tamaño de efecto y cautela.)

### 3. Lectura (90 min)

Walpole: Binomial. OpenStax: binomial distribution.

### 4. Commit

```bash
git commit -am "feat(m04): binomial sim y PMF L06"
```

## Hecho cuando

1. Simulación + al menos un k con PMF teórica comparada.
2. Nota A/B cautelosa.
3. Commit.

## Siguiente

[L07 — Esperanza y varianza en código](L07-esperanza-y-varianza.md)
