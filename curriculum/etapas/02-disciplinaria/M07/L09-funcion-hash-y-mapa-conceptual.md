---
id: L09
materia: M07
orden: 9
titulo: Función hash y mapa conceptual
horas: 5.0
semana: 3
lectura: Funciones hash, universo de claves y colisiones
evidencia: Hash notes + función hash string→number con tests deterministas
---

# L09 — Función hash y mapa conceptual

**~5.0 h · Semana 3**

Sin una función hash defendible, la tabla de la próxima lección es decorado.

## Objetivo

Implementar un hash string→número determinista, documentar colisiones y dejar tests con valores esperados fijos.

## Pasos

### 1. Lectura (45 min)

Capítulo de tablas hash: universo, colisión, preferencia por distribución uniforme. Anota 5 términos en `docs/hash-notes.md`.

### 2. Implementa FNV-1a (u otra simple) (75 min)

```bash
mkdir -p src/hash
```

`src/hash/fnv1a.ts`: `hashString(s: string): number` (uint32). Misma entrada → misma salida siempre.

### 3. Tests deterministas (50 min)

```ts
expect(hashString("")).toBe(/* valor fijo */)
expect(hashString("agenda")).toBe(/* ... */)
expect(hashString("Agenda")).not.toBe(hashString("agenda")) // si tu fn es case-sensitive
```

Incluye dos strings distintos que colisionen **módulo 8** (búsqueda corta o documenta el par).

### 4. Notas de diseño (40 min)

En `docs/hash-notes.md`: dibuja “clave → hash → índice = h % m”. Una frase sobre por qué `m` primo o potencia de 2 (elige postura y justifica).

### 5. Commit (15 min)

```bash
git commit -am "feat(m07): funcion hash string"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Joyanes / texto univ. ED (ed. ES) | Hash: distribución, colisiones, por qué no usar solo key.length | [MDN Map (contraste)](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map) |
| Catálogo | Entrada de esta materia | [Bibliografía · M07](../../../bibliografia.md#m07-estructuras-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. `src/hash/fnv1a.ts` (o similar) hash string→uint32 determinista con ≥4 tests fijos.
2. `docs/hash-notes.md` explica colisión y por qué modulo tabla.
3. Commit `feat(m07): funcion hash string`.

## Errores comunes

- Hash no determinista (usa Date/random).
- Confundir “buen hash” con “encriptación”.
- Tests que solo chequean “es un número” sin valores esperados.

## Siguiente

[L10 — Tabla hash con encadenamiento](L10-tabla-hash-con-encadenamiento.md)
