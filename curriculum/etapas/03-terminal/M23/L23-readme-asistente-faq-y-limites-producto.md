---
id: L23
materia: M23
orden: 23
titulo: README asistente FAQ y límites producto
horas: 5
semana: 6
lectura: Soporte y expectativas
evidencia: projects/m23-ia/faq-asistente/README.md final
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Proyecto P3 FAQ integrado; soporte necesita límites claros.


      Conceptos que debes poder explicar al cerrar:


      - Scope.

      - No-go.

      - Soporte.

      - Privacidad.


      **Objetivo de esta lección:** Finalizar README: qué hace, qué no hace,
      escalación humana, privacidad.


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
      git commit -m "docs(m23): l23 readme-asistente-faq-y-l-mites-producto"
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
      git commit -m "docs(m23): l23 readme-asistente-faq-y-l-mites-producto"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «README asistente FAQ y límites producto», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de README asistente FAQ y
          límites producto
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
          Finalizar README: qué hace, qué no hace, escalación humana,
          privacidad.
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
    cuerpo: Enlaza código/endpoint staging.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/faq-asistente/README.md final`.'
      - README final.
      - Limits claros.
      - Enlace código.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L23 — README asistente FAQ y límites producto

**~5 h · Semana 6**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/faq-asistente/README.md final`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Finalizar README: qué hace, qué no hace, escalación humana, privacidad.

## Por qué empieza así

Proyecto P3 FAQ integrado; soporte necesita límites claros.

Conceptos que debes poder explicar al cerrar:

- Scope.
- No-go.
- Soporte.
- Privacidad.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Soporte y expectativas_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/faq-asistente`.

README final en `projects/m23-ia/faq-asistente/`: secciones Scope, Limits, Privacy, Runbook incidencia.

### 3. Laboratorio principal (90–120 min)

Enlaza código/endpoint staging.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l23 readme-asistente-faq-y-l-mites-producto"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Soporte y expectativas | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/faq-asistente/README.md final`.
2. README final.
3. Limits claros.
4. Enlace código.
5. Commit `docs(m23): l23 …` en el historial.

## Errores comunes

- ‘IA mágica’.
- Sin escalación humana.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L24 — Cierre M23 — P1–P3, dominio y handoff M26](L24-cierre-m23-p1-p3-dominio-y-handoff-m26.md)
