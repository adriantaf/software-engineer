---
id: L03
materia: M04
orden: 3
titulo: Independencia y probabilidad condicional
horas: 5
semana: 1
lectura: 'Walpole cap. 2 (condicional, independencia) · OpenStax Ch. 3'
evidencia: projects/m04-stats/src/condicional.ts + notas/independencia-producto.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Simular o calcular un ejemplo de P(A|B) y documentar un caso
      donde asumir independencia rompe un funnel o un modelo de riesgo.


      **Condicional:** restringes el espacio a lo que ya pasó (B).  

      **Independencia:** P(A|B) = P(A) — saber B no cambia A.


      En funnels: “¿compró dado que abrió el carrito?” es condicional, no
      marginal.
  - id: s2
    tipo: ejemplo
    titulo: 1. Tabla de contingencia pequeña
    xp: 10
    cuerpo: |-
      ```ts
      export function pCondicional(
        cuentaAB: number,
        cuentaB: number,
      ): number {
        if (cuentaB === 0) return NaN;
        return cuentaAB / cuentaB;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Independencia y probabilidad condicional" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: >-
          projects/m04-stats/src/condicional.ts +
          notas/independencia-producto.md
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
      ¿Es buena práctica en esta lección? “Confundir P(A|B) con P(B|A) (lo
      arreglas formalmente en L04 con Bayes)."
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
          Simular o calcular un ejemplo de P(A|B) y documentar un caso donde
          asumir independencia rompe un funnel o un modelo de riesgo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Código de verificación
    xp: 10
    cuerpo: >-
      `src/condicional.ts` — funciones:


      ```ts

      export function pCondicional(
        cuentaAB: number,
        cuentaB: number,
      ): number {
        if (cuentaB === 0) return NaN;
        return cuentaAB / cuentaB;
      }

      ```


      Opcional: simula dos monedas independientes y estima P(segunda cara |
      primera cara) ≈ 0.5.
  - id: s7
    tipo: explicacion
    titulo: 3. Nota de producto
    xp: 10
    cuerpo: |-
      `notas/independencia-producto.md`:

      ```markdown
      Independencia vs condicional
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Tabla y tres probabilidades calculadas (en nota o script).
      - '`condicional.ts` con `pCondicional` usado en el ejemplo.'
      - Nota con funnel y párrafo base-rate.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Independencia y probabilidad condicional

**~5 h · Semana 1**

Calculas P(A|B), distingues independencia de “no correlación visual” y evitas el error base-rate en decisiones de producto.

## Objetivo

Simular o calcular un ejemplo de P(A|B) y documentar un caso donde asumir independencia rompe un funnel o un modelo de riesgo.

## Idea clave

**Condicional:** restringes el espacio a lo que ya pasó (B).  
**Independencia:** P(A|B) = P(A) — saber B no cambia A.

En funnels: “¿compró dado que abrió el carrito?” es condicional, no marginal.

## Pasos

### 1. Tabla de contingencia pequeña (45 min)

Inventa o usa datos de ejemplo (30 sesiones):

| | Compra (C) | No compra |
|---|------------|-----------|
| Vio promo (V) | 8 | 12 |
| No vio promo | 2 | 8 |

Calcula a mano:

- P(C)
- P(C|V)
- P(C|¬V)

¿V “ayuda”? Compara condicionales, no solo totales.

### 2. Código de verificación (50 min)

`src/condicional.ts` — funciones:

```ts
export function pCondicional(
  cuentaAB: number,
  cuentaB: number,
): number {
  if (cuentaB === 0) return NaN;
  return cuentaAB / cuentaB;
}
```

Opcional: simula dos monedas independientes y estima P(segunda cara | primera cara) ≈ 0.5.

### 3. Nota de producto (40 min)

`notas/independencia-producto.md`:

```markdown
# Independencia vs condicional

## Ejemplo funnel (tabla arriba)
- P(C|V) =
- Conclusión cauta:

## Caso donde asumir independencia falla
(ej. dispositivo móvil y tipo de usuario)

## Base rate (1 párrafo)
Por qué “el 90% de churners no abrió el email” no implica que el email salve al 90%.
```

### 4. Lectura (60 min)

Walpole: probabilidad condicional, regla del producto, independencia.

### 5. Commit

```bash
git commit -am "docs(m04): condicional e independencia L03"
```

## Lectura de esta lección

| Fuente | Foco |
|--------|------|
| Walpole | Cap. 2 — conditional probability |
| OpenStax | Ch. 3 — conditional / independent events |
| Catálogo | [Bibliografía · M04](../../../bibliografia.md#m04-probabilidad-y-estadistica) |


## Hecho cuando

1. Tabla y tres probabilidades calculadas (en nota o script).
2. `condicional.ts` con `pCondicional` usado en el ejemplo.
3. Nota con funnel y párrafo base-rate.
4. Commit.

## Errores comunes

- Confundir P(A|B) con P(B|A) (lo arreglas formalmente en L04 con Bayes).
- Decir “independiente” porque dos gráficos “se ven” separados con poca data.

## Siguiente

[L04 — Bayes intro para decisiones de producto](L04-bayes-intro-producto.md)
