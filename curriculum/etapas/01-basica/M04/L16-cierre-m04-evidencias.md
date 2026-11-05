---
id: L16
materia: M04
orden: 16
titulo: 'Cierre M04: evidencias y dominio'
horas: 5
semana: 4
lectura: Checklist projects/m04-stats/README.md + ficha M04
evidencia: notas/cierre-m04.md + progress.json actualizable
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras la materia como en M01 L08: checklist honesta, criterios de
      dominio y bitácora de lo aprendido antes de marcar la UI.


      **Objetivo de esta lección:** Verificar P1–P3 y proyecto, autoevaluar
      dominio y dejar `notas/cierre-m04.md` con retro y siguiente materia.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Checklist de evidencias
    xp: 10
    cuerpo: >-
      En `projects/m04-stats/notas/cierre-m04.md`: | Ítem | Evidencia | ¿Marco
      en UI? | |------|-----------|---------------| | **P1** | sim-moneda 10k +
      conclusión | | | **P2** | CSV + pipeline + tablas | | | **P3** |
      hipotesis-viernes (u otra) | | | **Proyecto** | informe.md | | |
      **Lecciones** | L01–L16 solo si “Hecho cuando” | |
  - id: s3
    tipo: ejemplo
    titulo: Criterios de dominio
    xp: 10
    cuerpo: >-
      Responde sí/no + una frase cada uno: - [ ] Escribí “correlación ≠
      causalidad” con ejemplo propio. - [ ] Puedo explicar mi histograma a un no
      técnico. - [ ] Interpreté un IC sin frase bayesiana incorrecta. - [ ] El
      informe tiene limitaciones y recomendación. Si algún “no”, anota qué
      lección repetirás 1 h.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cierre M04: evidencias y dominio», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: '`cierre-m04.md` con tabla y dominio honesto.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cierre M04: evidencias
          y dominio
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Marcar la materia completa sin
      `informe.md`."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
          Verificar P1–P3 y proyecto, autoevaluar dominio y dejar
          `notas/cierre-m04.md` con retro y siguiente materia.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: proyecto
    titulo: Proyecto de cierre · M04
    xp: 25
    enunciado: >-
      Cierra **Probabilidad y estadística aplicada** con evidencia real en el
      repo. Marca la rúbrica solo si puedes demostrar cada criterio (si no está
      en git, no cuenta).
    entregables:
      - 'P1: Simular experimentos (moneda, dados) y contrastar con teoría'
      - 'P2: Estadísticos descriptivos sobre un CSV real'
      - 'P3: Intervalo de confianza / hipótesis simple interpretada'
      - 'Proyecto: Informe de datos de un negocio o dataset público'
      - notas/cierre-m04.md + progress.json actualizable
    rubrica:
      - id: r1
        criterio: '`cierre-m04.md` con tabla y dominio honesto.'
      - id: r2
        criterio: Sabes qué checkboxes de la ficha puedes marcar hoy.
      - id: r3
        criterio: '`informe.md` y P1–P3 verificados en repo.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`cierre-m04.md` con tabla y dominio honesto.'
      - Sabes qué checkboxes de la ficha puedes marcar hoy.
      - '`informe.md` y P1–P3 verificados en repo.'
    siguiente: Materia M04 lista para marcar completada cuando la rúbrica sea real.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Cierre M04: evidencias y dominio

**~5 h · Semana 4**

Cierras la materia como en M01 L08: checklist honesta, criterios de dominio y bitácora de lo aprendido antes de marcar la UI.

## Objetivo

Verificar P1–P3 y proyecto, autoevaluar dominio y dejar `notas/cierre-m04.md` con retro y siguiente materia.

## Pasos

### 1. Checklist de evidencias (45 min)

En `projects/m04-stats/notas/cierre-m04.md`:

| Ítem | Evidencia | ¿Marco en UI? |
|------|-----------|---------------|
| **P1** | sim-moneda 10k + conclusión | |
| **P2** | CSV + pipeline + tablas | |
| **P3** | hipotesis-viernes (u otra) | |
| **Proyecto** | informe.md | |
| **Lecciones** | L01–L16 solo si “Hecho cuando” | |

### 2. Criterios de dominio (40 min)

Responde sí/no + una frase cada uno:

- [ ] Escribí “correlación ≠ causalidad” con ejemplo propio.
- [ ] Puedo explicar mi histograma a un no técnico.
- [ ] Interpreté un IC sin frase bayesiana incorrecta.
- [ ] El informe tiene limitaciones y recomendación.

Si algún “no”, anota qué lección repetirás 1 h.

### 3. Retro semana 4 (30 min)

```markdown
## Qué bloqueó
-

## Qué reutilizaré en M22
-

## Qué sigue (M05)
-
```

### 4. Ritual de progreso (15 min)

1. Marca lecciones completadas (solo las que cumplen criterio).
2. Marca prácticas/proyecto con evidencia en git.
3. Actualiza `progress.json` cuando toque el ritual semanal y commitea.

### 5. Lectura de cierre (opcional, 60 min)

Repaso rápido Walpole caps. 2, 5–6, 8–9 según huecos que marcaste.

## Hecho cuando

1. `cierre-m04.md` con tabla y dominio honesto.
2. Sabes qué checkboxes de la ficha puedes marcar hoy.
3. `informe.md` y P1–P3 verificados en repo.

## Errores comunes

- Marcar la materia completa sin `informe.md`.
- P3 con conclusión causal fuerte.
- Lecciones marcadas sin commits de evidencia.

## Siguiente

Vuelve a la [ficha M04](../M04-probabilidad-estadistica.md), cierra checkboxes con evidencia, y pasa a **M05 — Organización de computadoras**.
