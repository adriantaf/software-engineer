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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un spike sin timebox se convierte en feature a medias en producción.


      Conceptos que debes poder explicar al cerrar:


      - Hipótesis falsable

      - Timebox ≤1 semana

      - Demo script


      **Objetivo de esta lección:** Elegir **un** candidato para semana 3;
      definir hipótesis medible, non-goals y criterio de éxito/fallo.


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
      git commit -m "docs(m24): l08 plan-del-spike-hip-tesis-alcance-y-xito"
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
      git commit -m "docs(m24): l08 plan-del-spike-hip-tesis-alcance-y-xito"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Plan del spike — hipótesis, alcance y éxito», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Plan del spike —
          hipótesis, alcance y é…
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
          Elegir un candidato para semana 3; definir hipótesis medible,
          non-goals y criterio de éxito/fallo.
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
