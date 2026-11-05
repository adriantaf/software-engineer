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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Verificar P1–P3 y proyecto, autoevaluar dominio y dejar
      `notas/cierre-m04.md` con retro y siguiente materia.


      Cierras la materia como en M01 L08: checklist honesta, criterios de
      dominio y bitácora de lo aprendido antes de marcar la UI.
  - id: s2
    tipo: ejemplo
    titulo: 1. Checklist de evidencias
    xp: 10
    cuerpo: |-
      En `projects/m04-stats/notas/cierre-m04.md`:

      | Ítem | Evidencia | ¿Marco en UI? |
      |------|-----------|---------------|
      | **P1** | sim-moneda 10k + conclusión | |
      | **P2** | CSV + pipeline + tablas | |
      | **P3** | hipotesis-viernes (u otra) | |
      | **Proyecto** | informe.md | |
      | **Lecciones** | L01–L16 solo si “Hecho cuando” | |
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cierre M04: evidencias y dominio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/cierre-m04.md + progress.json actualizable
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Marcar la materia completa sin
      `informe.md`."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Verificar P1–P3 y proyecto, autoevaluar dominio y dejar
          `notas/cierre-m04.md` con retro y siguiente materia.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Criterios de dominio
    xp: 10
    cuerpo: |-
      Responde sí/no + una frase cada uno:

      - [ ] Escribí “correlación ≠ causalidad” con ejemplo propio.
      - [ ] Puedo explicar mi histograma a un no técnico.
      - [ ] Interpreté un IC sin frase bayesiana incorrecta.
      - [ ] El informe tiene limitaciones y recomendación.

      Si algún “no”, anota qué lección repetirás 1 h.
  - id: s7
    tipo: explicacion
    titulo: 3. Retro semana 4
    xp: 10
    cuerpo: '```markdown'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`cierre-m04.md` con tabla y dominio honesto.'
      - Sabes qué checkboxes de la ficha puedes marcar hoy.
      - '`informe.md` y P1–P3 verificados en repo.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
