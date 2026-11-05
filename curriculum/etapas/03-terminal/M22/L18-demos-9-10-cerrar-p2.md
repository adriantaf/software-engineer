---
id: L18
materia: M22
orden: 18
titulo: Demos 9–10 — cerrar P2
horas: 5
semana: 5
lectura: Lean — validación comercial
evidencia: projects/m22-bektor/demos/demo-09.md + demo-10.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2 exige 10 fichas; copy-paste invalida criterio dominio.


      Conceptos que debes poder explicar al cerrar:


      - Índice demos.

      - Aprendizaje único.

      - Trial pedido.


      **Objetivo de esta lección:** Completar demos 9 y 10 con aprendizajes
      **distintos**; índice en demos/README.md.


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
      git commit -m "docs(m22): l18 demos-9-10-cerrar-p2"
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
      git commit -m "docs(m22): l18 demos-9-10-cerrar-p2"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Demos 9–10 — cerrar P2», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Demos 9–10 — cerrar P2
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
          Completar demos 9 y 10 con aprendizajes distintos; índice en
          demos/README.md.
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
    cuerpo: Verifica contador 10/10 en README raíz.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m22-bektor/demos/demo-09.md +
        demo-10.md`.
      - 10 demos totales.
      - README índice.
      - Aprendizajes distintos.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Demos 9–10 — cerrar P2

**~5 h · Semana 5**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-09.md + demo-10.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Completar demos 9 y 10 con aprendizajes **distintos**; índice en demos/README.md.

## Por qué empieza así

P2 exige 10 fichas; copy-paste invalida criterio dominio.

Conceptos que debes poder explicar al cerrar:

- Índice demos.
- Aprendizaje único.
- Trial pedido.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — validación comercial_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Crea demo-09 y demo-10. `projects/m22-bektor/demos/README.md` tabla 10 filas con enlace y aprendizaje one-liner.

### 3. Laboratorio principal (90–120 min)

Verifica contador 10/10 en README raíz.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l18 demos-9-10-cerrar-p2"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — validación comercial | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-09.md + demo-10.md`.
2. 10 demos totales.
3. README índice.
4. Aprendizajes distintos.
5. Commit `docs(m22): l18 …` en el historial.

## Errores comunes

- Duplicar aprendizaje.
- Demo sin producto mostrado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L19 — Landing de precios y enlace en evidencia](L19-landing-de-precios-y-enlace-en-evidencia.md)
