---
id: L13
materia: M22
orden: 13
titulo: Métricas accionables — tablero de trials
horas: 5
semana: 4
lectura: Lean — medir lo que importa
evidencia: projects/m22-bektor/metricas-trials.md datos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Llenar tablero con trials iniciados, activación 7d y notas;
      rechazar vanity metrics.


      MRR ficticio sin pagos está prohibido en la ficha; mide activación y
      conversación.


      Conceptos que debes poder explicar al cerrar:


      - Trial iniciado.

      - Activación 7d.

      - Vanity vs accionable.

      - Seguimiento.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m22): l13 m-tricas-accionables-tablero-de-trials"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Métricas accionables — tablero de trials" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m22-bektor/metricas-trials.md datos
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
          Llenar tablero con trials iniciados, activación 7d y notas; rechazar
          vanity metrics.
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


      Actualiza `projects/m22-bektor/metricas-trials.md` con filas reales (≥6
      negocios contactados).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      Define fórmula activación en el archivo. Gráfico ASCII o tabla semanal
      suficiente.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m22-bektor/metricas-trials.md datos`.'
      - Tablero con datos.
      - Fórmula activación.
      - Sin MRR inventado.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Métricas accionables — tablero de trials

**~5 h · Semana 4**

Vendes suscripción SaaS, no agencia. Hoy entregas **`projects/m22-bektor/metricas-trials.md datos`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M22.

## Objetivo

Llenar tablero con trials iniciados, activación 7d y notas; rechazar vanity metrics.

## Por qué empieza así

MRR ficticio sin pagos está prohibido en la ficha; mide activación y conversación.

Conceptos que debes poder explicar al cerrar:

- Trial iniciado.
- Activación 7d.
- Vanity vs accionable.
- Seguimiento.

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee en *El método Lean Startup* (ed. ES) lo indicado: _Lean — medir lo que importa_.

Traduce a Vitrina: 5 bullets en `projects/m22-bektor/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing).

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m22-bektor`.

Actualiza `projects/m22-bektor/metricas-trials.md` con filas reales (≥6 negocios contactados).

### 3. Laboratorio principal (90–120 min)

Define fórmula activación en el archivo. Gráfico ASCII o tabla semanal suficiente.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m22): l13 m-tricas-accionables-tablero-de-trials"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *El método Lean Startup* — Eric Ries (ed. ES) | Lean — medir lo que importa | [producto-saas (Vitrina)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M22](../../../bibliografia.md#m22-emprendimiento) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m22-bektor/metricas-trials.md datos`.
2. Tablero con datos.
3. Fórmula activación.
4. Sin MRR inventado.
5. Commit `docs(m22): l13 …` en el historial.

## Errores comunes

- Contar WhatsApp enviado como trial.
- Métricas sin definición.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L14 — Demos 7–8 — seguimiento y lotes pequeños](L14-demos-7-8-seguimiento-y-lotes-pequenos.md)
