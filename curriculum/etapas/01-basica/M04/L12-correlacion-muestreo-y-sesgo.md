---
id: L12
materia: M04
orden: 12
titulo: 'Correlación, muestreo y sesgo'
horas: 5
semana: 3
lectura: Walpole correlación intro · OpenStax Ch. 2 (correlation)
evidencia: projects/m04-stats/src/correlacion.ts + notas/correlacion-no-causalidad.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Calculas correlación de Pearson entre dos columnas numéricas, escribes
      **correlación ≠ causalidad** con tu ejemplo y discutes sesgo de muestreo.


      **Objetivo de esta lección:** Cerrar P2 (pipeline + tablas + reflexión) y
      preparar inferencia de la semana 4.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Correlación
    xp: 10
    cuerpo: >-
      `src/correlacion.ts` — función `correlacionPearson(xs, ys)` (covarianza /
      producto de σ). Aplícala a `pedidos` vs `ingresos_mxn`.
  - id: s3
    tipo: ejemplo
    titulo: Nota obligatoria
    xp: 10
    cuerpo: >-
      `notas/correlacion-no-causalidad.md`: ```markdown # Correlación ≠
      causalidad
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Correlación, muestreo y sesgo», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: Correlación calculada y reportada con cautela.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Correlación, muestreo y
          sesgo
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
          Cerrar P2 (pipeline + tablas + reflexión) y preparar inferencia de la
          semana 4.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Correlación calculada y reportada con cautela.
      - Nota con ejemplo propio de no causalidad.
      - P2 lista para marcar en UI (pipeline completo).
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L12 — Correlación, muestreo y sesgo

**~5 h · Semana 3**

Calculas correlación de Pearson entre dos columnas numéricas, escribes **correlación ≠ causalidad** con tu ejemplo y discutes sesgo de muestreo.

## Objetivo

Cerrar P2 (pipeline + tablas + reflexión) y preparar inferencia de la semana 4.

## Pasos

### 1. Correlación (50 min)

`src/correlacion.ts` — función `correlacionPearson(xs, ys)` (covarianza / producto de σ). Aplícala a `pedidos` vs `ingresos_mxn`.

### 2. Nota obligatoria (45 min)

`notas/correlacion-no-causalidad.md`:

```markdown
# Correlación ≠ causalidad

## Mi ejemplo (software o producto)
-

## Tres razones alternativas (confusores)
1.
2.
3.

## Muestreo
¿Mi CSV representa a todos los días/canales? ¿Qué sesgo veo?
```

### 3. Checklist P2 (30 min)

Verifica en `projects/m04-stats/README.md`: limpieza, descriptivos, tablas commiteadas.

### 4. Lectura (90 min)

Correlación y limitaciones. Muestreo aleatorio simple (idea).

### 5. Commit

```bash
git commit -am "feat(m04): correlacion muestreo cierre P2 L12"
```

## Hecho cuando

1. Correlación calculada y reportada con cautela.
2. Nota con ejemplo propio de no causalidad.
3. P2 lista para marcar en UI (pipeline completo).
4. Commit.

## Siguiente

[L13 — Intervalos de confianza interpretados](L13-intervalos-de-confianza.md)
