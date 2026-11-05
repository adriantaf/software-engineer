---
id: L09
materia: M22
orden: 9
titulo: Tres hipótesis de precio o sub-vertical
horas: 5
semana: 3
lectura: Lean — experimentación
evidencia: projects/m22-bektor/pricing-experimentos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Semana 3 exige rigor: precio no es número mágico, es hipótesis.


      Conceptos que debes poder explicar al cerrar:


      - Precio.

      - Elasticidad (cualitativa).

      - Free tier.

      - Límites técnicos.


      **Objetivo de esta lección:** Documentar tres experimentos de pricing o
      empaquetado y cómo los invalidarías con datos de demos.


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
      git commit -m "docs(m22): l09 tres-hip-tesis-de-precio-o-sub-vertical"
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
      git commit -m "docs(m22): l09 tres-hip-tesis-de-precio-o-sub-vertical"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tres hipótesis de precio o sub-vertical», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tres hipótesis de
          precio o sub-vertical
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
          Documentar tres experimentos de pricing o empaquetado y cómo los
          invalidarías con datos de demos.
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
    cuerpo: >-
      Compara alternativas: libreta, Calendly genérico, WhatsApp solo — tabla 1
      página.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/pricing-experimentos.md`.'
      - 3 hipótesis.
      - Tabla alternativas.
      - Señales éxito/fracaso.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Tres hipótesis de precio o sub-vertical

**~5 h · Semana 3**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pricing-experimentos.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Documentar tres experimentos de pricing o empaquetado y cómo los invalidarías con datos de demos.

## Por qué empieza así

Semana 3 exige rigor: precio no es número mágico, es hipótesis.

Conceptos que debes poder explicar al cerrar:

- Precio.
- Elasticidad (cualitativa).
- Free tier.
- Límites técnicos.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — experimentación_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

`projects/m22-bektor/pricing-experimentos.md`: 3 hipótesis (ej. Pro $499 vs $699 MXN; límite pedidos/mes). Para cada una: señal de éxito/fracaso en conversaciones.

### 3. Laboratorio principal (90–120 min)

Compara alternativas: libreta, Calendly genérico, WhatsApp solo — tabla 1 página.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l09 tres-hip-tesis-de-precio-o-sub-vertical"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — experimentación | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pricing-experimentos.md`.
2. 3 hipótesis.
3. Tabla alternativas.
4. Señales éxito/fracaso.
5. Commit `docs(m22): l09 …` en el historial.

## Errores comunes

- Precio sin justificación.
- Copiar USD sin MXN.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L10 — Demos 5–6 — escuchar precio en voz alta](L10-demos-5-6-escuchar-precio-en-voz-alta.md)
