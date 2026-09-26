---
id: L22
materia: M02
orden: 22
titulo: Comandos stats y pulido UX
horas: 3
semana: 6
lectura: "— (foco proyecto)"
evidencia: "comandos stats + list legible + help actualizado"
---

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
