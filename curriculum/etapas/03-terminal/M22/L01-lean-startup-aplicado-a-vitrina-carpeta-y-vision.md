---
id: L01
materia: M22
orden: 1
titulo: Lean Startup aplicado a Vitrina — carpeta y visión
horas: 5
semana: 1
lectura: 'El método Lean Startup — visión, start, build-measure-learn'
evidencia: projects/m22-bektor/demos + bitacora-m22.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      M22 vende **suscripción** al producto que construiste; Bektor como agencia
      no es el modelo del plan.


      Conceptos que debes poder explicar al cerrar:


      - Visión vs estrategia.

      - Build-measure-learn.

      - SaaS vertical.

      - Anti-patrón agencia.


      **Objetivo de esta lección:** Crear estructura comercial, leer
      visión/start/BML y escribir hipótesis de negocio SaaS (no agencia).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m22-bektor/demos
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Prepara evidencia y carpetas
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m22-bektor/demos
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Lean Startup aplicado a Vitrina — carpeta y visión», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Lean Startup aplicado a
          Vitrina — carpe…
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

      `mkdir -p projects/m22-bektor/demos`
    comandoEsperado:
      - mkdir -p projects/m22-bektor/demos
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m22-bektor/demos'
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
          Crear estructura comercial, leer visión/start/BML y escribir hipótesis
          de negocio SaaS (no agencia).
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
    cuerpo: Lista 3 supuestos que **matarían** el negocio si fueran falsos.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/demos + bitacora-m22.md`.'
      - demos/ existe.
      - bitacora con BML.
      - 3 supuestos críticos.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L01 — Lean Startup aplicado a Vitrina — carpeta y visión

**~5 h · Semana 1**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos + bitacora-m22.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Crear estructura comercial, leer visión/start/BML y escribir hipótesis de negocio SaaS (no agencia).

## Por qué empieza así

M22 vende **suscripción** al producto que construiste; Bektor como agencia no es el modelo del plan.

Conceptos que debes poder explicar al cerrar:

- Visión vs estrategia.
- Build-measure-learn.
- SaaS vertical.
- Anti-patrón agencia.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _El método Lean Startup — visión, start, build-measure-learn_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

```bash
mkdir -p projects/m22-bektor/demos
```

### 3. Laboratorio principal (90–120 min)

Lista 3 supuestos que **matarían** el negocio si fueran falsos.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l01 lean-startup-aplicado-a-vitrina-carpe"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | El método Lean Startup — visión, start, build-measure-learn | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos + bitacora-m22.md`.
2. demos/ existe.
3. bitacora con BML.
4. 3 supuestos críticos.
5. Commit `docs(m22): l01 …` en el historial.

## Errores comunes

- Volver a vender ‘páginas web’.
- Leer sin escribir acción.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L02 — ICP único — sub-vertical fijado por escrito](L02-icp-unico-sub-vertical-fijado-por-escrito.md)
