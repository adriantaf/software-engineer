---
id: L10
materia: M07
orden: 10
titulo: Tabla hash con encadenamiento
horas: 5
semana: 3
lectura: 'Encadenamiento (chaining): buckets y listas'
evidencia: HashMapChaining con set/get/delete + load factor logged
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cada bucket es una lista (o array) de pares clave-valor. Hoy montas el
      mapa usable.


      **Objetivo de esta lección:** Entregar `HashMap<K,V>` (string keys al
      inicio está bien) con encadenamiento, API set/get/delete y `loadFactor`
      visible.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Diseño de buckets
    xp: 10
    cuerpo: |-
      ```bash
      npx tsx -e "import { HashMap } from './src/hash-map.ts'; ..."
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementación
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m07): hashmap encadenamiento"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tabla hash con encadenamiento», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tabla hash con
          encadenamiento
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

      `npx tsx -e "import { HashMap } from './src/hash-map.ts'; ..."`
    comandoEsperado:
      - 'npx tsx -e "import { HashMap } from ''./src/hash-map.ts''; ..."'
      - 'git commit -am "feat(m07): hashmap encadenamiento"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: npx tsx -e "import { HashMap } from ''./src/hash-map.ts''; ..."'
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
          Entregar `HashMap<K,V>` (string keys al inicio está bien) con
          encadenamiento, API set/get/delete y `loadFactor` visible.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests
    xp: 10
    cuerpo: >-
      set+get; overwrite; delete + get undefined; has false; varias claves en
      mismo bucket (usa el par colisionante de L09 o fuerza módulo pequeño en
      test).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `src/hash-map.ts` con `set`/`get`/`delete`/`has` y buckets por
        encadenamiento.
      - >-
        Tests cubren overwrite, delete, get ausente; logueas o expones
        `loadFactor`.
      - 'Commit `feat(m07): hashmap encadenamiento`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Tabla hash con encadenamiento

**~5.0 h · Semana 3**

Cada bucket es una lista (o array) de pares clave-valor. Hoy montas el mapa usable.

## Objetivo

Entregar `HashMap<K,V>` (string keys al inicio está bien) con encadenamiento, API set/get/delete y `loadFactor` visible.

## Pasos

### 1. Diseño de buckets (30 min)

Escribe en `docs/hash-notes.md` la forma de cada entrada `{ key, value }` y cómo resuelves igualdad de claves.

### 2. Implementación (100 min)

`src/hash-map.ts`: array de buckets (capacidad inicial 8 o 16); `set` inserta o actualiza; `get`/`has`; `delete` remueve de la cadena; getter `loadFactor = size/capacity`.

### 3. Tests (60 min)

set+get; overwrite; delete + get undefined; has false; varias claves en mismo bucket (usa el par colisionante de L09 o fuerza módulo pequeño en test).

### 4. Smoke manual (20 min)

```bash
npx tsx -e "import { HashMap } from './src/hash-map.ts'; ..."
```

O un test de integración corto.

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): hashmap encadenamiento"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Hash map con encadenamiento; set/get/delete | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/hash-map.ts` con `set`/`get`/`delete`/`has` y buckets por encadenamiento.
2. Tests cubren overwrite, delete, get ausente; logueas o expones `loadFactor`.
3. Commit `feat(m07): hashmap encadenamiento`.

## Errores comunes

- Open addressing sin decirlo (esta lección es chaining).
- No manejar update de clave existente.
- Usar `Map` nativo por dentro y llamarlo implementación propia.

## Siguiente

[L11 — Factor de carga y rehash](L11-factor-de-carga-y-rehash.md)
