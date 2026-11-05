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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Construyes un IC del 95% para la media de pedidos (fórmula con z o t según
      tu lectura) y practicas la frase correcta de interpretación.


      **Objetivo de esta lección:** Calcular IC para μ con tus datos y explicar
      qué significa “95% de confianza” **sin** decir que μ está dentro con
      probabilidad 95%.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Fórmula en nota
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): intervalo confianza media L13"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Código
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m04): intervalo confianza media L13"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Intervalos de confianza interpretados», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: IC calculado sobre tu CSV.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Intervalos de confianza
          interpretados
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

      `git commit -am "feat(m04): intervalo confianza media L13"`
    comandoEsperado:
      - 'git commit -am "feat(m04): intervalo confianza media L13"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m04): intervalo confianza media L13"'
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
          Calcular IC para μ con tus datos y explicar qué significa “95% de
          confianza” sin decir que μ está dentro con probabilidad 95%.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Producto
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
