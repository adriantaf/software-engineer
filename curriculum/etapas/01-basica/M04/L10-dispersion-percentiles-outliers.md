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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Extender el pipeline con σ, p25/p75 y documentar una
      decisión sobre outliers (mantener, etiquetar o excluir con justificación).


      Añades desviación estándar, IQR y regla de outliers; decides qué hacer con
      un día “Black Friday” en tus datos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Funciones
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): dispersion percentiles L10"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Dispersión, percentiles y outliers" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/src/percentiles.ts + salida/dispersion.md
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

      `git commit -am "feat(m04): dispersion percentiles L10"`
    comandoEsperado:
      - 'git commit -am "feat(m04): dispersion percentiles L10"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m04): dispersion percentiles L10"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Extender el pipeline con σ, p25/p75 y documentar una decisión sobre
          outliers (mantener, etiquetar o excluir con justificación).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Informe corto
    xp: 10
    cuerpo: '`salida/dispersion.md`: rango, σ, IQR, lista de fechas outlier (si hay).'
  - id: s7
    tipo: explicacion
    titulo: 3. Decisión de negocio
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
