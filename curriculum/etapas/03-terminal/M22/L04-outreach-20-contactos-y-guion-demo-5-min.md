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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin lista no hay 10 demos; sin guion las conversaciones divagan.


      Conceptos que debes poder explicar al cerrar:


      - Outreach.

      - Staging URL.

      - Demo script.

      - CTA trial 14 días.


      **Objetivo de esta lección:** Armar lista de 20 negocios ICP y guion de
      demo staging: login → pedido → WhatsApp → cierre trial.


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
      git commit -m "docs(m22): l04 outreach-20-contactos-y-guion-demo-5-min"
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
      git commit -m "docs(m22): l04 outreach-20-contactos-y-guion-demo-5-min"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Outreach 20 contactos y guion demo 5 min», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Outreach 20 contactos y
          guion demo 5 min
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
          Armar lista de 20 negocios ICP y guion de demo staging: login → pedido
          → WhatsApp → cierre trial.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
