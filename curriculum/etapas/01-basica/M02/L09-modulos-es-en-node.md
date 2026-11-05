---
id: L09
materia: M02
orden: 9
titulo: Módulos ES en Node
horas: 2.5
semana: 3
lectura: EJ cap. 10 (módulos) + TS Handbook Modules
evidencia: src/ reorganizado con imports .js + package.json type module
formato: pasos
xpLeccion: 75
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Reorganizar katas/modelo en módulos ES (`"type": "module"`)
      y entender por qué los imports terminan en `.js`.


      Un `index.ts` de 400 líneas es deuda. La semana 3 separa dominio, I/O y
      CLI.
  - id: s2
    tipo: ejemplo
    titulo: 1. Activar ESM
    xp: 10
    cuerpo: |-
      ```json
      {
        "type": "module",
        "scripts": {
          "build": "tsc",
          "start": "tsx src/cli/demo.ts"
        }
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Módulos ES en Node" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/ reorganizado con imports .js + package.json type module
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
      ¿Es buena práctica en esta lección? “Olvidar `.js` en imports relativos
      con NodeNext."
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
          Reorganizar katas/modelo en módulos ES (`"type": "module"`) y entender
          por qué los imports terminan en `.js`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Barrel opcional
    xp: 10
    cuerpo: >-
      `src/modelo/index.ts` reexporta `habito` y `almacen`. No abuses: solo
      donde simplifica.
  - id: s7
    tipo: explicacion
    titulo: 3. Mover CLI demo
    xp: 10
    cuerpo: >-
      `src/cli/demo.ts` importa `crearHabito` y `nombresOrdenados`, imprime un
      flujo mínimo.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`npm run start` (o `tsx src/cli/demo.ts`) funciona tras el refactor.'
      - 'No hay imports circulares obvios (si los hay, documenta el arreglo).'
      - 'Commit `refactor(m02): módulos ES`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
