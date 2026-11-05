---
id: L03
materia: M03
orden: 3
titulo: Predicados y cuantificadores
horas: 3
semana: 1
lectura: 'Rosen Cap. 1.4–1.5 — predicados, ∀, ∃, dominio, negación de cuantificadores'
evidencia: apuntes/predicados.md + 5 enunciados ∀/∃ traducidos ES ↔ lógica
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Traducir enunciados del español a ∀/∃ con dominio explícito;
      negar cuantificadores correctamente; reconocer orden de cuantificadores.


      La lógica proposicional no alcanza para “todo entero” o “existe un x tal
      que…”. Entran **predicados** y cuantificadores.
  - id: s2
    tipo: ejemplo
    titulo: 1. Predicados y dominio
    xp: 10
    cuerpo: |-
      ```ts
      export function todos<T>(xs: T[], p: (x: T) => boolean): boolean {
        return xs.every(p);
      }

      export function existe<T>(xs: T[], p: (x: T) => boolean): boolean {
        return xs.some(p);
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Predicados y cuantificadores" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: apuntes/predicados.md + 5 enunciados ∀/∃ traducidos ES ↔ lógica
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
      ¿Es buena práctica en esta lección? “Olvidar el dominio (“para todo x” sin
      decir de dónde es x)."
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
          Traducir enunciados del español a ∀/∃ con dominio explícito; negar
          cuantificadores correctamente; reconocer orden de cuantificadores.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Traducciones bidireccionales
    xp: 10
    cuerpo: |-
      Escribe **5 pares** (español ↔ fórmula). Incluye al menos:

      1. ∀ sobre enteros (ej. “todo entero mayor que 1…”).
      2. ∃ sobre reales o enteros.
      3. ∀∃ (para todo … existe …).
      4. ∃∀ (existe … tal que para todo …).
      5. Negación de un cuantificador (ej. “no todos…” ↔ ∃…¬).

      Siempre declara `D` en cada enunciado.
  - id: s7
    tipo: explicacion
    titulo: 3. Negaciones
    xp: 10
    cuerpo: >-
      Reglas (demuestra con equivalencia o ejemplo):


      - ¬(∀x P(x)) ↔ ∃x ¬P(x)

      - ¬(∃x P(x)) ↔ ∀x ¬P(x)


      Aplica a **2** enunciados del paso 2: escribe la negación en español y en
      fórmula.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `predicados.md` tiene 5 traducciones con dominio y 2 negaciones
        trabajadas.
      - '`todos` / `existe` tienen tests en un dominio finito.'
      - Distingues ∀∃ de ∃∀ con un ejemplo donde el significado cambia.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Predicados y cuantificadores

**~3 h · Semana 1**

La lógica proposicional no alcanza para “todo entero” o “existe un x tal que…”. Entran **predicados** y cuantificadores.

## Objetivo

Traducir enunciados del español a ∀/∃ con dominio explícito; negar cuantificadores correctamente; reconocer orden de cuantificadores.

## Pasos

### 1. Predicados y dominio (30 min)

En `projects/m03-discretas/apuntes/predicados.md`:

- Definición: predicado `P(x)` sobre un dominio `D`.
- Ejemplo: `D = ℤ`, `P(x)`: “x es par”.
- Diferencia entre **variable ligada** y **libre**.

### 2. Traducciones bidireccionales (60–70 min)

Escribe **5 pares** (español ↔ fórmula). Incluye al menos:

1. ∀ sobre enteros (ej. “todo entero mayor que 1…”).
2. ∃ sobre reales o enteros.
3. ∀∃ (para todo … existe …).
4. ∃∀ (existe … tal que para todo …).
5. Negación de un cuantificador (ej. “no todos…” ↔ ∃…¬).

Siempre declara `D` en cada enunciado.

### 3. Negaciones (40 min)

Reglas (demuestra con equivalencia o ejemplo):

- ¬(∀x P(x)) ↔ ∃x ¬P(x)
- ¬(∃x P(x)) ↔ ∀x ¬P(x)

Aplica a **2** enunciados del paso 2: escribe la negación en español y en fórmula.

### 4. Puente a código (30 min)

En `src/logic.ts` (o `src/predicates.ts`):

```ts
export function todos<T>(xs: T[], p: (x: T) => boolean): boolean {
  return xs.every(p);
}

export function existe<T>(xs: T[], p: (x: T) => boolean): boolean {
  return xs.some(p);
}
```

Tests: dominio finito `xs = [1,2,3,4]` y predicados “par”, “> 2”, etc. Relaciona con ∀/∃ **solo cuando el dominio es la lista** (limitación explícita en el apunte).

### 5. Lectura activa (30 min)

Rosen 1.4–1.5: resuelve 1 ejercicio de traducción y 1 de negación en `predicados.md`.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Rosen | Cap. 1.4–1.5 |
| Apuntes | `leyes-logicas.md` (implicación en enunciados) |
| Catálogo | [Bibliografía · M03](../../../bibliografia.md#m03-matematicas-discretas) |


## Hecho cuando

1. `predicados.md` tiene 5 traducciones con dominio y 2 negaciones trabajadas.
2. `todos` / `existe` tienen tests en un dominio finito.
3. Distingues ∀∃ de ∃∀ con un ejemplo donde el significado cambia.

## Errores comunes

- Olvidar el dominio (“para todo x” sin decir de dónde es x).
- Negar mal: ¬∀x P(x) como ∀x ¬P(x).
- Creer que `todos` en código es igual a ∀ sobre ℤ (solo finito listado).

## Siguiente

[L04 — Métodos de demostración (intro)](L04-metodos-de-demostracion.md)
