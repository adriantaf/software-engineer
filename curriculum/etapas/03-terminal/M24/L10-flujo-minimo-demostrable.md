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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar un flujo que un mentor pueda ver en ≤10 min
      (webhook, evento UI, mensaje test, etc.).


      P3 exige PoC, no repositorio vacío con intenciones.


      Conceptos que debes poder explicar al cerrar:


      - Happy path

      - Idempotencia básica

      - Logs sin PII
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura concreta de la fuente
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/ curriculum/etapas/03-terminal/ || git add projects/
      git status
      git commit -m "docs(m24): l10 flujo-m-nimo-demostrable"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Flujo mínimo demostrable" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m24-emergentes/spike/ + demo-log.md
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
          Implementar un flujo que un mentor pueda ver en ≤10 min (webhook,
          evento UI, mensaje test, etc.).
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
      Confirma rutas bajo `projects/m24-emergentes`.


      Completa el happy path del plan. Registra en `spike/demo-log.md` pasos +
      capturas o salida terminal.
  - id: s7
    tipo: explicacion
    titulo: 3. Laboratorio principal
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
