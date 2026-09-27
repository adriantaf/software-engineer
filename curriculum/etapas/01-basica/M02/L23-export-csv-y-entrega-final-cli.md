---
id: L23
materia: M02
orden: 23
titulo: Export CSV y entrega final CLI
horas: 2.5
semana: 6
lectura: "— (foco proyecto + README)"
evidencia: "comando export --csv + README completo m02-habits"
---

# L23 — Export CSV y entrega final CLI

**~2.5 h · Semana 6**

Cierras funcionalidad: `export --csv` a archivo o stdout, README con ejemplos copy-paste, checklist de requisitos del proyecto.

## Objetivo

Exportación CSV de hábitos (id, nombre, # completados) y documentación que otra persona pueda seguir sin ti.

## Por qué importa

CSV es el puente hacia hojas de cálculo y análisis. El README es evidencia de comunicación técnica.

## Pasos

### 1. Generador CSV (50 min)

`src/dominio/exportar-csv.ts`:

```ts
import type { Habito } from "../modelo/habito.js";

export function habitosACsv(habitos: Habito[]): string {
  const header = "id,nombre,marcados";
  const rows = habitos.map(
    (h) => `${h.id},${escapeCsv(h.nombre)},${h.completados.length}`
  );
  return [header, ...rows].join("\n");
}

function escapeCsv(s: string): string {
  if (/[",\n]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
  return s;
}
```

### 2. Comando export (40 min)

`export --csv [ruta]` — si no hay ruta, imprime a stdout. Tests del escape CSV.

### 3. README final (50 min)

`projects/m02-habits/README.md`:

- Instalación
- Todos los comandos con ejemplos
- Dónde vive `data/habits.json`
- `npm test`

### 4. Verificación requisitos (20 min)

Tabla en README: add/list/done/stats/export ✓

## Lectura de esta lección

Opcional: EJ cap. 7 si buscas ideas de proyecto integrador.

## Hecho cuando

1. `export --csv` genera archivo válido abrible en Excel/LibreOffice.
2. README cumple requisitos mínimos de la ficha M02.
3. `npm test` sigue verde.

## Errores comunes

- CSV sin escapar comas en nombres.
- README sin comandos reales probados.
- Commitear CSV con datos personales.

## Siguiente

[L24 — Cierre M02 y evidencias](L24-cierre-m02-y-evidencias.md)
