---
id: L11
materia: M04
orden: 11
titulo: Visualización e histogramas para no técnicos
horas: 5
semana: 3
lectura: OpenStax gráficos · Walpole gráficos descriptivos
evidencia: >-
  projects/m04-stats/salida/histograma-pedidos.md (+ png/svg opcional) +
  notas/explicar-histograma.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Construyes un histograma de pedidos (script, Python, Excel o herramienta
      que prefieras) y escribes la explicación que darías en una reunión con
      stakeholders.


      **Objetivo de esta lección:** Cumplir el criterio de dominio “explicas un
      histograma a un no técnico” con evidencia escrita.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Histograma
    xp: 10
    cuerpo: >-
      Genera bins sobre `pedidos` (ej. 10 bins). Guarda: - Imagen en
      `salida/histograma-pedidos.png` **o** - Histograma ASCII/tabla en
      `salida/histograma-pedidos.md`
  - id: s3
    tipo: ejemplo
    titulo: Guion de 2 minutos
    xp: 10
    cuerpo: '`notas/explicar-histograma.md`: ```markdown # Cómo explico este histograma'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Visualización e histogramas para no técnicos», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Histograma guardado en `salida/`.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Visualización e
          histogramas para no téc…
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
          Cumplir el criterio de dominio “explicas un histograma a un no
          técnico” con evidencia escrita.
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
      - Histograma guardado en `salida/`.
      - Guion de explicación completo.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L11 — Visualización e histogramas para no técnicos

**~5 h · Semana 3**

Construyes un histograma de pedidos (script, Python, Excel o herramienta que prefieras) y escribes la explicación que darías en una reunión con stakeholders.

## Objetivo

Cumplir el criterio de dominio “explicas un histograma a un no técnico” con evidencia escrita.

## Pasos

### 1. Histograma (70 min)

Genera bins sobre `pedidos` (ej. 10 bins). Guarda:

- Imagen en `salida/histograma-pedidos.png` **o**
- Histograma ASCII/tabla en `salida/histograma-pedidos.md`

### 2. Guion de 2 minutos (40 min)

`notas/explicar-histograma.md`:

```markdown
# Cómo explico este histograma

## Qué muestra (sin jerga)
-

## Qué NO muestra
-

## Pregunta que abre al negocio
-
```

### 3. Lectura (60 min)

Buenas prácticas de gráficos (eje Y, bins, no truncar ejes sin decirlo).

### 4. Commit

```bash
git commit -am "docs(m04): histograma y guion L11"
```

## Hecho cuando

1. Histograma guardado en `salida/`.
2. Guion de explicación completo.
3. Commit.

## Siguiente

[L12 — Correlación, muestreo y sesgo](L12-correlacion-muestreo-y-sesgo.md)
