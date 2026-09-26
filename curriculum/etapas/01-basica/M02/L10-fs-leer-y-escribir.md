---
id: L10
materia: M02
orden: 10
titulo: Leer y escribir archivos con fs
horas: 3
semana: 3
lectura: "Node.js docs — fs/promises, path"
evidencia: "src/io/archivo-json.ts con load/save EstadoApp"
---

# L10 — Leer y escribir archivos con fs

**~3 h · Semana 3**

Persistencia local con `fs/promises` y `path`: leer JSON, validar forma básica, escribir atomically-ish.

## Objetivo

Implementar `loadEstado` / `saveEstado` para `EstadoApp` en un archivo bajo `data/`.

## Por qué importa

La CLI de hábitos vive entre ejecuciones gracias a un JSON en disco. Hoy construyes esa capa.

## Pasos

### 1. Rutas seguras (30 min)

`src/io/rutas.ts`:

```ts
import path from "node:path";

export function rutaDatos(nombreArchivo: string): string {
  return path.join(process.cwd(), "data", nombreArchivo);
}
```

Crea `data/.gitkeep` y documenta en README que `habits.json` es local.

### 2. Load / save (60 min)

`src/io/archivo-json.ts`:

```ts
import { readFile, writeFile, mkdir } from "node:fs/promises";
import type { EstadoApp } from "../modelo/almacen.js";
import { rutaDatos } from "./rutas.js";

const ARCHIVO = "habits.json";

export async function loadEstado(): Promise<EstadoApp> {
  const ruta = rutaDatos(ARCHIVO);
  try {
    const raw = await readFile(ruta, "utf8");
    return JSON.parse(raw) as EstadoApp;
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code === "ENOENT") {
      return { habitos: [], version: 1 };
    }
    throw e;
  }
}

export async function saveEstado(estado: EstadoApp): Promise<void> {
  const ruta = rutaDatos(ARCHIVO);
  await mkdir(path.dirname(ruta), { recursive: true });
  await writeFile(ruta, JSON.stringify(estado, null, 2), "utf8");
}
```

(Añade `import path from "node:path"` donde haga falta.)

### 3. Script de prueba (40 min)

`src/io/archivo-json-demo.ts` crea hábito, guarda, recarga, verifica.

### 4. Node docs (40 min)

Lee `fs/promises` y `path` en la documentación oficial de Node.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| Node.js | [fs/promises](https://nodejs.org/api/fs.html#promises-api) |
| Node.js | [path](https://nodejs.org/api/path.html) |

## Hecho cuando

1. `loadEstado` devuelve estado vacío si no hay archivo.
2. `saveEstado` crea `data/habits.json` legible.
3. Demo ejecutado al menos una vez con salida verificada.

## Errores comunes

- `JSON.parse` sin try/catch en archivos corruptos (anota TODO para semana 5).
- Rutas relativas al archivo `.ts` en vez de `cwd` del proyecto.
- Commitear `habits.json` con datos personales.

## Siguiente

[L11 — argv y diseño de CLI](L11-argv-y-diseno-de-cli.md)
