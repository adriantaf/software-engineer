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
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El JSON en disco debe mapear a tipos que el compilador entienda. Hoy
      diseñas ese contrato.


      **Objetivo de esta lección:** Esqueleto del dominio de la CLI: tipo
      `Habito`, validación mínima al crear, sin `any`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Modelo Habito
    xp: 10
    cuerpo: >-
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


      `src/modelo/habito.ts`: En versiones de Node sin `crypto.randomUUID`
      global, usa `import { randomUUID } from "node:crypto"`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Objetos anidados
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Objetos, interfaces y tipos», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`Habito` y `crearHabito` compilan; nombre vacío lanza error claro.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Objetos, interfaces y
          tipos
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
      ¿Es recomendable en esta lección? “`interface` y `type` duplicados para lo
      mismo sin criterio."
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
          Esqueleto del dominio de la CLI: tipo `Habito`, validación mínima al
          crear, sin `any`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: EJ cap. 4 ejercicios
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
