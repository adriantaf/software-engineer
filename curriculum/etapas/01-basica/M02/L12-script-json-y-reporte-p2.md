---
id: L12
materia: M02
orden: 12
titulo: Script JSON y reporte (P2)
horas: 3
semana: 3
lectura: Repaso módulos + manejo archivo faltante
evidencia: projects/m02-katas/src/scripts/reporte.ts + README P2
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `reporte.ts` independiente de la CLI de hábitos
      (puede leer un JSON de ventas, hábitos exportados o inventario ficticio).


      En trabajo real leerás JSON de terceros. P2 demuestra módulos + errores
      útiles sin UI.
  - id: s2
    tipo: ejemplo
    titulo: 1. Formato de entrada
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Script JSON y reporte (P2)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: projects/m02-katas/src/scripts/reporte.ts + README P2
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
      ¿Es buena práctica en esta lección? “`catch` vacío o `console.log(e)` sin
      contexto."
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
          Implementar `reporte.ts` independiente de la CLI de hábitos (puede
          leer un JSON de ventas, hábitos exportados o inventario ficticio).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Generador de reporte
    xp: 10
    cuerpo: |-
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
  - id: s7
    tipo: explicacion
    titulo: 3. README P2
    xp: 10
    cuerpo: >-
      En `projects/m02-katas/README.md` sección **P2** con comando, ejemplo de
      salida y comportamiento archivo faltante.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - Reporte corre con el JSON de ejemplo.
      - Ruta inexistente → mensaje claro y código de salida ≠ 0.
      - Evidencia P2 documentada para marcar en la UI cuando revises la ficha.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
