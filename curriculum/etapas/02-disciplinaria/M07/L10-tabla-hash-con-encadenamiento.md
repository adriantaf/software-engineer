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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar `HashMap<K,V>` (string keys al inicio está bien)
      con encadenamiento, API set/get/delete y `loadFactor` visible.


      Cada bucket es una lista (o array) de pares clave-valor. Hoy montas el
      mapa usable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Diseño de buckets
    xp: 10
    cuerpo: |-
      ```bash
      npx tsx -e "import { HashMap } from './src/hash-map.ts'; ..."
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tabla hash con encadenamiento" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: HashMapChaining con set/get/delete + load factor logged
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

      `npx tsx -e "import { HashMap } from './src/hash-map.ts'; ..."`
    comandoEsperado:
      - 'npx tsx -e "import { HashMap } from ''./src/hash-map.ts''; ..."'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: npx tsx -e "import { HashMap } from ''./src/hash-map.ts''; ..."'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Entregar `HashMap<K,V>` (string keys al inicio está bien) con
          encadenamiento, API set/get/delete y `loadFactor` visible.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementación
    xp: 10
    cuerpo: >-
      `src/hash-map.ts`: array de buckets (capacidad inicial 8 o 16); `set`
      inserta o actualiza; `get`/`has`; `delete` remueve de la cadena; getter
      `loadFactor = size/capacity`.
  - id: s7
    tipo: explicacion
    titulo: 3. Tests
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
