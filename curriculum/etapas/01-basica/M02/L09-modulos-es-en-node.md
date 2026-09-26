---
id: L09
materia: M02
orden: 9
titulo: Módulos ES en Node
horas: 2.5
semana: 3
lectura: "EJ cap. 10 (módulos) + TS Handbook Modules"
evidencia: "src/ reorganizado con imports .js + package.json type module"
---

# L09 — Módulos ES en Node

**~2.5 h · Semana 3**

Partes el código en módulos con `import`/`export`, rutas explícitas y un árbol de carpetas que aguante la CLI.

## Objetivo

Reorganizar katas/modelo en módulos ES (`"type": "module"`) y entender por qué los imports terminan en `.js`.

## Por qué importa

Un `index.ts` de 400 líneas es deuda. La semana 3 separa dominio, I/O y CLI.

## Pasos

### 1. Activar ESM (20 min)

En `package.json`:

```json
{
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "tsx src/cli/demo.ts"
  }
}
```

Imports entre archivos TS usan extensión **`.js`** en el import (resolución NodeNext).

### 2. Barrel opcional (40 min)

`src/modelo/index.ts` reexporta `habito` y `almacen`. No abuses: solo donde simplifica.

### 3. Mover CLI demo (45 min)

`src/cli/demo.ts` importa `crearHabito` y `nombresOrdenados`, imprime un flujo mínimo.

### 4. EJ cap. 10 (50 min)

Lee módulos en EJ; refactoriza un ejercicio anterior a dos archivos.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 10 |
| TS Handbook | [Modules](https://www.typescriptlang.org/docs/handbook/2/modules.html) |
| MDN | [Módulos JS](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Modules) |

## Hecho cuando

1. `npm run start` (o `tsx src/cli/demo.ts`) funciona tras el refactor.
2. No hay imports circulares obvios (si los hay, documenta el arreglo).
3. Commit `refactor(m02): módulos ES`.

## Errores comunes

- Olvidar `.js` en imports relativos con NodeNext.
- Mezclar `require` y `import`.
- Barrel que reexporta todo y oculta dependencias.

## Siguiente

[L10 — Leer y escribir archivos con fs](L10-fs-leer-y-escribir.md)
