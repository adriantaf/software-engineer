---
id: L09
materia: M07
orden: 9
titulo: Función hash y mapa conceptual
horas: 5
semana: 3
lectura: 'Funciones hash, universo de claves y colisiones'
evidencia: Hash notes + función hash string→number con tests deterministas
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin una función hash defendible, la tabla de la próxima lección es
      decorado.


      **Objetivo de esta lección:** Implementar un hash string→número
      determinista, documentar colisiones y dejar tests con valores esperados
      fijos.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```ts

      expect(hashString("")).toBe(/* valor fijo */)

      expect(hashString("agenda")).toBe(/* ... */)

      expect(hashString("Agenda")).not.toBe(hashString("agenda")) // si tu fn es
      case-sensitive

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Implementa FNV-1a (u otra simple)
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p src/hash

      ```


      `src/hash/fnv1a.ts`: `hashString(s: string): number` (uint32). Misma
      entrada → misma salida siempre.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Función hash y mapa conceptual», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Función hash y mapa
          conceptual
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

      `mkdir -p src/hash`
    comandoEsperado:
      - mkdir -p src/hash
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p src/hash'
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
          Implementar un hash string→número determinista, documentar colisiones
          y dejar tests con valores esperados fijos.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests deterministas
    xp: 10
    cuerpo: >-
      Incluye dos strings distintos que colisionen **módulo 8** (búsqueda corta
      o documenta el par).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `src/hash/fnv1a.ts` (o similar) hash string→uint32 determinista con ≥4
        tests fijos.
      - '`docs/hash-notes.md` explica colisión y por qué modulo tabla.'
      - 'Commit `feat(m07): funcion hash string`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
