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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cumplir el criterio de dominio “explicas un histograma a un
      no técnico” con evidencia escrita.


      Construyes un histograma de pedidos (script, Python, Excel o herramienta
      que prefieras) y escribes la explicación que darías en una reunión con
      stakeholders.
  - id: s2
    tipo: ejemplo
    titulo: 1. Histograma
    xp: 10
    cuerpo: |-
      Genera bins sobre `pedidos` (ej. 10 bins). Guarda:

      - Imagen en `salida/histograma-pedidos.png` **o**
      - Histograma ASCII/tabla en `salida/histograma-pedidos.md`
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Visualización e histogramas para no técnicos" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: >-
          projects/m04-stats/salida/histograma-pedidos.md (+ png/svg opcional) +
          notas/explicar-histograma.md
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
          Cumplir el criterio de dominio “explicas un histograma a un no
          técnico” con evidencia escrita.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Guion de 2 minutos
    xp: 10
    cuerpo: |-
      `notas/explicar-histograma.md`:

      ```markdown
      Cómo explico este histograma
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Histograma guardado en `salida/`.
      - Guion de explicación completo.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
