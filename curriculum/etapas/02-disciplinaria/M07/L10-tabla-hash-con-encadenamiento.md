---
id: L10
materia: M07
orden: 10
titulo: Tabla hash con encadenamiento
horas: 5.0
semana: 3
lectura: "Encadenamiento (chaining): buckets y listas"
evidencia: HashMapChaining con set/get/delete + load factor logged
---

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
