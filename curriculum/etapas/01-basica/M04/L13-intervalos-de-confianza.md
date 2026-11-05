---
id: L13
materia: M04
orden: 13
titulo: Intervalos de confianza interpretados
horas: 5
semana: 4
lectura: 'Walpole cap. 8 (IC media, intro) · OpenStax Ch. 8'
evidencia: projects/m04-stats/src/ic-media.ts + notas/ic-interpretacion.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Calcular IC para μ con tus datos y explicar qué significa
      “95% de confianza” **sin** decir que μ está dentro con probabilidad 95%.


      Construyes un IC del 95% para la media de pedidos (fórmula con z o t según
      tu lectura) y practicas la frase correcta de interpretación.
  - id: s2
    tipo: ejemplo
    titulo: 1. Fórmula en nota
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): intervalo confianza media L13"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Intervalos de confianza interpretados" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/src/ic-media.ts + notas/ic-interpretacion.md
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

      `git commit -am "feat(m04): intervalo confianza media L13"`
    comandoEsperado:
      - 'git commit -am "feat(m04): intervalo confianza media L13"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m04): intervalo confianza media L13"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Calcular IC para μ con tus datos y explicar qué significa “95% de
          confianza” **sin** decir que μ está dentro con probabilidad 95%.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Código
    xp: 10
    cuerpo: >-
      `src/ic-media.ts`: dado array de pedidos, devuelve `{ media, s, n, icBajo,
      icAlto }` usando z≈1.96 si n≥30.
  - id: s7
    tipo: explicacion
    titulo: 3. Producto
    xp: 10
    cuerpo: >-
      “Si el IC de conversión semanal es [4%, 9%], ¿lanzamos el feature?” —
      respuesta prudente.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - IC calculado sobre tu CSV.
      - Nota con interpretación correcta.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Intervalos de confianza interpretados

**~5 h · Semana 4**

Construyes un IC del 95% para la media de pedidos (fórmula con z o t según tu lectura) y practicas la frase correcta de interpretación.

## Objetivo

Calcular IC para μ con tus datos y explicar qué significa “95% de confianza” **sin** decir que μ está dentro con probabilidad 95%.

## Pasos

### 1. Fórmula en nota (30 min)

`notas/ic-interpretacion.md`: IC = x̄ ± z_{0.025} · (s/√n). Frase correcta vs incorrecta (dos ejemplos).

### 2. Código (60 min)

`src/ic-media.ts`: dado array de pedidos, devuelve `{ media, s, n, icBajo, icAlto }` usando z≈1.96 si n≥30.

### 3. Producto (40 min)

“Si el IC de conversión semanal es [4%, 9%], ¿lanzamos el feature?” — respuesta prudente.

### 4. Lectura (90 min)

Walpole cap. 8 (intervalo para la media).

### 5. Commit

```bash
git commit -am "feat(m04): intervalo confianza media L13"
```

## Hecho cuando

1. IC calculado sobre tu CSV.
2. Nota con interpretación correcta.
3. Commit.

## Siguiente

[L14 — Hipótesis simple con pregunta de negocio](L14-prueba-de-hipotesis-simple.md)
