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
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 y la CLI comparten semanas 3–4. Hoy cierras el canon de katas y dejas
      async sin deuda técnica grave.


      **Objetivo de esta lección:** CLI estable con flujo async completo; repo
      katas con **≥20** soluciones P1 listas para marcar.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Auditoría async CLI
    xp: 10
    cuerpo: >-
      Revisa cada comando: ¿siempre `await saveEstado`? ¿`main` captura errores?
      Añade prueba manual documentada en README habits.
  - id: s3
    tipo: ejemplo
    titulo: Completar P1 katas
    xp: 10
    cuerpo: >-
      Hasta **20** archivos en `src/katas/` o carpeta `katas/` documentada.
      README lista títulos y dificultad.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Integrar async en el proyecto», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: ≥20 katas con README (P1 lista para evidencia).
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Integrar async en el
          proyecto
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
    pregunta: ¿Es recomendable en esta lección? “Marcar P1 con 12 katas “casi”."
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
          CLI estable con flujo async completo; repo katas con ≥20 soluciones P1
          listas para marcar.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Refactor menor
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
