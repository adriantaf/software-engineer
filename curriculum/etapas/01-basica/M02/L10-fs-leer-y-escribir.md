---
id: L10
materia: M02
orden: 10
titulo: Leer y escribir archivos con fs
horas: 3
semana: 3
lectura: 'Node.js docs — fs/promises, path'
evidencia: src/io/archivo-json.ts con load/save EstadoApp
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Implementar `loadEstado` / `saveEstado` para `EstadoApp` en
      un archivo bajo `data/`.


      La CLI de hábitos vive entre ejecuciones gracias a un JSON en disco. Hoy
      construyes esa capa.
  - id: s2
    tipo: ejemplo
    titulo: 1. Rutas seguras
    xp: 10
    cuerpo: |-
      ```ts
      import path from "node:path";

      export function rutaDatos(nombreArchivo: string): string {
        return path.join(process.cwd(), "data", nombreArchivo);
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Leer y escribir archivos con fs" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/io/archivo-json.ts con load/save EstadoApp
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
      ¿Es buena práctica en esta lección? “`JSON.parse` sin try/catch en
      archivos corruptos (anota TODO para semana 5)."
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
          Implementar `loadEstado` / `saveEstado` para `EstadoApp` en un archivo
          bajo `data/`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Load / save
    xp: 10
    cuerpo: |-
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
  - id: s7
    tipo: explicacion
    titulo: 3. Script de prueba
    xp: 10
    cuerpo: '`src/io/archivo-json-demo.ts` crea hábito, guarda, recarga, verifica.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`loadEstado` devuelve estado vacío si no hay archivo.'
      - '`saveEstado` crea `data/habits.json` legible.'
      - Demo ejecutado al menos una vez con salida verificada.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
