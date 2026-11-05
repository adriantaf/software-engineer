---
id: L02
materia: M01
orden: 2
titulo: Método y práctica deliberada
horas: 2
semana: 1
lectura: "Cómo estudiar (esta guía del plan) + regla 40/30/30"
evidencia: "projects/m01-diario/semana-0001.md con plan de la semana (bloques de horas)"
formato: pasos
xpLeccion: 70
pasos:
  - id: s1
    tipo: explicacion
    titulo: Consumo vs práctica deliberada
    xp: 10
    cuerpo: |
      **Consumo pasivo** = ver videos sin producir.

      **Práctica deliberada** = un objetivo concreto, feedback (error, diff, mentor) y repetición.

      La brújula del plan: **40 / 30 / 30** (teoría / práctica / proyecto). No es dogma rígido: si un día solo tienes 2 h, prioriza práctica + proyecto.
  - id: s2
    tipo: ejemplo
    titulo: Semana tipo (~20 h)
    xp: 10
    cuerpo: |
      | Bloque | Horas | Qué haces |
      |--------|-------|-----------|
      | Teoría / libro | 6–8 | Leer con lápiz: dudas, no subrayar todo |
      | Práctica | 6–8 | Comandos, ejercicios, evidencia en `projects/` |
      | Proyecto | 4–6 | Avance medible (diario, ADR, código) |
      | Retro | 1 | Qué bloqueó / qué sigue |

      Si solo tienes **2 h**: 1 h práctica + 1 h proyecto. La lectura se acorta o se mueve; no se inventa otro temario.
  - id: s3
    tipo: quiz
    titulo: "¿Qué es práctica deliberada?"
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Cuál es el mejor ejemplo de práctica deliberada?"
    opciones:
      - id: a
        texto: Ver 3 horas de tutoriales “para inspirarte”
      - id: b
        texto: Escribir entorno.md, fallar el commit, leer el error y corregirlo
      - id: c
        texto: Subrayar un capítulo entero sin tomar notas
    respuesta: b
    explicacionError: Deliberada = objetivo + feedback + repetición. Ver o subrayar sin producir no cuenta.
    explicacionOk: "Sí — produciste, fallaste, corregiste."
  - id: s4
    tipo: quiz
    titulo: Regla 40/30/30
    xp: 10
    variante: completar
    pregunta: "Completa: la regla del plan es 40 / 30 / ___ (teoría / práctica / ?)."
    respuesta:
      - "30"
      - "proyecto"
      - "30 proyecto"
    explicacionError: "El tercer bloque es **proyecto** (30%). Respuesta corta aceptada: `30` o `proyecto`."
    explicacionOk: Teoría 40 · práctica 30 · proyecto 30.
  - id: s5
    tipo: quiz
    titulo: Bitácora de la semana
    xp: 15
    variante: verdadero_falso
    pregunta: "La evidencia de L02 es tener projects/m01-diario/semana-0001.md con bloques de horas planificados."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: "Sí es verdadero — sin bitácora no hay método instalado."
    explicacionOk: Correcto. Escribe el plan en la bitácora ahora (offline).
  - id: s6
    tipo: resumen
    titulo: Cierre L02
    xp: 10
    puntos:
      - Leíste (o repasas) Cómo estudiar.
      - Entiendes 40/30/30 y práctica deliberada.
      - "Existe `semana-0001.md` con bloques de horas reales para tu semana."
    siguiente: "Siguiente → L03 Shell, navegación y archivos."
---

## Lectura complementaria

- [Cómo estudiar](../../../como-estudiar.md) — flujo por materia, qué cuenta como terminado.

## Plantilla bitácora

```markdown
# Semana 0001 — M01

## Plan (horas)
- Teoría:
- Práctica:
- Proyecto:

## Qué haré concreto
- …

## Riesgos / bloqueos previstos
- …
```
