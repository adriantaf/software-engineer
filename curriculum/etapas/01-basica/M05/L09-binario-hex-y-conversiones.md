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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Convertir entre decimal, binario y hexadecimal; interpretar
      bytes como datos; implementar conversiones en TypeScript con tests
      manuales claros.


      Todo en la máquina es bits. Dominar conversiones evita errores en flags,
      permisos y protocolos.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```ts

      export function decToBin(n: number): string { /* solo enteros ≥0
      razonables */ }

      export function decToHex(n: number): string { /* mayúsculas opcional,
      consistente */ }

      export function binToDec(s: string): number { /* validar entrada */ }

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Binario, hex y conversiones" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m05-como-corre/conversiones.ts + notas-conversiones.md
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
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Usar `parseInt` sin validar strings
      inválidos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Convertir entre decimal, binario y hexadecimal; interpretar bytes como
          datos; implementar conversiones en TypeScript con tests manuales cla…
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `notas-conversiones.md`
    xp: 10
    cuerpo: >-
      Tabla de ejercicios resueltos (incluye permisos Unix `rwx` como ejemplo de
      bits).
  - id: s7
    tipo: ejemplo
    titulo: 3. Código `conversiones.ts`
    xp: 10
    cuerpo: >-
      ```ts

      export function decToBin(n: number): string { /* solo enteros ≥0
      razonables */ }

      export function decToHex(n: number): string { /* mayúsculas opcional,
      consistente */ }

      export function binToDec(s: string): number { /* validar entrada */ }

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Notas con 10 conversiones manuales + explicación chmod.
      - '`conversiones.ts` con funciones y casos de prueba ejecutables.'
      - Entiendes por qué hex agrupa bits de a 4.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
