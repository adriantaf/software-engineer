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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar un hash string→número determinista, documentar
      colisiones y dejar tests con valores esperados fijos.


      Sin una función hash defendible, la tabla de la próxima lección es
      decorado.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```ts

      expect(hashString("")).toBe(/* valor fijo */)

      expect(hashString("agenda")).toBe(/* ... */)

      expect(hashString("Agenda")).not.toBe(hashString("agenda")) // si tu fn es
      case-sensitive

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Función hash y mapa conceptual" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Hash notes + función hash string→number con tests deterministas
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

      `mkdir -p src/hash`
    comandoEsperado:
      - mkdir -p src/hash
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p src/hash'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Implementar un hash string→número determinista, documentar colisiones
          y dejar tests con valores esperados fijos.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Implementa FNV-1a (u otra simple)
    xp: 10
    cuerpo: >-
      ```bash

      mkdir -p src/hash

      ```


      `src/hash/fnv1a.ts`: `hashString(s: string): number` (uint32). Misma
      entrada → misma salida siempre.
  - id: s7
    tipo: ejemplo
    titulo: 3. Tests deterministas
    xp: 10
    cuerpo: >-
      ```ts

      expect(hashString("")).toBe(/* valor fijo */)

      expect(hashString("agenda")).toBe(/* ... */)

      expect(hashString("Agenda")).not.toBe(hashString("agenda")) // si tu fn es
      case-sensitive

      ```
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
