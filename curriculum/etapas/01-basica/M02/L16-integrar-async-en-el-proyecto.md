---
id: L16
materia: M02
orden: 16
titulo: Integrar async en el proyecto
horas: 3
semana: 4
lectura: Repaso cap. 11 EJ + revisión load/save CLI
evidencia: m02-habits estable async + nota semana 4 en bitácora
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** CLI estable con flujo async completo; repo katas con **≥20**
      soluciones P1 listas para marcar.


      P1 y la CLI comparten semanas 3–4. Hoy cierras el canon de katas y dejas
      async sin deuda técnica grave.
  - id: s2
    tipo: ejemplo
    titulo: 1. Auditoría async CLI
    xp: 10
    cuerpo: >-
      Revisa cada comando: ¿siempre `await saveEstado`? ¿`main` captura errores?
      Añade prueba manual documentada en README habits.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Integrar async en el proyecto" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: m02-habits estable async + nota semana 4 en bitácora
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
    pregunta: ¿Es buena práctica en esta lección? “Marcar P1 con 12 katas “casi”."
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
          CLI estable con flujo async completo; repo katas con **≥20**
          soluciones P1 listas para marcar.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Completar P1 katas
    xp: 10
    cuerpo: >-
      Hasta **20** archivos en `src/katas/` o carpeta `katas/` documentada.
      README lista títulos y dificultad.
  - id: s7
    tipo: explicacion
    titulo: 3. Refactor menor
    xp: 10
    cuerpo: Extrae cualquier función >40 líneas del cli a `src/servicios/`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - ≥20 katas con README (P1 lista para evidencia).
      - CLI habits async sin errores silenciosos en prueba manual.
      - Commits de la semana 4 agrupados con sentido.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L16 — Integrar async en el proyecto

**~3 h · Semana 4**

Cierras la semana 4 consolidando async en la CLI, corrigiendo race conditions obvias y completando katas hasta **20** (P1).

## Objetivo

CLI estable con flujo async completo; repo katas con **≥20** soluciones P1 listas para marcar.

## Por qué importa

P1 y la CLI comparten semanas 3–4. Hoy cierras el canon de katas y dejas async sin deuda técnica grave.

## Pasos

### 1. Auditoría async CLI (45 min)

Revisa cada comando: ¿siempre `await saveEstado`? ¿`main` captura errores? Añade prueba manual documentada en README habits.

### 2. Completar P1 katas (90 min)

Hasta **20** archivos en `src/katas/` o carpeta `katas/` documentada. README lista títulos y dificultad.

### 3. Refactor menor (30 min)

Extrae cualquier función >40 líneas del cli a `src/servicios/`.

### 4. Retro semana 4 (25 min)

Bitácora: fetch usado, async explicado a un compañero imaginario en 3 frases.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Repaso cap. 11 |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. ≥20 katas con README (P1 lista para evidencia).
2. CLI habits async sin errores silenciosos en prueba manual.
3. Commits de la semana 4 agrupados con sentido.

## Errores comunes

- Marcar P1 con 12 katas “casi”.
- Duplicar lógica entre katas y CLI en vez de reutilizar ideas.
- Ignorar JSON corrupto (lo atacas en L17).

## Siguiente

[L17 — Errores, throw y mensajes](L17-errores-throw-y-mensajes.md)
