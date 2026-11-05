---
id: L14
materia: M22
orden: 14
titulo: Demos 7–8 — seguimiento y lotes pequeños
horas: 5
semana: 4
lectura: Lean — cohortes pequeñas
evidencia: projects/m22-bektor/demos/demo-07.md + demo-08.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dos demos con **seguimiento** a contactos previos; practicar
      lote de 5 contactos/semana.


      Semana 4 acelera aprendizaje acumulado, no spam.


      Conceptos que debes poder explicar al cerrar:


      - Follow-up.

      - Cadencia.

      - CRM mínimo.

      - Rechazo documentado.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l14 demos-7-8-seguimiento-y-lotes-peque-os"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Demos 7–8 — seguimiento y lotes pequeños" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/demos/demo-07.md + demo-08.md
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
          Dos demos con **seguimiento** a contactos previos; practicar lote de 5
          contactos/semana.
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
    cuerpo: |-
      Confirma rutas bajo `projects/m22-bektor/demos`.

      Demos 7–8. En bitácora: tabla follow-ups (fecha, contacto, resultado).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: 'Marca en outreach-lista estado: pendiente / demo / trial / no.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m22-bektor/demos/demo-07.md +
        demo-08.md`.
      - 2 demos.
      - Follow-ups registrados.
      - Estados en lista.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L14 — Demos 7–8 — seguimiento y lotes pequeños

**~5 h · Semana 4**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-07.md + demo-08.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Dos demos con **seguimiento** a contactos previos; practicar lote de 5 contactos/semana.

## Por qué empieza así

Semana 4 acelera aprendizaje acumulado, no spam.

Conceptos que debes poder explicar al cerrar:

- Follow-up.
- Cadencia.
- CRM mínimo.
- Rechazo documentado.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — cohortes pequeñas_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Demos 7–8. En bitácora: tabla follow-ups (fecha, contacto, resultado).

### 3. Laboratorio principal (90–120 min)

Marca en outreach-lista estado: pendiente / demo / trial / no.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l14 demos-7-8-seguimiento-y-lotes-peque-os"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — cohortes pequeñas | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-07.md + demo-08.md`.
2. 2 demos.
3. Follow-ups registrados.
4. Estados en lista.
5. Commit `docs(m22): l14 …` en el historial.

## Errores comunes

- Spam sin personalizar.
- No registrar rechazos.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L15 — Objeción #1 y cambio de producto o mensaje](L15-objecion-1-y-cambio-de-producto-o-mensaje.md)
