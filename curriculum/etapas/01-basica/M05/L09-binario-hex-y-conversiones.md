---
id: L09
materia: M05
orden: 9
titulo: 'Binario, hex y conversiones'
horas: 5
semana: 3
lectura: 'Stallings — representación de datos, sistemas numéricos'
evidencia: projects/m05-como-corre/conversiones.ts + notas-conversiones.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Todo en la máquina es bits. Dominar conversiones evita errores en flags,
      permisos y protocolos.


      **Objetivo de esta lección:** Convertir entre decimal, binario y
      hexadecimal; interpretar bytes como datos; implementar conversiones en
      TypeScript con tests manuales claros.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```ts

      export function decToBin(n: number): string { /* solo enteros ≥0
      razonables */ }

      export function decToHex(n: number): string { /* mayúsculas opcional,
      consistente */ }

      export function binToDec(s: string): number { /* validar entrada */ }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`notas-conversiones.md`'
    xp: 10
    cuerpo: >-
      ```ts

      export function decToBin(n: number): string { /* solo enteros ≥0
      razonables */ }

      export function decToHex(n: number): string { /* mayúsculas opcional,
      consistente */ }

      export function binToDec(s: string): number { /* validar entrada */ }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Binario, hex y conversiones», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: Notas con 10 conversiones manuales + explicación chmod.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Binario, hex y
          conversiones
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Usar `parseInt` sin validar strings
      inválidos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
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
          Convertir entre decimal, binario y hexadecimal; interpretar bytes como
          datos; implementar conversiones en TypeScript con tests manuales
          claros.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Código `conversiones.ts`
    xp: 10
    cuerpo: >-
      En `projects/m05-como-corre/` (configura `tsx` si hace falta, como en
      M02): Añade al menos **8 casos de prueba** documentados al final del
      archivo o en comentarios.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Notas con 10 conversiones manuales + explicación chmod.
      - '`conversiones.ts` con funciones y casos de prueba ejecutables.'
      - Entiendes por qué hex agrupa bits de a 4.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Binario, hex y conversiones

**~5 h · Semana 3**

Todo en la máquina es bits. Dominar conversiones evita errores en flags, permisos y protocolos.

## Objetivo

Convertir entre decimal, binario y hexadecimal; interpretar bytes como datos; implementar conversiones en TypeScript con tests manuales claros.

## Pasos

### 1. Lectura (60–75 min)

Stallings: representación numérica (bases 2, 10, 16). Haz **10 conversiones a mano** antes de codear.

### 2. `notas-conversiones.md` (45 min)

Tabla de ejercicios resueltos (incluye permisos Unix `rwx` como ejemplo de bits).

### 3. Código `conversiones.ts` (120 min)

En `projects/m05-como-corre/` (configura `tsx` si hace falta, como en M02):

```ts
export function decToBin(n: number): string { /* solo enteros ≥0 razonables */ }
export function decToHex(n: number): string { /* mayúsculas opcional, consistente */ }
export function binToDec(s: string): number { /* validar entrada */ }
```

Añade al menos **8 casos de prueba** documentados al final del archivo o en comentarios.

### 4. Puente con permisos (30 min)

Explica `chmod 644` en binario (6 = rw-, etc.) en las notas.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Stallings | Sistemas numéricos, representación |
| Catálogo | [Bibliografía · M05](../../../bibliografia.md#m05-organizacion-de-computadoras) |


## Hecho cuando

1. Notas con 10 conversiones manuales + explicación chmod.
2. `conversiones.ts` con funciones y casos de prueba ejecutables.
3. Entiendes por qué hex agrupa bits de a 4.

## Errores comunes

- Usar `parseInt` sin validar strings inválidos.
- Confundir string binario con número JS.

## Siguiente

[L10 — Enteros, complemento a dos y overflow](L10-enteros-complemento-y-overflow.md)
