---
id: L08
materia: M01
orden: 8
titulo: ADR, bitácora y cierre
horas: 3
semana: 2
lectura: "Plantilla ADR + bitácora semana 2"
evidencia: "ADR + semana-0002.md + progress.json actualizado"
formato: pasos
xpLeccion: 100
pasos:
  - id: s1
    tipo: explicacion
    titulo: Documentar decisiones
    xp: 10
    cuerpo: |
      Un **ADR** (Architecture Decision Record) captura una decisión técnica: contexto, opciones, decisión y consecuencias.

      No es un ensayo. Es una nota que tu yo del futuro agradecerá.

      Hoy cierras M01: ADR + bitácora semana 2 + evidencia de P1–P3/proyecto.
  - id: s2
    tipo: ejemplo
    titulo: Esqueleto ADR
    xp: 10
    cuerpo: |
      ```markdown
      # ADR 001 — TypeScript como lenguaje principal del plan

      ## Estado
      Aceptada

      ## Contexto
      Necesito un lenguaje para todo el plan (CLI, web, tests) con tipado.

      ## Opciones
      1. JavaScript solo
      2. TypeScript
      3. Python

      ## Decisión
      TypeScript (strict) como default.

      ## Consecuencias
      + Mejor feedback en el editor; − curva inicial de tipos.
      ```
  - id: s3
    tipo: quiz
    titulo: Qué va en un ADR
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Qué sección es esencial en un ADR corto?"
    opciones:
      - id: a
        texto: Solo el logo de la empresa
      - id: b
        texto: Contexto, decisión y consecuencias
      - id: c
        texto: El historial completo de git blame
    respuesta: b
    explicacionError: Contexto + decisión + consecuencias (y opciones si aporta).
    explicacionOk: Correcto.
  - id: s4
    tipo: codigo
    titulo: Mini checklist en JS
    xp: 15
    enunciado: |
      Implementa `todasHechas(flags)` que recibe un array de booleanos y
      devuelve `true` solo si **todos** son `true` (rúbrica completa).
    language: javascript
    starter: |
      function todasHechas(flags) {
        // tu código
      }
    tests:
      - nombre: todos true
        assert: "todasHechas([true, true, true]) === true"
      - nombre: uno false
        assert: "todasHechas([true, false, true]) === false"
      - nombre: vacío
        assert: "todasHechas([]) === true"
    explicacionError: "Usa `flags.every(Boolean)` o un bucle. Array vacío → true."
  - id: s5
    tipo: proyecto
    titulo: Proyecto de cierre M01
    xp: 25
    enunciado: |
      Entrega el **diario de ingeniería** de M01. Marca la rúbrica solo si la evidencia existe en el repo (no mientas al checkbox).
    entregables:
      - "projects/m01-diario/entorno.md (P1)"
      - "≥7 commits atómicos en 7 días o log pegado en bitácora (P2)"
      - "projects/m01-diario/adr-001-*.md con contexto / decisión / consecuencias (P3)"
      - "Al menos 2 notas semana-NNNN.md + progress.json exportado"
    rubrica:
      - id: r1
        criterio: entorno.md existe con SO, Git, Node, editor
      - id: r2
        criterio: ADR 001 escrito y commiteado
      - id: r3
        criterio: Bitácora semana 2 (semana-0002.md) con retro honesta
      - id: r4
        criterio: Puedo explicar branching y un merge simple sin GUI
  - id: s6
    tipo: quiz
    titulo: Honor system
    xp: 10
    variante: verdadero_falso
    pregunta: "Debo marcar la rúbrica aunque el ADR aún no exista en disk."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: "Falso — si no está en git, no cuenta."
    explicacionOk: "Bien. Integridad > barra de progreso."
  - id: s7
    tipo: resumen
    titulo: M01 cerrado
    xp: 15
    puntos:
      - Método 40/30/30 + bitácora viva.
      - Shell y Git básicos sin depender solo de la GUI.
      - "ADR y evidencias en `projects/m01-diario/`."
      - "Siguiente materia: M02 Programación I (TypeScript)."
    siguiente: Vuelve al mapa de M01 y marca la materia completada cuando la rúbrica sea real.
---

## Lectura complementaria

- Plantilla ADR arriba → guárdala como `projects/m01-diario/adr-001-typescript.md`.
- Actualiza `progress.json` desde la UI (exportar) y haz commit semanal.
