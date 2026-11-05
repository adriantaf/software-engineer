---
id: L03
materia: M22
orden: 3
titulo: Oferta SaaS en un párrafo
horas: 5
semana: 1
lectura: Lean — propuesta de valor
evidencia: projects/m22-bektor/oferta-saas.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Redactar oferta de **un producto** suscripción: problema del
      dueño → Vitrina → precio orientativo → trial.


      P1 es un párrafo defendible, no folleto de servicios Bektor.


      Conceptos que debes poder explicar al cerrar:


      - Problema.

      - Outcome.

      - Suscripción.

      - Siguiente paso trial.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l03 oferta-saas-en-un-p-rrafo"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Oferta SaaS en un párrafo" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m22-bektor/oferta-saas.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git add projects/ curriculum/etapas/03-terminal/ || git add projects/`
    comandoEsperado:
      - git add projects/ curriculum/etapas/03-terminal/ || git add projects/
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: git add projects/ curriculum/etapas/03-terminal/ || git add
      projects/
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Redactar oferta de **un producto** suscripción: problema del dueño →
          Vitrina → precio orientativo → trial.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Prepara evidencia y carpetas
    xp: 10
    cuerpo: >-
      Confirma rutas bajo `projects/m22-bektor`.


      Escribe `projects/m22-bektor/oferta-saas.md` con **un párrafo** (≤120
      palabras). Prohibido: ‘también hacemos logos/hosting’.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: Añade pitch **60 segundos** en bullet (≤6 líneas) al final del archivo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/oferta-saas.md`.'
      - Un párrafo oferta.
      - Pitch 60s.
      - Menciona suscripción MXN orientativa.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L03 — Oferta SaaS en un párrafo

**~5 h · Semana 1**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/oferta-saas.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Redactar oferta de **un producto** suscripción: problema del dueño → Vitrina → precio orientativo → trial.

## Por qué empieza así

P1 es un párrafo defendible, no folleto de servicios Bektor.

Conceptos que debes poder explicar al cerrar:

- Problema.
- Outcome.
- Suscripción.
- Siguiente paso trial.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — propuesta de valor_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Escribe `projects/m22-bektor/oferta-saas.md` con **un párrafo** (≤120 palabras). Prohibido: ‘también hacemos logos/hosting’.

### 3. Laboratorio principal (90–120 min)

Añade pitch **60 segundos** en bullet (≤6 líneas) al final del archivo.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l03 oferta-saas-en-un-p-rrafo"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — propuesta de valor | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/oferta-saas.md`.
2. Un párrafo oferta.
3. Pitch 60s.
4. Menciona suscripción MXN orientativa.
5. Commit `docs(m22): l03 …` en el historial.

## Errores comunes

- Lista de servicios agencia.
- Sin CTA trial.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L04 — Outreach 20 contactos y guion demo 5 min](L04-outreach-20-contactos-y-guion-demo-5-min.md)
