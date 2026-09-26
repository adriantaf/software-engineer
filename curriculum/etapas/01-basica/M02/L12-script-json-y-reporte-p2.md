---
id: L12
materia: M02
orden: 12
titulo: Script JSON y reporte (P2)
horas: 3
semana: 3
lectura: "Repaso módulos + manejo archivo faltante"
evidencia: "projects/m02-katas/src/scripts/reporte.ts + README P2"
---

# L12 — Script JSON y reporte (P2)

**~3 h · Semana 3**

Entregas la **práctica P2**: script que lee un JSON de entrada, genera un reporte en consola y falla con mensaje claro si el archivo no existe.

## Objetivo

Implementar `reporte.ts` independiente de la CLI de hábitos (puede leer un JSON de ventas, hábitos exportados o inventario ficticio).

## Por qué importa

En trabajo real leerás JSON de terceros. P2 demuestra módulos + errores útiles sin UI.

## Pasos

### 1. Formato de entrada (30 min)

`data/ejemplo-reporte.json`:

```json
{
  "periodo": "2026-03",
  "items": [
    { "nombre": "alpha", "cantidad": 3 },
    { "nombre": "beta", "cantidad": 7 }
  ]
}
```

Define `interface EntradaReporte` en `src/scripts/tipos-reporte.ts`.

### 2. Generador de reporte (60 min)

`src/scripts/reporte.ts`:

```ts
import { readFile } from "node:fs/promises";
import path from "node:path";
import type { EntradaReporte } from "./tipos-reporte.js";

export function formatearReporte(data: EntradaReporte): string {
  const total = data.items.reduce((s, i) => s + i.cantidad, 0);
  const lineas = data.items.map((i) => `  - ${i.nombre}: ${i.cantidad}`);
  return [`Reporte ${data.periodo}`, `Total unidades: ${total}`, ...lineas].join("\n");
}

export async function main(rutaRelativa: string): Promise<void> {
  const ruta = path.resolve(process.cwd(), rutaRelativa);
  try {
    const raw = await readFile(ruta, "utf8");
    const data = JSON.parse(raw) as EntradaReporte;
    console.log(formatearReporte(data));
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code === "ENOENT") {
      console.error(`No se encontró el archivo: ${ruta}`);
      process.exitCode = 1;
      return;
    }
    throw e;
  }
}
```

Entry: `npx tsx src/scripts/reporte.ts data/ejemplo-reporte.json`

### 3. README P2 (25 min)

En `projects/m02-katas/README.md` sección **P2** con comando, ejemplo de salida y comportamiento archivo faltante.

### 4. Cierre semana 3 (30 min)

Bitácora: CLI + P2 estado; katas ≥17 si puedes.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Repaso cap. 10 si el refactor de módulos fue flojo |

## Hecho cuando

1. Reporte corre con el JSON de ejemplo.
2. Ruta inexistente → mensaje claro y código de salida ≠ 0.
3. Evidencia P2 documentada para marcar en la UI cuando revises la ficha.

## Errores comunes

- `catch` vacío o `console.log(e)` sin contexto.
- Mezclar P2 dentro de la CLI de hábitos sin separación.
- No probar el caso ENOENT.

## Siguiente

[L13 — Promises y el modelo mental async](L13-promises-y-modelo-mental.md)
