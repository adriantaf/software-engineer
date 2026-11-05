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
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      En trabajo real leerás JSON de terceros. P2 demuestra módulos + errores
      útiles sin UI.


      **Objetivo de esta lección:** Implementar `reporte.ts` independiente de la
      CLI de hábitos (puede leer un JSON de ventas, hábitos exportados o
      inventario ficticio).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Formato de entrada
    xp: 10
    cuerpo: >-
      ```json

      {
        "periodo": "2026-03",
        "items": [
          { "nombre": "alpha", "cantidad": 3 },
          { "nombre": "beta", "cantidad": 7 }
        ]
      }

      ```


      `data/ejemplo-reporte.json`: Define `interface EntradaReporte` en
      `src/scripts/tipos-reporte.ts`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Generador de reporte
    xp: 10
    cuerpo: >-
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


      `src/scripts/reporte.ts`: Entry: `npx tsx src/scripts/reporte.ts
      data/ejemplo-reporte.json`
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Script JSON y reporte (P2)», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: Reporte corre con el JSON de ejemplo.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Script JSON y reporte
          (P2)
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
      ¿Es recomendable en esta lección? “`catch` vacío o `console.log(e)` sin
      contexto."
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
          Implementar `reporte.ts` independiente de la CLI de hábitos (puede
          leer un JSON de ventas, hábitos exportados o inventario ficticio).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: README P2
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
