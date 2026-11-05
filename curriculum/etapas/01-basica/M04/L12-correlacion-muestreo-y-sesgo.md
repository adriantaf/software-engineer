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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cerrar P2 (pipeline + tablas + reflexión) y preparar
      inferencia de la semana 4.


      Calculas correlación de Pearson entre dos columnas numéricas, escribes
      **correlación ≠ causalidad** con tu ejemplo y discutes sesgo de muestreo.
  - id: s2
    tipo: ejemplo
    titulo: 1. Correlación
    xp: 10
    cuerpo: >-
      `src/correlacion.ts` — función `correlacionPearson(xs, ys)` (covarianza /
      producto de σ). Aplícala a `pedidos` vs `ingresos_mxn`.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Correlación, muestreo y sesgo" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: >-
          projects/m04-stats/src/correlacion.ts +
          notas/correlacion-no-causalidad.md
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
          Cerrar P2 (pipeline + tablas + reflexión) y preparar inferencia de la
          semana 4.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Nota obligatoria
    xp: 10
    cuerpo: |-
      `notas/correlacion-no-causalidad.md`:

      ```markdown
      Correlación ≠ causalidad
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Correlación calculada y reportada con cautela.
      - Nota con ejemplo propio de no causalidad.
      - P2 lista para marcar en UI (pipeline completo).
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
