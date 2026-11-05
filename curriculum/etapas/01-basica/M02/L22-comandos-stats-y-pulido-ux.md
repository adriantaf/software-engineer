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
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Comando `stats` con totales (hábitos activos, marcados en la
      semana o total) y UX de `list`/`help` digna de demo.


      Requisitos mínimos del proyecto incluyen `stats`. La diferencia entre
      “funciona” y “usable” está en los detalles de salida.
  - id: s2
    tipo: ejemplo
    titulo: 1. stats
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Comandos stats y pulido UX" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: comandos stats + list legible + help actualizado
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
      ¿Es buena práctica en esta lección? “Stats que releen disco en bucle
      innecesario."
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
          Comando `stats` con totales (hábitos activos, marcados en la semana o
          total) y UX de `list`/`help` digna de demo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. list mejorado
    xp: 10
    cuerpo: 'Orden alfabético, indicador hecho/pendiente, ids acortados si hace falta.'
  - id: s7
    tipo: explicacion
    titulo: 3. help
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
