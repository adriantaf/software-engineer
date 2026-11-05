---
id: L04
materia: M22
orden: 4
titulo: Outreach 20 contactos y guion demo 5 min
horas: 5
semana: 1
lectura: Lean — experimento de contacto
evidencia: projects/m22-bektor/outreach-lista.md + guion-demo-5min.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Armar lista de 20 negocios ICP y guion de demo staging:
      login → pedido → WhatsApp → cierre trial.


      Sin lista no hay 10 demos; sin guion las conversaciones divagan.


      Conceptos que debes poder explicar al cerrar:


      - Outreach.

      - Staging URL.

      - Demo script.

      - CTA trial 14 días.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l04 outreach-20-contactos-y-guion-demo-5-min"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Outreach 20 contactos y guion demo 5 min" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/outreach-lista.md + guion-demo-5min.md
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
          Armar lista de 20 negocios ICP y guion de demo staging: login → pedido
          → WhatsApp → cierre trial.
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


      `projects/m22-bektor/outreach-lista.md`: 20 filas (nombre, contacto, por
      qué encajan).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      `projects/m22-bektor/guion-demo-5min.md`: pasos cronometrados sobre
      **staging/prod M19**, nunca localhost.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m22-bektor/outreach-lista.md +
        guion-demo-5min.md`.
      - 20 contactos.
      - Guion 5 min.
      - pricing.md borrador.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — Outreach 20 contactos y guion demo 5 min

**~5 h · Semana 1**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/outreach-lista.md + guion-demo-5min.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Armar lista de 20 negocios ICP y guion de demo staging: login → pedido → WhatsApp → cierre trial.

## Por qué empieza así

Sin lista no hay 10 demos; sin guion las conversaciones divagan.

Conceptos que debes poder explicar al cerrar:

- Outreach.
- Staging URL.
- Demo script.
- CTA trial 14 días.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — experimento de contacto_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

`projects/m22-bektor/outreach-lista.md`: 20 filas (nombre, contacto, por qué encajan).

### 3. Laboratorio principal (90–120 min)

`projects/m22-bektor/guion-demo-5min.md`: pasos cronometrados sobre **staging/prod M19**, nunca localhost.

### 4. Endurece el entregable (40–60 min)

Borrador `projects/m22-bektor/pricing.md`: planes Free/Pro MXN + límites (calendarios, pedidos/mes).

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l04 outreach-20-contactos-y-guion-demo-5-min"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — experimento de contacto | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/outreach-lista.md + guion-demo-5min.md`.
2. 20 contactos.
3. Guion 5 min.
4. pricing.md borrador.
5. Commit `docs(m22): l04 …` en el historial.

## Errores comunes

- Demo localhost.
- Lista sin contacto real.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Validated learning — hipótesis de dolor y métrica de trial](L05-validated-learning-hipotesis-de-dolor-y-metrica-de-trial.md)
