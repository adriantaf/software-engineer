---
id: L10
materia: M22
orden: 10
titulo: Demos 5–6 — escuchar precio en voz alta
horas: 5
semana: 3
lectura: Lean — experimentos de mercado
evidencia: projects/m22-bektor/demos/demo-05.md + demo-06.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M26 integrará Stripe; hoy practicas defensa del valor en MXN.


      Conceptos que debes poder explicar al cerrar:


      - Anclaje precio.

      - Free/Pro.

      - Objeción precio.

      - Trial como reduce riesgo.


      **Objetivo de esta lección:** Dos demos donde **dices el precio** o rango
      Pro sin tartamudear y registras reacción.


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
      git commit -m "docs(m22): l10 demos-5-6-escuchar-precio-en-voz-alta"
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
      git commit -m "docs(m22): l10 demos-5-6-escuchar-precio-en-voz-alta"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Demos 5–6 — escuchar precio en voz alta», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Demos 5–6 — escuchar
          precio en voz alta
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
          Dos demos donde dices el precio o rango Pro sin tartamudear y
          registras reacción.
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
      Ajusta `projects/m22-bektor/pricing.md` con límites técnicos reales del
      producto (no prometer IA ilimitada si M23 costea tokens).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m22-bektor/demos/demo-05.md +
        demo-06.md`.
      - 2 demos con precio dicho.
      - pricing.md actualizado.
      - Reacción documentada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Demos 5–6 — escuchar precio en voz alta

**~5 h · Semana 3**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-05.md + demo-06.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Dos demos donde **dices el precio** o rango Pro sin tartamudear y registras reacción.

## Por qué empieza así

M26 integrará Stripe; hoy practicas defensa del valor en MXN.

Conceptos que debes poder explicar al cerrar:

- Anclaje precio.
- Free/Pro.
- Objeción precio.
- Trial como reduce riesgo.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — experimentos de mercado_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Documenta demos 5–6. En cada ficha campo **Reacción precio** (verbatim si puedes).

### 3. Laboratorio principal (90–120 min)

Ajusta `projects/m22-bektor/pricing.md` con límites técnicos reales del producto (no prometer IA ilimitada si M23 costea tokens).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l10 demos-5-6-escuchar-precio-en-voz-alta"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — experimentos de mercado | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-05.md + demo-06.md`.
2. 2 demos con precio dicho.
3. pricing.md actualizado.
4. Reacción documentada.
5. Commit `docs(m22): l10 …` en el historial.

## Errores comunes

- Evitar nombrar precio.
- Prometer features inexistentes.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Refinar ICP tras objeciones recurrentes](L11-refinar-icp-tras-objeciones-recurrentes.md)
