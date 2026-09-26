---
id: L06
materia: M02
orden: 6
titulo: Objetos, interfaces y tipos
horas: 3
semana: 2
lectura: "EJ cap. 4 (objetos) + TS Handbook Object Types"
evidencia: "src/modelo/habito.ts con interface Habito + factory tipada"
---

# L06 — Objetos, interfaces y tipos

**~3 h · Semana 2**

Defines **formas** de datos con `interface` y `type`, campos opcionales y funciones que construyen objetos válidos.

## Objetivo

Esqueleto del dominio de la CLI: tipo `Habito`, validación mínima al crear, sin `any`.

## Por qué importa

El JSON en disco debe mapear a tipos que el compilador entienda. Hoy diseñas ese contrato.

## Pasos

### 1. Modelo Habito (50 min)

`src/modelo/habito.ts`:

```ts
export interface Habito {
  id: string;
  nombre: string;
  creadoEn: string; // ISO 8601
  completados: string[]; // fechas ISO del día marcado done
  etiquetas?: string[];
}

export function crearHabito(nombre: string, ahora = new Date()): Habito {
  const limpio = nombre.trim();
  if (!limpio) throw new Error("nombre vacío");
  return {
    id: crypto.randomUUID(),
    nombre: limpio,
    creadoEn: ahora.toISOString(),
    completados: [],
  };
}
```

En versiones de Node sin `crypto.randomUUID` global, usa `import { randomUUID } from "node:crypto"`.

### 2. Objetos anidados (40 min)

`src/modelo/almacen.ts` — tipo `EstadoApp { habitos: Habito[]; version: number }` con `estadoVacio(): EstadoApp`.

### 3. EJ cap. 4 ejercicios (40 min)

≥2 ejercicios del capítulo en TS.

### 4. Katas (30 min)

Dos katas más; apunta total hacia 12.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 4 (objetos) |
| TS Handbook | [Object Types](https://www.typescriptlang.org/docs/handbook/2/objects.html) |

## Hecho cuando

1. `Habito` y `crearHabito` compilan; nombre vacío lanza error claro.
2. `EstadoApp` definido para uso futuro en la CLI.
3. Commit `feat(m02): modelo Habito`.

## Errores comunes

- `interface` y `type` duplicados para lo mismo sin criterio.
- Fechas como `Date` en JSON (serialización dolorosa) — aquí usamos string ISO a propósito.
- Objetos literales con campos de más sin error (activa excess property checks mentalmente).

## Siguiente

[L07 — map, filter y reduce](L07-map-filter-y-reduce.md)
