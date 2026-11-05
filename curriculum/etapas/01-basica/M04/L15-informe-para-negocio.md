---
id: L15
materia: M04
orden: 15
titulo: Informe para negocio (informe.md)
horas: 5
semana: 4
lectura: Relee objetivos M04 y M22 (emprendimiento) en el plan
evidencia: projects/m04-stats/informe.md completo
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Integras simulaciones, descriptivos, gráfico e inferencia en un informe de
      una página que un dueño de negocio pueda leer — **proyecto** de la
      materia.


      **Objetivo de esta lección:** Redactar `informe.md` con pregunta, datos,
      método, resultado, limitaciones y recomendación accionable.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Borrador
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m04-stats/informe.md
      git commit -m "docs(m04): informe de negocio L15"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Edición para audiencia
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m04-stats/informe.md
      git commit -m "docs(m04): informe de negocio L15"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Informe para negocio (informe.md)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`informe.md` tiene todas las secciones obligatorias.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Informe para negocio
          (informe.md)
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

      `git add projects/m04-stats/informe.md`
    comandoEsperado:
      - git add projects/m04-stats/informe.md
      - 'git commit -m "docs(m04): informe de negocio L15"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git add projects/m04-stats/informe.md'
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
          Redactar `informe.md` con pregunta, datos, método, resultado,
          limitaciones y recomendación accionable.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Revisión cruzada
    xp: 10
    cuerpo: >-
      Pide a alguien (o simula con checklist): ¿entendió la recomendación sin
      ver el código?
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`informe.md` tiene todas las secciones obligatorias.'
      - Recomendación accionable presente.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Informe para negocio (`informe.md`)

**~5 h · Semana 4**

Integras simulaciones, descriptivos, gráfico e inferencia en un informe de una página que un dueño de negocio pueda leer — **proyecto** de la materia.

## Objetivo

Redactar `informe.md` con pregunta, datos, método, resultado, limitaciones y recomendación accionable.

## Estructura obligatoria

Crea `projects/m04-stats/informe.md`:

```markdown
# Informe — [título corto]

## Pregunta de negocio
-

## Datos
- Fuente:
- Periodo:
- n / columnas clave:

## Método
- Descriptivos:
- Visualización:
- Inferencia (IC / hipótesis):

## Resultados
(bullets con números, sin jerga innecesaria)

## Limitaciones
-

## Recomendación
(una acción concreta; qué medir después)

## Anexo técnico (opcional)
Enlaces a scripts en src/
```

## Pasos

### 1. Borrador (60 min)

Copia cifras desde `salida/` y notas L09–L14. No inventes números.

### 2. Edición para audiencia (50 min)

Lee en voz alta. Elimina “rechazamos H0” sin traducción. Añade una frase sobre correlación ≠ causalidad si usaste correlación.

### 3. Revisión cruzada (30 min)

Pide a alguien (o simula con checklist): ¿entendió la recomendación sin ver el código?

### 4. Commit

```bash
git add projects/m04-stats/informe.md
git commit -m "docs(m04): informe de negocio L15"
```

## Hecho cuando

1. `informe.md` tiene todas las secciones obligatorias.
2. Recomendación accionable presente.
3. Commit.

## Siguiente

[L16 — Cierre M04: evidencias y dominio](L16-cierre-m04-evidencias.md)
