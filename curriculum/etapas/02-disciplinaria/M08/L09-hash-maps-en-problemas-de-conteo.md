---
id: L09
materia: M08
orden: 9
titulo: Hash maps en problemas de conteo
horas: 5
semana: 3
lectura: Patrón hashing / conteo de frecuencias
evidencia: 2 problemas patrón hash
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Resolver dos problemas de conteo/hash con evidencia completa
      e índice actualizado.


      El mapa de frecuencias convierte muchos O(n²) en O(n) promedio.
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige problemas
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): problemas hash conteo"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Hash maps en problemas de conteo" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: 2 problemas patrón hash
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

      `git commit -am "feat(m08): problemas hash conteo"`
    comandoEsperado:
      - 'git commit -am "feat(m08): problemas hash conteo"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m08): problemas hash conteo"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Resolver dos problemas de conteo/hash con evidencia completa e índice
          actualizado.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Problema A
    xp: 10
    cuerpo: >-
      Carpeta `problems/…`: enunciado, solución con `Map`, complejidad, 3 tests
      (borde: vacío / un elemento).
  - id: s7
    tipo: explicacion
    titulo: 3. Problema B
    xp: 10
    cuerpo: >-
      Igual plantilla. Si two-sum ya existía con fuerza bruta, reescribe con
      hash y anota mejora.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Dos problemas en `problems/` con patrón hash/conteo, complejidad y ≥3
        tests c/u.
      - Actualizas `indice-patrones.md` con esas filas.
      - 'Commit `feat(m08): problemas hash conteo`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Hash maps en problemas de conteo

**~5.0 h · Semana 3**

El mapa de frecuencias convierte muchos O(n²) en O(n) promedio.

## Objetivo

Resolver dos problemas de conteo/hash con evidencia completa e índice actualizado.

## Pasos

### 1. Elige problemas (15 min)

Ejemplos: anagramas (`isAnagram`), two-sum con `Map`, primer carácter único, conteo de votos. Dos bastan.

### 2. Problema A (70 min)

Carpeta `problems/…`: enunciado, solución con `Map`, complejidad, 3 tests (borde: vacío / un elemento).

### 3. Problema B (70 min)

Igual plantilla. Si two-sum ya existía con fuerza bruta, reescribe con hash y anota mejora.

### 4. Índice (30 min)

Patrón `hash-conteo` en `indice-patrones.md`.

### 5. Commit (15 min)

```bash
git commit -am "feat(m08): problemas hash conteo"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Frequency map; anagramas; two-sum con hash | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dos problemas en `problems/` con patrón hash/conteo, complejidad y ≥3 tests c/u.
2. Actualizas `indice-patrones.md` con esas filas.
3. Commit `feat(m08): problemas hash conteo`.

## Errores comunes

- Solución O(n²) presentada como hash.
- Usar sort+two pointers sin reconocer que no es el patrón de hoy.
- Índice sin enlazar archivos.

## Siguiente

[L10 — Two pointers en arrays ordenados](L10-two-pointers-en-arrays-ordenados.md)
