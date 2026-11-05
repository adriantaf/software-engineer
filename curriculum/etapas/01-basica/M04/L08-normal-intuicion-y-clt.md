---
id: L08
materia: M04
orden: 8
titulo: 'Normal, z-scores y preview del TCL'
horas: 5
semana: 2
lectura: 'Walpole cap. 6 (Normal, intro) · OpenStax Ch. 6–7'
evidencia: projects/m04-stats/src/normal-clt.ts + notas/normal-latencia.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Intuición de la Normal (sin integral obligatoria): z-score, histograma de
      medias muestrales y por qué muchas métricas “se parecen” a campana.


      **Objetivo de esta lección:** Simular medias de muestras de Bernoulli o
      uniforme y observar forma aproximadamente normal; interpretar un z-score
      en latencia de API.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Z-score
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): CLT preview y z-score L08"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: TCL preview
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): CLT preview y z-score L08"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Normal, z-scores y preview del TCL», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Script CLT ejecutado con histograma o resumen de medias.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Normal, z-scores y
          preview del TCL
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

      `git commit -am "feat(m04): CLT preview y z-score L08"`
    comandoEsperado:
      - 'git commit -am "feat(m04): CLT preview y z-score L08"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m04): CLT preview y z-score L08"'
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
          Simular medias de muestras de Bernoulli o uniforme y observar forma
          aproximadamente normal; interpretar un z-score en latencia de API.
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
    cuerpo: 'Walpole cap. 6 (Normal, tabla Z opcional). OpenStax CLT (Ch. 7 idea).'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Script CLT ejecutado con histograma o resumen de medias.
      - Nota con z-score de latencia interpretado (¿raro o no?).
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Normal, z-scores y preview del TCL

**~5 h · Semana 2**

Intuición de la Normal (sin integral obligatoria): z-score, histograma de medias muestrales y por qué muchas métricas “se parecen” a campana.

## Objetivo

Simular medias de muestras de Bernoulli o uniforme y observar forma aproximadamente normal; interpretar un z-score en latencia de API.

## Pasos

### 1. Z-score (30 min)

`notas/normal-latencia.md`:

\[
z = \frac{x - \mu}{\sigma}
\]

Ejemplo: latencia media histórica 120 ms, σ = 30, hoy 195 ms → z = ?

### 2. TCL preview (70 min)

`src/normal-clt.ts`: bucle que toma 5_000 muestras de tamaño n=30 de `bernoulli(0.3)`, guarda la **media** de cada muestra, imprime histograma de medias (bins en consola o array).

### 3. Lectura (90 min)

Walpole cap. 6 (Normal, tabla Z opcional). OpenStax CLT (Ch. 7 idea).

### 4. Cierre semana 2 (20 min)

Lista en nota qué distribuciones ya simulaste (Bernoulli, Binomial, medias).

### 5. Commit

```bash
git commit -am "feat(m04): CLT preview y z-score L08"
```

## Hecho cuando

1. Script CLT ejecutado con histograma o resumen de medias.
2. Nota con z-score de latencia interpretado (¿raro o no?).
3. Commit.

## Siguiente

[L09 — Descriptivos y primer pipeline CSV](L09-descriptivos-y-csv.md)
