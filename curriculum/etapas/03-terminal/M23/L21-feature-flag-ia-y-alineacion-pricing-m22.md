---
id: L21
materia: M23
orden: 21
titulo: Feature flag IA y alineación pricing M22
horas: 5
semana: 6
lectura: Plan Pro limits + cost control
evidencia: projects/m23-ia/faq-asistente/plan-pro-ia.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Vender IA ilimitada en Pro sin costeo tumba margen.


      Conceptos que debes poder explicar al cerrar:


      - Feature flag.

      - Cuota mensual.

      - Upgrade.

      - Free sin RAG.


      **Objetivo de esta lección:** Documentar flag o límite IA por plan
      Free/Pro coherente con pricing M22.


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
      git commit -m "docs(m23): l21 feature-flag-ia-y-alineaci-n-pricing-m22"
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
      git commit -m "docs(m23): l21 feature-flag-ia-y-alineaci-n-pricing-m22"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Feature flag IA y alineación pricing M22», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Feature flag IA y
          alineación pricing M22
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
          Documentar flag o límite IA por plan Free/Pro coherente con pricing
          M22.
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
    cuerpo: Enlaza `projects/m22-bektor/pricing.md` con nota cruzada.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m23-ia/faq-asistente/plan-pro-ia.md`.'
      - plan-pro-ia.md.
      - Enlace pricing.
      - Cuotas numéricas.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L21 — Feature flag IA y alineación pricing M22

**~5 h · Semana 6**

Métricas e IA **por tenant**, sin mezclar datos. Hoy entregas **`projects/m23-ia/faq-asistente/plan-pro-ia.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M23.

## Objetivo

Documentar flag o límite IA por plan Free/Pro coherente con pricing M22.

## Por qué empieza así

Vender IA ilimitada en Pro sin costeo tumba margen.

Conceptos que debes poder explicar al cerrar:

- Feature flag.
- Cuota mensual.
- Upgrade.
- Free sin RAG.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee la fuente de hoy: _Plan Pro limits + cost control_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `projects/m23-ia/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m23-ia/faq-asistente`.

`projects/m23-ia/faq-asistente/plan-pro-ia.md`: tabla plan → cuotas tokens/preguntas.

### 3. Laboratorio principal (90–120 min)

Enlaza `projects/m22-bektor/pricing.md` con nota cruzada.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m23): l21 feature-flag-ia-y-alineaci-n-pricing-m22"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs API LLM elegida + política de datos | Plan Pro limits + cost control | [producto-saas · FAQ por tenant](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M23](../../../bibliografia.md#m23-ia-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m23-ia/faq-asistente/plan-pro-ia.md`.
2. plan-pro-ia.md.
3. Enlace pricing.
4. Cuotas numéricas.
5. Commit `docs(m23): l21 …` en el historial.

## Errores comunes

- IA gratis ilimitada.
- Flag sin default seguro.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L22 — Costo mensual estimado por tenant activo](L22-costo-mensual-estimado-por-tenant-activo.md)
