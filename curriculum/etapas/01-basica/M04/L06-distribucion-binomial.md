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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar “n Bernoullis” y calcular P(X = k) con
      coeficiente binomial para n ≤ 20; interpretar n como tamaño de muestra de
      usuarios.


      Cuentas éxitos en n ensayos independientes: simulas Binomial(n,p) y
      contrastas con la PMF teórica en un caso pequeño.
  - id: s2
    tipo: ejemplo
    titulo: 1. Simulación
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Distribución binomial: fórmula vs simulación" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/src/binomial.ts + notas/binomial-ab-test.md
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
          Implementar “n Bernoullis” y calcular P(X = k) con coeficiente
          binomial para n ≤ 20; interpretar n como tamaño de muestra de
          usuarios.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. A/B sin heroísmo
    xp: 10
    cuerpo: >-
      `notas/binomial-ab-test.md`: “100 usuarios, 12 conversiones en A vs 15 en
      B” — ¿qué puedes decir **sin** aún hacer test formal? (Solo tamaño de
      efecto y cautela.)
  - id: s7
    tipo: explicacion
    titulo: 3. Lectura
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
