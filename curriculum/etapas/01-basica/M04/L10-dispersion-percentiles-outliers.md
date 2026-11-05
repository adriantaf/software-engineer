---
id: L10
materia: M04
orden: 10
titulo: 'Dispersión, percentiles y outliers'
horas: 5
semana: 3
lectura: Walpole descriptivos (dispersión) · OpenStax Ch. 2
evidencia: projects/m04-stats/src/percentiles.ts + salida/dispersion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Añades desviación estándar, IQR y regla de outliers; decides qué hacer con
      un día “Black Friday” en tus datos.


      **Objetivo de esta lección:** Extender el pipeline con σ, p25/p75 y
      documentar una decisión sobre outliers (mantener, etiquetar o excluir con
      justificación).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Funciones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): dispersion percentiles L10"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Informe corto
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): dispersion percentiles L10"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dispersión, percentiles y outliers», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`dispersion.md` con σ e IQR.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dispersión, percentiles
          y outliers
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "feat(m04): dispersion percentiles L10"`
    comandoEsperado:
      - 'git commit -am "feat(m04): dispersion percentiles L10"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m04): dispersion percentiles L10"'
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
          Extender el pipeline con σ, p25/p75 y documentar una decisión sobre
          outliers (mantener, etiquetar o excluir con justificación).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Decisión de negocio
    xp: 10
    cuerpo: >-
      Párrafo: “Si informo media de pedidos al dueño, ¿incluyo el outlier?” —
      consecuencias de cada opción.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`dispersion.md` con σ e IQR.'
      - Decisión sobre outliers justificada.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Dispersión, percentiles y outliers

**~5 h · Semana 3**

Añades desviación estándar, IQR y regla de outliers; decides qué hacer con un día “Black Friday” en tus datos.

## Objetivo

Extender el pipeline con σ, p25/p75 y documentar una decisión sobre outliers (mantener, etiquetar o excluir con justificación).

## Pasos

### 1. Funciones (60 min)

`src/percentiles.ts`: percentil empírico (ordenar + interpolación simple). Usa `varianzaMuestral` de L07 para σ.

### 2. Informe corto (50 min)

`salida/dispersion.md`: rango, σ, IQR, lista de fechas outlier (si hay).

### 3. Decisión de negocio (30 min)

Párrafo: “Si informo media de pedidos al dueño, ¿incluyo el outlier?” — consecuencias de cada opción.

### 4. Lectura (90 min)

Desviación, coeficiente de variación (si aparece en Walpole).

### 5. Commit

```bash
git commit -am "feat(m04): dispersion percentiles L10"
```

## Hecho cuando

1. `dispersion.md` con σ e IQR.
2. Decisión sobre outliers justificada.
3. Commit.

## Siguiente

[L11 — Visualización e histogramas para no técnicos](L11-visualizacion-e-histogramas.md)
