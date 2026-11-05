---
id: L20
materia: M22
orden: 20
titulo: Pivote Bektor → Vitrina — narrativa completa
horas: 5
semana: 5
lectura: Lean — pivot documentado
evidencia: projects/m22-bektor/pivote-bektor-vitrina.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Proyecto de materia: decisión de negocio trazable, no rebranding
      cosmetico.


      Conceptos que debes poder explicar al cerrar:


      - Pivot.

      - Evidencia.

      - SaaS.

      - Anti-agencia.


      **Objetivo de esta lección:** Finalizar narrativa de pivote: qué vendía
      Bektor, qué vendes ahora, evidencia de conversaciones.


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
      git commit -m "docs(m22): l20 pivote-bektor-vitrina-narrativa-compl"
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
      git commit -m "docs(m22): l20 pivote-bektor-vitrina-narrativa-compl"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pivote Bektor → Vitrina — narrativa completa», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pivote Bektor → Vitrina
          — narrativa com…
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
          Finalizar narrativa de pivote: qué vendía Bektor, qué vendes ahora,
          evidencia de conversaciones.
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
      Actualiza `projects/m22-bektor/README.md` con enlaces a oferta, pricing,
      pivote, métricas.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/pivote-bektor-vitrina.md`.'
      - Pivote completo.
      - README actualizado.
      - Evidencia demos citada.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L20 — Pivote Bektor → Vitrina — narrativa completa

**~5 h · Semana 5**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/pivote-bektor-vitrina.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Finalizar narrativa de pivote: qué vendía Bektor, qué vendes ahora, evidencia de conversaciones.

## Por qué empieza así

Proyecto de materia: decisión de negocio trazable, no rebranding cosmetico.

Conceptos que debes poder explicar al cerrar:

- Pivot.
- Evidencia.
- SaaS.
- Anti-agencia.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — pivot documentado_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Completa `projects/m22-bektor/pivote-bektor-vitrina.md` (≥2 páginas markdown): timeline, métricas aprendizaje, quotes anonimizados de demos.

### 3. Laboratorio principal (90–120 min)

Actualiza `projects/m22-bektor/README.md` con enlaces a oferta, pricing, pivote, métricas.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l20 pivote-bektor-vitrina-narrativa-compl"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — pivot documentado | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/pivote-bektor-vitrina.md`.
2. Pivote completo.
3. README actualizado.
4. Evidencia demos citada.
5. Commit `docs(m22): l20 …` en el historial.

## Errores comunes

- Pivot sin fechas.
- Volver a listar servicios agencia.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L21 — Pricing final para M26 y trial operativo](L21-pricing-final-para-m26-y-trial-operativo.md)
