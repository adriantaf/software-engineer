---
id: L21
materia: M02
orden: 21
titulo: CLI — dominio y persistencia
horas: 3
semana: 6
lectura: "Repaso modelo Habito + separación capas"
evidencia: "m02-habits con src/dominio/ sin dependencia de console"
---

# L21 — CLI: dominio y persistencia

**~3 h · Semana 6**

Separas **dominio** (reglas) de **adaptadores** (CLI, fs). La persistencia queda detrás de una interfaz clara.

## Objetivo

Módulo `dominio/` con operaciones `agregarHabito`, `marcarHecho`, `listar` sobre `EstadoApp` sin `console` ni `fs`.

## Por qué importa

El proyecto final debe enseñarse en portafolio. Capas claras = mantenible y testeable.

## Pasos

### 1. Extraer dominio (70 min)

`src/dominio/operaciones.ts`:

```ts
import type { EstadoApp } from "../modelo/almacen.js";
import { crearHabito } from "../modelo/habito.js";
import { validarNombreHabito } from "../validacion/habito.js";

export function agregarHabito(estado: EstadoApp, nombreRaw: string): EstadoApp {
  const v = validarNombreHabito(nombreRaw);
  if (!v.ok) throw new Error(v.error);
  const habito = crearHabito(v.value);
  return { ...estado, habitos: [...estado.habitos, habito] };
}
```

Implementa `marcarHechoPorId` y tests asociados.

### 2. Adaptador CLI (50 min)

`cli.ts` solo parsea, llama dominio, imprime, guarda.

### 3. Tests dominio (50 min)

≥3 tests nuevos sobre operaciones puras.

### 4. README proyecto (20 min)

Diagrama texto: CLI → dominio → io.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Código limpio* | Repaso cap. 3 (funciones pequeñas) |

## Hecho cuando

1. `dominio/` sin imports de `fs` ni `process` (salvo tipos Node si unavoidable).
2. Tests dominio en verde.
3. Comandos previos siguen funcionando manualmente.

## Errores comunes

- “Dominio” que importa `cli.ts`.
- Estado global mutable fuera de `EstadoApp`.
- Saltarse tests al mover archivos.

## Siguiente

[L22 — Comandos stats y pulido UX](L22-comandos-stats-y-pulido-ux.md)
