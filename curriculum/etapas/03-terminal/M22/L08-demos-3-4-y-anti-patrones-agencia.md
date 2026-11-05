---
id: L08
materia: M22
orden: 8
titulo: Demos 3–4 y anti-patrones agencia
horas: 5
semana: 2
lectura: Lean — perseverancia vs pivot
evidencia: projects/m22-bektor/demos/demo-03.md + demo-04.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El pivote Bektor→Vitrina es decisión de negocio; documentar qué **no**
      vendes.


      Conceptos que debes poder explicar al cerrar:


      - Perseverancia.

      - Pivot.

      - Scope comercial.

      - Trial vs proyecto.


      **Objetivo de esta lección:** Completar dos demos más; registrar tentación
      de vender ‘proyecto a medida’ y rechazarla por escrito.


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
      git commit -m "docs(m22): l08 demos-3-4-y-anti-patrones-agencia"
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
      git commit -m "docs(m22): l08 demos-3-4-y-anti-patrones-agencia"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Demos 3–4 y anti-patrones agencia», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Demos 3–4 y
          anti-patrones agencia
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
          Completar dos demos más; registrar tentación de vender ‘proyecto a
          medida’ y rechazarla por escrito.
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
    cuerpo: Actualiza `projects/m22-bektor/README.md` con contador demos (4/10).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m22-bektor/demos/demo-03.md +
        demo-04.md`.
      - 2 demos.
      - pivote borrador.
      - README contador.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — Demos 3–4 y anti-patrones agencia

**~5 h · Semana 2**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-03.md + demo-04.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Completar dos demos más; registrar tentación de vender ‘proyecto a medida’ y rechazarla por escrito.

## Por qué empieza así

El pivote Bektor→Vitrina es decisión de negocio; documentar qué **no** vendes.

Conceptos que debes poder explicar al cerrar:

- Perseverancia.
- Pivot.
- Scope comercial.
- Trial vs proyecto.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — perseverancia vs pivot_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Crea demo-03 y demo-04. Escribe `projects/m22-bektor/pivote-bektor-vitrina.md` borrador: qué dejaste de vender (lista) y por qué SaaS gana.

### 3. Laboratorio principal (90–120 min)

Actualiza `projects/m22-bektor/README.md` con contador demos (4/10).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l08 demos-3-4-y-anti-patrones-agencia"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — perseverancia vs pivot | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-03.md + demo-04.md`.
2. 2 demos.
3. pivote borrador.
4. README contador.
5. Commit `docs(m22): l08 …` en el historial.

## Errores comunes

- Aceptar proyecto custom sin ADR comercial.
- Demos sin fecha.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L09 — Tres hipótesis de precio o sub-vertical](L09-tres-hipotesis-de-precio-o-sub-vertical.md)
