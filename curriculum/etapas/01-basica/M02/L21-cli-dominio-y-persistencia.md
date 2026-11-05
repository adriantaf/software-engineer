---
id: L21
materia: M02
orden: 21
titulo: CLI — dominio y persistencia
horas: 3
semana: 6
lectura: Repaso modelo Habito + separación capas
evidencia: m02-habits con src/dominio/ sin dependencia de console
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El proyecto final debe enseñarse en portafolio. Capas claras = mantenible
      y testeable.


      **Objetivo de esta lección:** Módulo `dominio/` con operaciones
      `agregarHabito`, `marcarHecho`, `listar` sobre `EstadoApp` sin `console`
      ni `fs`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Extraer dominio
    xp: 10
    cuerpo: >-
      ```ts

      import type { EstadoApp } from "../modelo/almacen.js";

      import { crearHabito } from "../modelo/habito.js";

      import { validarNombreHabito } from "../validacion/habito.js";


      export function agregarHabito(estado: EstadoApp, nombreRaw: string):
      EstadoApp {
        const v = validarNombreHabito(nombreRaw);
        if (!v.ok) throw new Error(v.error);
        const habito = crearHabito(v.value);
        return { ...estado, habitos: [...estado.habitos, habito] };
      }

      ```


      `src/dominio/operaciones.ts`: Implementa `marcarHechoPorId` y tests
      asociados.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Adaptador CLI
    xp: 10
    cuerpo: >-
      ```ts

      import type { EstadoApp } from "../modelo/almacen.js";

      import { crearHabito } from "../modelo/habito.js";

      import { validarNombreHabito } from "../validacion/habito.js";


      export function agregarHabito(estado: EstadoApp, nombreRaw: string):
      EstadoApp {
        const v = validarNombreHabito(nombreRaw);
        if (!v.ok) throw new Error(v.error);
        const habito = crearHabito(v.value);
        return { ...estado, habitos: [...estado.habitos, habito] };
      }

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «CLI — dominio y persistencia», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: >-
          `dominio/` sin imports de `fs` ni `process` (salvo tipos Node si
          unavoidable).
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de CLI — dominio y
          persistencia
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
    pregunta: ¿Es recomendable en esta lección? ““Dominio” que importa `cli.ts`."
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
          Módulo `dominio/` con operaciones `agregarHabito`, `marcarHecho`,
          `listar` sobre `EstadoApp` sin `console` ni `fs`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tests dominio
    xp: 10
    cuerpo: ≥3 tests nuevos sobre operaciones puras.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - >-
        `dominio/` sin imports de `fs` ni `process` (salvo tipos Node si
        unavoidable).
      - Tests dominio en verde.
      - Comandos previos siguen funcionando manualmente.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


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
