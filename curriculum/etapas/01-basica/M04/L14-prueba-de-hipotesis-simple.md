---
id: L14
materia: M04
orden: 14
titulo: Hipótesis simple con pregunta de negocio
horas: 5
semana: 4
lectura: Walpole cap. 9 (intro) · OpenStax Ch. 9 (idea)
evidencia: projects/m04-stats/notas/hipotesis-viernes.md + script o cálculo en src/
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Formulas H₀/H₁ para una pregunta tipo “¿los viernes hay más pedidos que
      otros días?” y concluyes con humildad — evidencia **P3**.


      **Objetivo de esta lección:** Completar P3: pregunta de negocio, método
      (aunque sea comparación de medias + IC o test que elijas), conclusión sin
      overclaim.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Pregunta y datos
    xp: 10
    cuerpo: >-
      En `notas/hipotesis-viernes.md`: ```markdown # ¿Los viernes hay más
      pedidos?
  - id: s3
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Hipótesis simple con pregunta de negocio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: Pregunta + H0/H1 + método + conclusión cautelosa en nota.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Hipótesis simple con
          pregunta de negocio
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s4
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? ““Rechazamos H0, entonces causamos más
      ventas los viernes.”"
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s5
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
          Completar P3: pregunta de negocio, método (aunque sea comparación de
          medias + IC o test que elijas), conclusión sin overclaim.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: >-
      ¿Debes hacer esto? “p-hacking: probar 10 cortes hasta que “salga
      significativo”."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Pregunta + H0/H1 + método + conclusión cautelosa en nota.
      - Cálculo reproducible (script o pasos pegados).
      - Listo para marcar P3 en la UI.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — Hipótesis simple con pregunta de negocio

**~5 h · Semana 4**

Formulas H₀/H₁ para una pregunta tipo “¿los viernes hay más pedidos que otros días?” y concluyes con humildad — evidencia **P3**.

## Objetivo

Completar P3: pregunta de negocio, método (aunque sea comparación de medias + IC o test que elijas), conclusión sin overclaim.

## Pasos

### 1. Pregunta y datos (30 min)

En `notas/hipotesis-viernes.md`:

```markdown
# ¿Los viernes hay más pedidos?

## Pregunta de negocio
-

## H0 y H1 (en lenguaje claro)
-

## Datos usados
-
```

Agrupa `pedidos` por día de semana (puede ser columna derivada en script).

### 2. Método simple (70 min)

Opciones válidas para este plan (elige una):

- Comparar media viernes vs resto con IC de la diferencia (aprox.)
- Test t de dos muestras con herramienta estadística
- Simulación de permutación (avanzado, opcional)

Documenta supuestos (independencia, tamaño n).

### 3. Conclusión (40 min)

Sección **Resultado** y **Limitaciones** (días festivos, una sola tienda, etc.).

### 4. Lectura (90 min)

Walpole cap. 9 lectura ligera: errores tipo I/II en una frase cada uno.

### 5. Commit

```bash
git commit -am "docs(m04): hipotesis viernes P3 L14"
```

## Hecho cuando

1. Pregunta + H0/H1 + método + conclusión cautelosa en nota.
2. Cálculo reproducible (script o pasos pegados).
3. Listo para marcar **P3** en la UI.
4. Commit.

## Errores comunes

- “Rechazamos H0, entonces causamos más ventas los viernes.”
- p-hacking: probar 10 cortes hasta que “salga significativo”.

## Siguiente

[L15 — Informe para negocio (`informe.md`)](L15-informe-para-negocio.md)
