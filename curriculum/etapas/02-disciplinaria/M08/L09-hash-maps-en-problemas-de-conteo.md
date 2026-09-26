---
id: L09
materia: M08
orden: 9
titulo: Hash maps en problemas de conteo
horas: 5.0
semana: 3
lectura: Patrón hashing / conteo de frecuencias
evidencia: 2 problemas patrón hash
---

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
