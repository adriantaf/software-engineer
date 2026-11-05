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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La práctica **P2** exige evidencia: no solo código bonito, sino
      **historia** del cambio.


      **Objetivo de esta lección:** Entregar documento `refactor-p2.md` con
      objetivos, diff representativo y métricas cualitativas (líneas,
      complejidad, nombres).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Baseline
    xp: 10
    cuerpo: |-
      ```bash
      git log --oneline -5
      git diff pre-refactor-semana1..HEAD --stat
      ```

      Si no tienes tag, compara commit de L04 vs actual.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Redactar `refactor-p2.md`
    xp: 10
    cuerpo: |-
      ```bash
      git add refactor-p2.md
      git commit -m "docs(m06): evidencia refactor P2 codigo limpio"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Refactor documentado (P2)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`refactor-p2.md` completo con diff real.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Refactor documentado
          (P2)
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git log --oneline -5`
    comandoEsperado:
      - git log --oneline -5
      - git diff pre-refactor-semana1..HEAD --stat
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git log --oneline -5'
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
          Entregar documento `refactor-p2.md` con objetivos, diff representativo
          y métricas cualitativas (líneas, complejidad, nombres).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Pulido final
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
