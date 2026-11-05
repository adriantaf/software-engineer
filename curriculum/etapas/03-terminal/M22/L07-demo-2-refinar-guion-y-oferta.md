---
id: L07
materia: M22
orden: 7
titulo: Demo 2 — refinar guion y oferta
horas: 5
semana: 2
lectura: Lean — pivot del mensaje
evidencia: projects/m22-bektor/demos/demo-02.md + oferta-saas.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Segunda conversación; actualizar guion u oferta según
      objeción #1 observada.


      Build-measure-learn en ventas: el mensaje es código que refactorizas.


      Conceptos que debes poder explicar al cerrar:


      - Objeción Excel/WhatsApp.

      - Iteración mensaje.

      - Evidencia en git.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l07 demo-2-refinar-guion-y-oferta"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Demo 2 — refinar guion y oferta" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/demos/demo-02.md + oferta-saas.md
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
          Segunda conversación; actualizar guion u oferta según objeción #1
          observada.
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
      Confirma rutas bajo `projects/m22-bektor/demos`.


      Documenta `projects/m22-bektor/demos/demo-02.md`. Tras la call, edita
      **una** sección de `guion-demo-5min.md` o `oferta-saas.md` con cambio
      justificado (commit separado).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: 'Nota en bitácora: ¿la objeción es precio, tiempo o confianza?'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m22-bektor/demos/demo-02.md +
        oferta-saas.md`.
      - demo-02.md.
      - Cambio guion/oferta commiteado.
      - Objeción clasificada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Demo 2 — refinar guion y oferta

**~5 h · Semana 2**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/demos/demo-02.md + oferta-saas.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Segunda conversación; actualizar guion u oferta según objeción #1 observada.

## Por qué empieza así

Build-measure-learn en ventas: el mensaje es código que refactorizas.

Conceptos que debes poder explicar al cerrar:

- Objeción Excel/WhatsApp.
- Iteración mensaje.
- Evidencia en git.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — pivot del mensaje_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor/demos`.

Documenta `projects/m22-bektor/demos/demo-02.md`. Tras la call, edita **una** sección de `guion-demo-5min.md` o `oferta-saas.md` con cambio justificado (commit separado).

### 3. Laboratorio principal (90–120 min)

Nota en bitácora: ¿la objeción es precio, tiempo o confianza?

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l07 demo-2-refinar-guion-y-oferta"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — pivot del mensaje | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/demos/demo-02.md + oferta-saas.md`.
2. demo-02.md.
3. Cambio guion/oferta commiteado.
4. Objeción clasificada.

## Errores comunes

- Ignorar feedback.
- 10 demos idénticas sin aprendizaje.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L08 — Demos 3–4 y anti-patrones agencia](L08-demos-3-4-y-anti-patrones-agencia.md)
