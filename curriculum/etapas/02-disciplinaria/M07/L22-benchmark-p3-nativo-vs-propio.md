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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Correr un bench reproducible y dejar tabla de tiempos en el
      repo.


      P3 exige números, no opiniones. Mides insert/lookup en tu hash y array vs
      nativos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Harness
    xp: 10
    cuerpo: |-
      ```bash
      npm run bench
      # o: npx tsx bench/run.ts
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Benchmark P3: nativo vs propio" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: bench/ con tabla tiempos documentada
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

      `npm run bench`
    comandoEsperado:
      - npm run bench
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npm run bench'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Correr un bench reproducible y dejar tabla de tiempos en el repo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Casos
    xp: 10
    cuerpo: |-
      Mínimo:

      - `DynamicArray.push` vs `Array.push`
      - `HashMap.set/get` vs `Map.set/get`

      Opcional: heap extract vs array+sort periódico.
  - id: s7
    tipo: ejemplo
    titulo: 3. Ejecuta y pega
    xp: 10
    cuerpo: |-
      ```bash
      npm run bench
      # o: npx tsx bench/run.ts
      ```
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
