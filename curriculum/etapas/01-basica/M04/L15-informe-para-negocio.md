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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar `informe.md` con pregunta, datos, método,
      resultado, limitaciones y recomendación accionable.


      Integras simulaciones, descriptivos, gráfico e inferencia en un informe de
      una página que un dueño de negocio pueda leer — **proyecto** de la
      materia.
  - id: s2
    tipo: ejemplo
    titulo: 1. Borrador
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m04-stats/informe.md
      git commit -m "docs(m04): informe de negocio L15"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Informe para negocio (informe.md)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m04-stats/informe.md completo
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

      `git add projects/m04-stats/informe.md`
    comandoEsperado:
      - git add projects/m04-stats/informe.md
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m04-stats/informe.md'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Redactar `informe.md` con pregunta, datos, método, resultado,
          limitaciones y recomendación accionable.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Edición para audiencia
    xp: 10
    cuerpo: >-
      Lee en voz alta. Elimina “rechazamos H0” sin traducción. Añade una frase
      sobre correlación ≠ causalidad si usaste correlación.
  - id: s7
    tipo: explicacion
    titulo: 3. Revisión cruzada
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
