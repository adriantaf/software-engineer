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
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un `index.ts` de 400 líneas es deuda. La semana 3 separa dominio, I/O y
      CLI.


      **Objetivo de esta lección:** Reorganizar katas/modelo en módulos ES
      (`"type": "module"`) y entender por qué los imports terminan en `.js`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Activar ESM
    xp: 10
    cuerpo: >-
      ```json

      {
        "type": "module",
        "scripts": {
          "build": "tsc",
          "start": "tsx src/cli/demo.ts"
        }
      }

      ```


      En `package.json`: Imports entre archivos TS usan extensión **`.js`** en
      el import (resolución NodeNext).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Barrel opcional
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Módulos ES en Node», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: '`npm run start` (o `tsx src/cli/demo.ts`) funciona tras el refactor.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Módulos ES en Node
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
      ¿Es recomendable en esta lección? “Olvidar `.js` en imports relativos con
      NodeNext."
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
          Reorganizar katas/modelo en módulos ES (`"type": "module"`) y entender
          por qué los imports terminan en `.js`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Mover CLI demo
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
