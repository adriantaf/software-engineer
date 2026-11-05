---
id: L08
materia: M24
orden: 8
titulo: 'Plan del spike — hipótesis, alcance y éxito'
horas: 5
semana: 2
lectura: Spike-driven development (notas ficha)
evidencia: projects/m24-emergentes/spike/hipotesis.md + spike/plan.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Elegir **un** candidato para semana 3; definir hipótesis
      medible, non-goals y criterio de éxito/fallo.


      Un spike sin timebox se convierte en feature a medias en producción.


      Conceptos que debes poder explicar al cerrar:


      - Hipótesis falsable

      - Timebox ≤1 semana

      - Demo script
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l08 plan-del-spike-hip-tesis-alcance-y-xito"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Plan del spike — hipótesis, alcance y éxito" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m24-emergentes/spike/hipotesis.md + spike/plan.md
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
          Elegir **un** candidato para semana 3; definir hipótesis medible,
          non-goals y criterio de éxito/fallo.
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
      Confirma rutas bajo `projects/m24-emergentes/spike`.


      `projects/m24-emergentes/spike/hipotesis.md`: “Si integramos X, entonces Y
      métrica mejora Z%” (aunque midas manualmente).
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
    xp: 10
    cuerpo: >-
      `projects/m24-emergentes/spike/plan.md`: entradas, salidas, comandos demo,
      **fuera de alcance** (lista explícita).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Existe el entregable: `projects/m24-emergentes/spike/hipotesis.md +
        spike/plan.md`.
      - hipotesis.md y plan.md.
      - Non-goals ≥3 ítems.
      - Candidato spike único.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Plan del spike — hipótesis, alcance y éxito

**~5 h · Semana 2**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/hipotesis.md + spike/plan.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Elegir **un** candidato para semana 3; definir hipótesis medible, non-goals y criterio de éxito/fallo.

## Por qué empieza así

Un spike sin timebox se convierte en feature a medias en producción.

Conceptos que debes poder explicar al cerrar:

- Hipótesis falsable
- Timebox ≤1 semana
- Demo script

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _Spike-driven development (notas ficha)_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes/spike`.

`projects/m24-emergentes/spike/hipotesis.md`: “Si integramos X, entonces Y métrica mejora Z%” (aunque midas manualmente).

### 3. Laboratorio principal (90–120 min)

`projects/m24-emergentes/spike/plan.md`: entradas, salidas, comandos demo, **fuera de alcance** (lista explícita).

### 4. Endurece el entregable (40–60 min)

Actualiza matriz con candidato **elegido para spike**.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l08 plan-del-spike-hip-tesis-alcance-y-xito"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | Spike-driven development (notas ficha) | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/hipotesis.md + spike/plan.md`.
2. hipotesis.md y plan.md.
3. Non-goals ≥3 ítems.
4. Candidato spike único.
5. Commit `docs(m24): l08 …` en el historial.

## Errores comunes

- Spike de tres tecnologías a la vez.
- Hipótesis ‘aprender X’ sin métrica.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L09 — Scaffold del spike y entorno aislado](L09-scaffold-del-spike-y-entorno-aislado.md)
