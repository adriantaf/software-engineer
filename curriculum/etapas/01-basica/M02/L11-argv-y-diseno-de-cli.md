---
id: L11
materia: M02
orden: 11
titulo: argv y diseño de CLI
horas: 2.5
semana: 3
lectura: "Node process.argv + diseño de comandos (add/list)"
evidencia: "projects/m02-habits/ creado con src/cli.ts parseando argv"
---

# L11 — argv y diseño de CLI

**~2.5 h · Semana 3**

Arrancas el **proyecto CLI** en `projects/m02-habits/`: parser mínimo de `process.argv` y comandos `add` / `list`.

## Objetivo

Crear el repo de la CLI, copiar/adaptar modelo e I/O, y enrutar subcomandos sin librerías pesadas todavía.

## Por qué importa

Desde la semana 3 el proyecto crece cada lección. No lo dejes para la semana 6.

## Pasos

### 1. Nuevo proyecto CLI (25 min)

```bash
mkdir -p projects/m02-habits/src
cd projects/m02-habits
npm init -y
npm install -D typescript tsx vitest @types/node
```

Misma base `tsconfig` strict que katas. `"type": "module"`.

### 2. Tipos de comando (35 min)

`src/comandos.ts`:

```ts
export type Comando =
  | { tipo: "add"; nombre: string }
  | { tipo: "list" }
  | { tipo: "help" };

export function parseArgv(argv: string[]): Comando {
  const [, , cmd, ...rest] = argv;
  if (cmd === "add") {
    const nombre = rest.join(" ").trim();
    if (!nombre) return { tipo: "help" };
    return { tipo: "add", nombre };
  }
  if (cmd === "list") return { tipo: "list" };
  return { tipo: "help" };
}
```

### 3. Entry `cli.ts` (50 min)

Carga estado, ejecuta comando, guarda. Mensajes de ayuda claros en español.

### 4. Enlace en evidencia (20 min)

Actualiza `projects/m02-programacion/README.md` con ruta a `m02-habits`.

### 5. Prueba manual (30 min)

```bash
npx tsx src/cli.ts add Leer 20 min
npx tsx src/cli.ts list
```

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Node.js | [process.argv](https://nodejs.org/api/process.html#processargv) |

## Hecho cuando

1. Existe `projects/m02-habits/` con `add` y `list` funcionales contra JSON local.
2. `parseArgv` es función pura testeable (prepara L19).
3. Commit en git del esqueleto CLI.

## Errores comunes

- Toda la lógica dentro del `if (cmd === "add")` del entry.
- No persistir tras `add`.
- Mensajes de error crípticos (“Error”).

## Siguiente

[L12 — Script JSON y reporte (P2)](L12-script-json-y-reporte-p2.md)
