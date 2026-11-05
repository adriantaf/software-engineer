---
id: L12
materia: M12
orden: 12
titulo: Revisión M13 y cierre M12
horas: 5
semana: 3
lectura: Ficha M12 + handoff diseño
evidencia: nota-handoff-m13.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Handoff explícito + cierre de evidencias.

      Dejas el testigo listo para diseño (Larman/UML en M13).
  - id: s2
    tipo: ejemplo
    titulo: 1. Relectura SRS
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m12-srs
      git commit -m "docs(m12): cierre handoff m13"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Revisión M13 y cierre M12" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: nota-handoff-m13.md
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

      `git add projects/m12-srs`
    comandoEsperado:
      - git add projects/m12-srs
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git add projects/m12-srs'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Handoff explícito + cierre de evidencias.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Handoff
    xp: 10
    cuerpo: |-
      `nota-handoff-m13.md`:

      - Entidades candidatas (Cliente, Servicio, Pedido, Usuario…)
      - Casos de uso Must
      - Reglas de conflicto de horario
      - Preguntas abiertas
      - Riesgos (alcance, datos, auth)
  - id: s7
    tipo: explicacion
    titulo: 3. Dominio
    xp: 10
    cuerpo: >-
      Auto-check de la ficha: ¿puedes decir “no” con alternativa escrita? ¿3
      RNF? ¿Must con criterios?
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas y
        riesgos.
      - README m12 con checklist P1–P3 y proyecto cerrados.
      - 'Commit `docs(m12): cierre handoff m13`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Revisión M13 y cierre M12

**~5.0 h · Semana 3**

Dejas el testigo listo para diseño (Larman/UML en M13).

## Objetivo

Handoff explícito + cierre de evidencias.

## Pasos

### 1. Relectura SRS (40 min)

Lee `srs-v1.md` como si fueras M13: marca ambigüedades.

### 2. Handoff (75 min)

`nota-handoff-m13.md`:

- Entidades candidatas (Cliente, Servicio, Pedido, Usuario…)
- Casos de uso Must
- Reglas de conflicto de horario
- Preguntas abiertas
- Riesgos (alcance, datos, auth)

### 3. Dominio (30 min)

Auto-check de la ficha: ¿puedes decir “no” con alternativa escrita? ¿3 RNF? ¿Must con criterios?

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): cierre handoff m13"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Handoff a análisis/diseño: entidades, casos de uso, riesgos | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas y riesgos.
2. README m12 con checklist P1–P3 y proyecto cerrados.
3. Commit `docs(m12): cierre handoff m13`.

## Errores comunes

- Handoff vacío “lee el SRS”.
- Reabrir alcance Must sin versión.
- No enlazar stories/SRS desde README.

## Siguiente

Cierra la [ficha M12](../M12-requerimientos.md). Siguiente: [M13 — Análisis y diseño](../M13-analisis-y-diseno.md).
