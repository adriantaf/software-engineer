---
id: L11
materia: M02
orden: 11
titulo: argv y diseño de CLI
horas: 2.5
semana: 3
lectura: Node process.argv + diseño de comandos (add/list)
evidencia: projects/m02-habits/ creado con src/cli.ts parseando argv
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear el repo de la CLI, copiar/adaptar modelo e I/O, y
      enrutar subcomandos sin librerías pesadas todavía.


      Desde la semana 3 el proyecto crece cada lección. No lo dejes para la
      semana 6.
  - id: s2
    tipo: ejemplo
    titulo: 1. Nuevo proyecto CLI
    xp: 10
    cuerpo: |-
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "argv y diseño de CLI" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: projects/m02-habits/ creado con src/cli.ts parseando argv
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `mkdir -p projects/m02-habits/src`
    comandoEsperado:
      - mkdir -p projects/m02-habits/src
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m02-habits/src'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Crear el repo de la CLI, copiar/adaptar modelo e I/O, y enrutar
          subcomandos sin librerías pesadas todavía.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Tipos de comando
    xp: 10
    cuerpo: |-
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
  - id: s7
    tipo: explicacion
    titulo: 3. Entry `cli.ts`
    xp: 10
    cuerpo: >-
      Carga estado, ejecuta comando, guarda. Mensajes de ayuda claros en
      español.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        Existe `projects/m02-habits/` con `add` y `list` funcionales contra JSON
        local.
      - '`parseArgv` es función pura testeable (prepara L19).'
      - Commit en git del esqueleto CLI.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
