---
id: L06
materia: M02
orden: 6
titulo: 'Objetos, interfaces y tipos'
horas: 3
semana: 2
lectura: EJ cap. 4 (objetos) + TS Handbook Object Types
evidencia: src/modelo/habito.ts con interface Habito + factory tipada
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Esqueleto del dominio de la CLI: tipo `Habito`, validación
      mínima al crear, sin `any`.


      El JSON en disco debe mapear a tipos que el compilador entienda. Hoy
      diseñas ese contrato.
  - id: s2
    tipo: ejemplo
    titulo: 1. Modelo Habito
    xp: 10
    cuerpo: |-
      ```ts
      export interface Habito {
        id: string;
        nombre: string;
        creadoEn: string; // ISO 8601
        completados: string[]; // fechas ISO del día marcado done
        etiquetas?: string[];
      }

      export function crearHabito(nombre: string, ahora = new Date()): Habito {
        const limpio = nombre.trim();
        if (!limpio) throw new Error("nombre vacío");
        return {
          id: crypto.randomUUID(),
          nombre: limpio,
          creadoEn: ahora.toISOString(),
          completados: [],
        };
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Objetos, interfaces y tipos" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/modelo/habito.ts con interface Habito + factory tipada
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
      ¿Es buena práctica en esta lección? “`interface` y `type` duplicados para
      lo mismo sin criterio."
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
          Esqueleto del dominio de la CLI: tipo `Habito`, validación mínima al
          crear, sin `any`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Objetos anidados
    xp: 10
    cuerpo: >-
      `src/modelo/almacen.ts` — tipo `EstadoApp { habitos: Habito[]; version:
      number }` con `estadoVacio(): EstadoApp`.
  - id: s7
    tipo: explicacion
    titulo: 3. EJ cap. 4 ejercicios
    xp: 10
    cuerpo: ≥2 ejercicios del capítulo en TS.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`Habito` y `crearHabito` compilan; nombre vacío lanza error claro.'
      - '`EstadoApp` definido para uso futuro en la CLI.'
      - 'Commit `feat(m02): modelo Habito`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L06 — Objetos, interfaces y tipos

**~3 h · Semana 2**

Defines **formas** de datos con `interface` y `type`, campos opcionales y funciones que construyen objetos válidos.

## Objetivo

Esqueleto del dominio de la CLI: tipo `Habito`, validación mínima al crear, sin `any`.

## Por qué importa

El JSON en disco debe mapear a tipos que el compilador entienda. Hoy diseñas ese contrato.

## Pasos

### 1. Modelo Habito (50 min)

`src/modelo/habito.ts`:

```ts
export interface Habito {
  id: string;
  nombre: string;
  creadoEn: string; // ISO 8601
  completados: string[]; // fechas ISO del día marcado done
  etiquetas?: string[];
}

export function crearHabito(nombre: string, ahora = new Date()): Habito {
  const limpio = nombre.trim();
  if (!limpio) throw new Error("nombre vacío");
  return {
    id: crypto.randomUUID(),
    nombre: limpio,
    creadoEn: ahora.toISOString(),
    completados: [],
  };
}
```

En versiones de Node sin `crypto.randomUUID` global, usa `import { randomUUID } from "node:crypto"`.

### 2. Objetos anidados (40 min)

`src/modelo/almacen.ts` — tipo `EstadoApp { habitos: Habito[]; version: number }` con `estadoVacio(): EstadoApp`.

### 3. EJ cap. 4 ejercicios (40 min)

≥2 ejercicios del capítulo en TS.

### 4. Katas (30 min)

Dos katas más; apunta total hacia 12.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Eloquent JavaScript* | Cap. 4 (objetos) |
| TS Handbook | [Object Types](https://www.typescriptlang.org/docs/handbook/2/objects.html) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `Habito` y `crearHabito` compilan; nombre vacío lanza error claro.
2. `EstadoApp` definido para uso futuro en la CLI.
3. Commit `feat(m02): modelo Habito`.

## Errores comunes

- `interface` y `type` duplicados para lo mismo sin criterio.
- Fechas como `Date` en JSON (serialización dolorosa) — aquí usamos string ISO a propósito.
- Objetos literales con campos de más sin error (activa excess property checks mentalmente).

## Siguiente

[L07 — map, filter y reduce](L07-map-filter-y-reduce.md)
