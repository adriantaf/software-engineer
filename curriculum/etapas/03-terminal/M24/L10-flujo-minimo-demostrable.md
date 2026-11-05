---
id: L10
materia: M24
orden: 10
titulo: Flujo mínimo demostrable
horas: 5
semana: 3
lectura: API reference secciones usadas en el spike
evidencia: projects/m24-emergentes/spike/ + demo-log.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 exige PoC, no repositorio vacío con intenciones.


      Conceptos que debes poder explicar al cerrar:


      - Happy path

      - Idempotencia básica

      - Logs sin PII


      **Objetivo de esta lección:** Implementar un flujo que un mentor pueda ver
      en ≤10 min (webhook, evento UI, mensaje test, etc.).


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
      git commit -m "docs(m24): l10 flujo-m-nimo-demostrable"
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
      git commit -m "docs(m24): l10 flujo-m-nimo-demostrable"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Flujo mínimo demostrable», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Flujo mínimo
          demostrable
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
          Implementar un flujo que un mentor pueda ver en ≤10 min (webhook,
          evento UI, mensaje test, etc.).
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
    cuerpo: 'Si usas webhooks: verifica firma o documenta TODO explícito.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Existe el entregable: `projects/m24-emergentes/spike/ + demo-log.md`.'
      - Flujo demo reproducible.
      - demo-log.md con pasos.
      - 'Commit `docs(m24): l10 …` en el historial.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Flujo mínimo demostrable

**~5 h · Semana 3**

Evalúas tecnología emergente con decisión escrita. Hoy entregas **`projects/m24-emergentes/spike/ + demo-log.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M24.

## Objetivo

Implementar un flujo que un mentor pueda ver en ≤10 min (webhook, evento UI, mensaje test, etc.).

## Por qué empieza así

P3 exige PoC, no repositorio vacío con intenciones.

Conceptos que debes poder explicar al cerrar:

- Happy path
- Idempotencia básica
- Logs sin PII

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Lee fuentes **primarias** (docs oficiales / pricing / límites): _API reference secciones usadas en el spike_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs.

### 2. Prepara evidencia y carpetas (20–30 min)

Confirma rutas bajo `projects/m24-emergentes`.

Completa el happy path del plan. Registra en `spike/demo-log.md` pasos + capturas o salida terminal.

### 3. Laboratorio principal (90–120 min)

Si usas webhooks: verifica firma o documenta TODO explícito.

### 4. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m24): l10 flujo-m-nimo-demostrable"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs oficiales del candidato + ficha M24 | API reference secciones usadas en el spike | [producto-saas (encaje ICP)](../../../producto-saas.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M24](../../../bibliografia.md#m24-tecnologias-emergentes) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m24-emergentes/spike/ + demo-log.md`.
2. Flujo demo reproducible.
3. demo-log.md con pasos.
4. Commit `docs(m24): l10 …` en el historial.

## Errores comunes

- Demo solo en tu máquina sin instrucciones.
- PII real en prueba.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L11 — Medición contra la hipótesis](L11-medicion-contra-la-hipotesis.md)
