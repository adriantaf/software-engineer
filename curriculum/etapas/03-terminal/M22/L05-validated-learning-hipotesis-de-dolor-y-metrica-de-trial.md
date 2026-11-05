---
id: L05
materia: M22
orden: 5
titulo: Validated learning — hipótesis de dolor y métrica de trial
horas: 5
semana: 2
lectura: Lean — validated learning
evidencia: projects/m22-bektor/hipotesis-trial.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Formular hipótesis: dolor, solución mínima, métrica de éxito
      del trial (≥1 pedido en 7 días).


      M22 mide aprendizaje, no vanity; esta métrica alinea con M23.


      Conceptos que debes poder explicar al cerrar:


      - Hipótesis falsable.

      - Métrica activación.

      - Baseline.

      - Criterio de pivot.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l05 validated-learning-hip-tesis-de-dolor-y"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Validated learning — hipótesis de dolor y métrica de trial"
      como hecha, ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/hipotesis-trial.md
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
          Formular hipótesis: dolor, solución mínima, métrica de éxito del trial
          (≥1 pedido en 7 días).
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


      Crea `projects/m22-bektor/hipotesis-trial.md` con plantilla: Creemos que…
      Mediremos… Éxito si… Fracaso si…
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Enlaza a `projects/m22-bektor/metricas-trials.md` (crear encabezados de
      columnas: negocio, trial iniciado, activación 7d, notas).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/hipotesis-trial.md`.'
      - hipotesis-trial.md.
      - metricas-trials.md esqueleto.
      - Métrica activación definida.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Validated learning — hipótesis de dolor y métrica de trial

**~5 h · Semana 2**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/hipotesis-trial.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Formular hipótesis: dolor, solución mínima, métrica de éxito del trial (≥1 pedido en 7 días).

## Por qué empieza así

M22 mide aprendizaje, no vanity; esta métrica alinea con M23.

Conceptos que debes poder explicar al cerrar:

- Hipótesis falsable.
- Métrica activación.
- Baseline.
- Criterio de pivot.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — validated learning_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Crea `projects/m22-bektor/hipotesis-trial.md` con plantilla: Creemos que… Mediremos… Éxito si… Fracaso si…

### 3. Laboratorio principal (90–120 min)

Enlaza a `projects/m22-bektor/metricas-trials.md` (crear encabezados de columnas: negocio, trial iniciado, activación 7d, notas).

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l05 validated-learning-hip-tesis-de-dolor-y"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — validated learning | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/hipotesis-trial.md`.
2. hipotesis-trial.md.
3. metricas-trials.md esqueleto.
4. Métrica activación definida.
5. Commit `docs(m22): l05 …` en el historial.

## Errores comunes

- Métrica ‘likes’.
- Hipótesis no falsable.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Demo 1 — conversación real documentada](L06-demo-1-conversacion-real-documentada.md)
