---
id: L22
materia: M02
orden: 22
titulo: Comandos stats y pulido UX
horas: 3
semana: 6
lectura: — (foco proyecto)
evidencia: comandos stats + list legible + help actualizado
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Requisitos mínimos del proyecto incluyen `stats`. La diferencia entre
      “funciona” y “usable” está en los detalles de salida.


      **Objetivo de esta lección:** Comando `stats` con totales (hábitos
      activos, marcados en la semana o total) y UX de `list`/`help` digna de
      demo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: stats
    xp: 10
    cuerpo: |-
      ```ts
      import type { Habito } from "../modelo/habito.js";

      export function resumen(habitos: Habito[]): {
        totalHabitos: number;
        totalMarcados: number;
      } {
        return {
          totalHabitos: habitos.length,
          totalMarcados: habitos.reduce((s, h) => s + h.completados.length, 0),
        };
      }
      ```

      `src/dominio/estadisticas.ts`: CLI imprime formato fijo multi-línea.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: list mejorado
    xp: 10
    cuerpo: |-
      ```ts
      import type { Habito } from "../modelo/habito.js";

      export function resumen(habitos: Habito[]): {
        totalHabitos: number;
        totalMarcados: number;
      } {
        return {
          totalHabitos: habitos.length,
          totalMarcados: habitos.reduce((s, h) => s + h.completados.length, 0),
        };
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Comandos stats y pulido UX», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `stats` y `list` documentados en README con captura de salida (texto
          pegado).
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Comandos stats y pulido
          UX
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
      ¿Es recomendable en esta lección? “Stats que releen disco en bucle
      innecesario."
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
          Comando `stats` con totales (hábitos activos, marcados en la semana o
          total) y UX de `list`/`help` digna de demo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: help
    xp: 10
    cuerpo: Texto de ayuda con todos los comandos actuales y ejemplo por línea.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `stats` y `list` documentados en README con captura de salida (texto
        pegado).
      - '`help` lista `add`, `list`, `done`, `stats`.'
      - Tests stats en verde.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L22 — Comandos stats y pulido UX

**~3 h · Semana 6**

Implementas `stats` y mejoras de salida: tablas simples, mensajes de ayuda, códigos de salida coherentes.

## Objetivo

Comando `stats` con totales (hábitos activos, marcados en la semana o total) y UX de `list`/`help` digna de demo.

## Por qué importa

Requisitos mínimos del proyecto incluyen `stats`. La diferencia entre “funciona” y “usable” está en los detalles de salida.

## Pasos

### 1. stats (60 min)

`src/dominio/estadisticas.ts`:

```ts
import type { Habito } from "../modelo/habito.js";

export function resumen(habitos: Habito[]): {
  totalHabitos: number;
  totalMarcados: number;
} {
  return {
    totalHabitos: habitos.length,
    totalMarcados: habitos.reduce((s, h) => s + h.completados.length, 0),
  };
}
```

CLI imprime formato fijo multi-línea.

### 2. list mejorado (45 min)

Orden alfabético, indicador hecho/pendiente, ids acortados si hace falta.

### 3. help (30 min)

Texto de ayuda con todos los comandos actuales y ejemplo por línea.

### 4. Tests stats (45 min)

Tests de `resumen` con fixtures en memoria.

## Lectura de esta lección

Sin capítulo nuevo. Opcional: EJ cap. 7 (proyecto robot) como inspiración de estructura.

## Hecho cuando

1. `stats` y `list` documentados en README con captura de salida (texto pegado).
2. `help` lista `add`, `list`, `done`, `stats`.
3. Tests stats en verde.

## Errores comunes

- Stats que releen disco en bucle innecesario.
- Formato distinto en cada comando (inconsistencia visual).
- Olvidar actualizar help al añadir flags.

## Siguiente

[L23 — Export CSV y entrega final CLI](L23-export-csv-y-entrega-final-cli.md)
