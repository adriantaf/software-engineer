---
id: L09
materia: M23
orden: 9
titulo: Rúbrica de evaluación FAQ
horas: 5
semana: 3
lectura: Evaluación LLM — correcto/parcial/incorrecto/alucinación
evidencia: projects/m23-ia/llm-eval/rubrica.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Calidad medible habilita comparar prompt v1 vs v2 objetivamente.


      Conceptos que debes poder explicar al cerrar:


      - Rúbrica.

      - Anclas.

      - Alucinación.

      - Parcial aceptable.


      **Objetivo de esta lección:** Definir rúbrica con ejemplos anclados para
      calificar respuestas del asistente.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l09 r-brica-de-evaluaci-n-faq"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m23): l09 r-brica-de-evaluaci-n-faq"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Rúbrica de evaluación FAQ», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Rúbrica de evaluación
          FAQ
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

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      - git status
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
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
          Definir rúbrica con ejemplos anclados para calificar respuestas del
          asistente.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Laboratorio principal
    xp: 10
    cuerpo: Acuerda umbral (ej. ≥80% correcto+parcial aceptable) en el mismo archivo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/llm-eval/rubrica.md`.'
      - Rúbrica 4 niveles.
      - Ejemplos anclados.
      - Umbral numérico.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Rúbrica de evaluación FAQ

**~5 h · Semana 3**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/llm-eval/rubrica.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Definir rúbrica con ejemplos anclados para calificar respuestas del asistente.

## Por qué empieza así

Calidad medible habilita comparar prompt v1 vs v2 objetivamente.

Conceptos que debes poder explicar al cerrar:

- Rúbrica.
- Anclas.
- Alucinación.
- Parcial aceptable.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Evaluación LLM — correcto/parcial/incorrecto/alucinación_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/llm-eval`.

`projects/m23-ia/llm-eval/rubrica.md`: 4 categorías, definición, ejemplo bueno/malo por categoría.

### 3. Laboratorio principal (90–120 min)

Acuerda umbral (ej. ≥80% correcto+parcial aceptable) en el mismo archivo.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l09 r-brica-de-evaluaci-n-faq"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Evaluación LLM — correcto/parcial/incorrecto/alucinación | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/llm-eval/rubrica.md`.
2. Rúbrica 4 niveles.
3. Ejemplos anclados.
4. Umbral numérico.
5. Commit `docs(m23): l09 …` en el historial.

## Errores comunes

- ‘Se ve bien’.
- Sin definir alucinación.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Correr evaluación v1 sobre gold set](L10-correr-evaluacion-v1-sobre-gold-set.md)
