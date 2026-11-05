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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Simular medias de muestras de Bernoulli o uniforme y
      observar forma aproximadamente normal; interpretar un z-score en latencia
      de API.


      Intuición de la Normal (sin integral obligatoria): z-score, histograma de
      medias muestrales y por qué muchas métricas “se parecen” a campana.
  - id: s2
    tipo: ejemplo
    titulo: 1. Z-score
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): CLT preview y z-score L08"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Normal, z-scores y preview del TCL" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/src/normal-clt.ts + notas/normal-latencia.md
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "feat(m04): CLT preview y z-score L08"`
    comandoEsperado:
      - 'git commit -am "feat(m04): CLT preview y z-score L08"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m04): CLT preview y z-score L08"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Simular medias de muestras de Bernoulli o uniforme y observar forma
          aproximadamente normal; interpretar un z-score en latencia de API.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. TCL preview
    xp: 10
    cuerpo: >-
      `src/normal-clt.ts`: bucle que toma 5_000 muestras de tamaño n=30 de
      `bernoulli(0.3)`, guarda la **media** de cada muestra, imprime histograma
      de medias (bins en consola o array).
  - id: s7
    tipo: explicacion
    titulo: 3. Lectura
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
