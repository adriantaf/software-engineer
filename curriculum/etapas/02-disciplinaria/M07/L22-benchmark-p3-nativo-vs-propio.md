---
id: L22
materia: M07
orden: 22
titulo: 'Benchmark P3: nativo vs propio'
horas: 5
semana: 6
lectura: 'Medir antes de opinar: microbenchmarks honestos'
evidencia: bench/ con tabla tiempos documentada
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3 exige números, no opiniones. Mides insert/lookup en tu hash y array vs
      nativos.


      **Objetivo de esta lección:** Correr un bench reproducible y dejar tabla
      de tiempos en el repo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Harness
    xp: 10
    cuerpo: |-
      ```bash
      npm run bench
      # o: npx tsx bench/run.ts
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Casos
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m07-estructuras/bench
      git commit -m "feat(m07): bench P3 nativo vs propio"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Benchmark P3: nativo vs propio», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Benchmark P3: nativo vs
          propio
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

      `npm run bench`
    comandoEsperado:
      - npm run bench
      - git add projects/m07-estructuras/bench
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npm run bench'
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
        texto: Correr un bench reproducible y dejar tabla de tiempos en el repo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Ejecuta y pega
    xp: 10
    cuerpo: >-
      Copia salida a `bench/RESULTADOS.md` con fecha y máquina (sin datos
      personales).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `bench/run.ts` compara ≥2 estructuras propias vs nativas
        (`Array`/`Map`).
      - Tabla de tiempos en `bench/RESULTADOS.md` (o README P3).
      - 'Commit `feat(m07): bench P3 nativo vs propio`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L22 — Benchmark P3: nativo vs propio

**~5.0 h · Semana 6**

P3 exige números, no opiniones. Mides insert/lookup en tu hash y array vs nativos.

## Objetivo

Correr un bench reproducible y dejar tabla de tiempos en el repo.

## Pasos

### 1. Harness (50 min)

`bench/run.ts` con `performance.now()`, warmup 1 iter, luego mide. Parámetro `N` (default 100_000).

### 2. Casos (90 min)

Mínimo:

- `DynamicArray.push` vs `Array.push`
- `HashMap.set/get` vs `Map.set/get`

Opcional: heap extract vs array+sort periódico.

### 3. Ejecuta y pega (40 min)

```bash
npm run bench
# o: npx tsx bench/run.ts
```

Copia salida a `bench/RESULTADOS.md` con fecha y máquina (sin datos personales).

### 4. Lectura crítica (30 min)

Párrafo: por qué el nativo suele ganar y qué aprendiste implementando.

### 5. Commit (15 min)

```bash
git add projects/m07-estructuras/bench
git commit -m "feat(m07): bench P3 nativo vs propio"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Metodología: warmup, N grande, no mentir con N=10 | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `bench/run.ts` compara ≥2 estructuras propias vs nativas (`Array`/`Map`).
2. Tabla de tiempos en `bench/RESULTADOS.md` (o README P3).
3. Commit `feat(m07): bench P3 nativo vs propio`.

## Errores comunes

- Benchmark con N trivial o sin warmup.
- Conclusiones absolutas (“soy más rápido que V8”).
- No versionar el comando para reproducir.

## Siguiente

[L23 — README cuándo usar cada estructura](L23-readme-cuando-usar-cada-estructura.md)
