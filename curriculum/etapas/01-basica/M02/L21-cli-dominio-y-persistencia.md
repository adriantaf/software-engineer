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
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Módulo `dominio/` con operaciones `agregarHabito`,
      `marcarHecho`, `listar` sobre `EstadoApp` sin `console` ni `fs`.


      El proyecto final debe enseñarse en portafolio. Capas claras = mantenible
      y testeable.
  - id: s2
    tipo: ejemplo
    titulo: 1. Extraer dominio
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "CLI — dominio y persistencia" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: m02-habits con src/dominio/ sin dependencia de console
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
    pregunta: ¿Es buena práctica en esta lección? ““Dominio” que importa `cli.ts`."
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
          Módulo `dominio/` con operaciones `agregarHabito`, `marcarHecho`,
          `listar` sobre `EstadoApp` sin `console` ni `fs`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Adaptador CLI
    xp: 10
    cuerpo: '`cli.ts` solo parsea, llama dominio, imprime, guarda.'
  - id: s7
    tipo: explicacion
    titulo: 3. Tests dominio
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
