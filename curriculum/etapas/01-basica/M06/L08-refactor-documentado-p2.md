---
id: L08
materia: M06
orden: 8
titulo: Refactor documentado (P2)
horas: 5
semana: 2
lectura: 'Repaso CC 1–3, 6, 10 + diff git'
evidencia: >-
  refactor-p2.md con antes/después + diff; commit refactor(m06): P2 codigo
  limpio
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar documento `refactor-p2.md` con objetivos, diff
      representativo y métricas cualitativas (líneas, complejidad, nombres).


      La práctica **P2** exige evidencia: no solo código bonito, sino
      **historia** del cambio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Baseline
    xp: 10
    cuerpo: |-
      ```bash
      git log --oneline -5
      git diff pre-refactor-semana1..HEAD --stat
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Refactor documentado (P2)" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: >-
          refactor-p2.md con antes/después + diff; commit refactor(m06): P2
          codigo limpio
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

      `git log --oneline -5`
    comandoEsperado:
      - git log --oneline -5
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git log --oneline -5'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Entregar documento `refactor-p2.md` con objetivos, diff representativo
          y métricas cualitativas (líneas, complejidad, nombres).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Redactar `refactor-p2.md`
    xp: 10
    cuerpo: |-
      Secciones:

      - Motivación (CC + SOLID).
      - Capturas o bloques `diff` de 2–3 archivos clave.
      - Tabla: olor → técnica → resultado.
      - Checklist CC aplicado.
  - id: s7
    tipo: explicacion
    titulo: 3. Pulido final
    xp: 10
    cuerpo: Última pasada nombres/funciones. Elimina dead code.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`refactor-p2.md` completo con diff real.'
      - Código actual refleja nombres y funciones pequeñas.
      - Tests verdes.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L08 — Refactor documentado (P2)

**~5 h · Semana 2**

La práctica **P2** exige evidencia: no solo código bonito, sino **historia** del cambio.

## Objetivo

Entregar documento `refactor-p2.md` con objetivos, diff representativo y métricas cualitativas (líneas, complejidad, nombres).

## Pasos

### 1. Baseline (30 min)

```bash
git log --oneline -5
git diff pre-refactor-semana1..HEAD --stat
```

Si no tienes tag, compara commit de L04 vs actual.

### 2. Redactar `refactor-p2.md` (90 min)

Secciones:

- Motivación (CC + SOLID).
- Capturas o bloques `diff` de 2–3 archivos clave.
- Tabla: olor → técnica → resultado.
- Checklist CC aplicado.

### 3. Pulido final (120 min)

Última pasada nombres/funciones. Elimina dead code.

### 4. Tests y cobertura manual (45 min)

Lista casos de prueba; no hace falta cobertura 100 %.

### 5. Commit evidencia (15 min)

```bash
git add refactor-p2.md
git commit -m "docs(m06): evidencia refactor P2 codigo limpio"
```

Marca **P2** en la ficha cuando exista diff + narrativa.

## Hecho cuando

1. `refactor-p2.md` completo con diff real.
2. Código actual refleja nombres y funciones pequeñas.
3. Tests verdes.

## Errores comunes

- Diff ilegible (pegar 2000 líneas sin contexto).
- Refactor sin tests.

## Siguiente

[L09 — Union types y modelado de estados](L09-union-types-y-estados.md)
