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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El mapa de frecuencias convierte muchos O(n²) en O(n) promedio.


      **Objetivo de esta lección:** Resolver dos problemas de conteo/hash con
      evidencia completa e índice actualizado.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige problemas
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): problemas hash conteo"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Problema A
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m08): problemas hash conteo"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Hash maps en problemas de conteo», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Hash maps en problemas
          de conteo
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

      `git commit -am "feat(m08): problemas hash conteo"`
    comandoEsperado:
      - 'git commit -am "feat(m08): problemas hash conteo"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m08): problemas hash conteo"'
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
          Resolver dos problemas de conteo/hash con evidencia completa e índice
          actualizado.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Problema B
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
