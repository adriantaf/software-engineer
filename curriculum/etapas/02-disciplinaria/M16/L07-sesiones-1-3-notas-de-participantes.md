---
id: L07
materia: M16
orden: 7
titulo: Sesiones 1–3 — notas de participantes
horas: 5
semana: 2
lectura: Facilitación; notas estructuradas
evidencia: sesiones/participante-1..3.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** `sesiones/participante-1.md` … `participante-3.md`.


      Personas reales (design partner, conocidos del rubro, compañeros). No
      auto-test.
  - id: s2
    tipo: ejemplo
    titulo: 2. Facilita y anota
    xp: 10
    cuerpo: |-
      ```markdown
      # Participante P1
      Consentimiento: sí
      Perfil: staff de … (anónimo)
      Tarea 1: …
      Obstáculos:
      Pedidos textuales:
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Sesiones 1–3 — notas de participantes" como hecha, ¿qué
      cuenta de verdad?
    opciones:
      - id: a
        texto: sesiones/participante-1..3.md
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
    pregunta: ¿Es buena práctica en esta lección? “Sesiones inventadas."
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
        texto: '`sesiones/participante-1.md` … `participante-3.md`.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Commit parcial el mismo día
    xp: 10
    cuerpo: '`docs(m16): sesiones 1-3 usabilidad`'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Tres archivos de sesión con consentimiento anotado, tareas y pedidos
        textuales relevantes.
      - Sin PII innecesaria (usa P1/P2/P3).
      - 'Commit `docs(m16): sesiones 1-3 usabilidad`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L07 — Sesiones 1–3 — notas de participantes

**~5.0 h · Semana 2**

Personas reales (design partner, conocidos del rubro, compañeros). No auto-test.

## Objetivo

`sesiones/participante-1.md` … `participante-3.md`.

## Pasos (hazlos en orden)

### 1. Agenda 3 sesiones (ya deberías haber citado)

### 2. Facilita y anota (3×15–30 min + buffer)

Plantilla:

```markdown
# Participante P1
Consentimiento: sí
Perfil: staff de … (anónimo)
Tarea 1: …
Obstáculos:
Pedidos textuales:
```

### 3. Commit parcial el mismo día

`docs(m16): sesiones 1-3 usabilidad`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Tres sesiones reales con notas por participante | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Tres archivos de sesión con consentimiento anotado, tareas y pedidos textuales relevantes.
2. Sin PII innecesaria (usa P1/P2/P3).
3. Commit `docs(m16): sesiones 1-3 usabilidad`.

## Errores comunes

- Sesiones inventadas.
- Facilitador que interrumpe y “enseña” la UI.
- Notas solo “le fue bien”.

## Siguiente

[L08 — Sesiones 4–5 y resumen agregado P2](L08-sesiones-4-5-y-resumen-agregado-p2.md)
