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
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Desde la semana 3 el proyecto crece cada lección. No lo dejes para la
      semana 6.


      **Objetivo de esta lección:** Crear el repo de la CLI, copiar/adaptar
      modelo e I/O, y enrutar subcomandos sin librerías pesadas todavía.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Nuevo proyecto CLI
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m02-habits/src
      cd projects/m02-habits
      npm init -y
      npm install -D typescript tsx vitest @types/node
      ```

      Misma base `tsconfig` strict que katas. `"type": "module"`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Tipos de comando
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

      `src/comandos.ts`:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «argv y diseño de CLI», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: >-
          Existe `projects/m02-habits/` con `add` y `list` funcionales contra
          JSON local.
      - id: b
        texto: Instalar herramientas al azar sin evidencia de argv y diseño de CLI
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `mkdir -p projects/m02-habits/src`
    comandoEsperado:
      - mkdir -p projects/m02-habits/src
      - cd projects/m02-habits
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m02-habits/src'
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
          Crear el repo de la CLI, copiar/adaptar modelo e I/O, y enrutar
          subcomandos sin librerías pesadas todavía.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Entry `cli.ts`
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
