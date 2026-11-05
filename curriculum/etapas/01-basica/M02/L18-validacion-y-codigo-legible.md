---
id: L18
materia: M02
orden: 18
titulo: Validación y código legible
horas: 3
semana: 5
lectura: Código limpio caps. 2–3 (nombres; funciones)
evidencia: refactor nombres en habits + validadores en src/validacion/
formato: pasos
xpLeccion: 96
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      La CLI crece. Sin validación y nombres claros, el archivo principal se
      vuelve inmantenible.


      **Objetivo de esta lección:** Capa `validacion/` para argumentos CLI y
      refactor de al menos 3 funciones con nombres que revelan intención.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Validadores
    xp: 10
    cuerpo: |-
      ```ts
      import { err, ok, type Result } from "../tipos/resultado.js";

      export function validarNombreHabito(raw: string): Result<string, string> {
        const t = raw.trim();
        if (t.length < 2) return err("el nombre debe tener al menos 2 caracteres");
        if (t.length > 80) return err("el nombre es demasiado largo");
        return ok(t);
      }
      ```

      `src/validacion/habito.ts`: Integra en `add`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Lectura Código limpio
    xp: 10
    cuerpo: |-
      ```ts
      import { err, ok, type Result } from "../tipos/resultado.js";

      export function validarNombreHabito(raw: string): Result<string, string> {
        const t = raw.trim();
        if (t.length < 2) return err("el nombre debe tener al menos 2 caracteres");
        if (t.length > 80) return err("el nombre es demasiado largo");
        return ok(t);
      }
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Validación y código legible», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: '`add` usa validador `Result`.'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Validación y código
          legible
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
      ¿Es recomendable en esta lección? “Validar solo en CLI y no en funciones
      de dominio."
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
          Capa `validacion/` para argumentos CLI y refactor de al menos 3
          funciones con nombres que revelan intención.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Refactor
    xp: 10
    cuerpo: >-
      - Funciones ≤25 líneas donde sea razonable. - Renombra variables de una
      letra salvo bucles triviales. - Elimina duplicación entre `list` y futuro
      `stats`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`add` usa validador `Result`.'
      - '`NOTAS-CC.md` con reglas propias.'
      - '`done` marca hábito o fecha (mínimo viable).'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L18 — Validación y código legible

**~3 h · Semana 5**

Validas entradas de comandos y aplicas *Código limpio* en nombres y tamaño de funciones.

## Objetivo

Capa `validacion/` para argumentos CLI y refactor de al menos 3 funciones con nombres que revelan intención.

## Por qué importa

La CLI crece. Sin validación y nombres claros, el archivo principal se vuelve inmantenible.

## Pasos

### 1. Validadores (50 min)

`src/validacion/habito.ts`:

```ts
import { err, ok, type Result } from "../tipos/resultado.js";

export function validarNombreHabito(raw: string): Result<string, string> {
  const t = raw.trim();
  if (t.length < 2) return err("el nombre debe tener al menos 2 caracteres");
  if (t.length > 80) return err("el nombre es demasiado largo");
  return ok(t);
}
```

Integra en `add`.

### 2. Lectura Código limpio (45 min)

Caps. 2–3: anota 5 reglas aplicables a tu CLI en `projects/m02-habits/NOTAS-CC.md`.

### 3. Refactor (60 min)

- Funciones ≤25 líneas donde sea razonable.
- Renombra variables de una letra salvo bucles triviales.
- Elimina duplicación entre `list` y futuro `stats`.

### 4. Comando `done` (25 min)

Esqueleto `done <id>` con validación de id existente.

## Lectura de esta lección

| Fuente | Qué leer |
|--------|----------|
| *Código limpio* | Caps. 2–3 (ed. ES) |
| Catálogo | [bibliografía](../../../bibliografia.md) |
| Catálogo | [Bibliografía · M02](../../../bibliografia.md#m02-programacion-i) |


## Hecho cuando

1. `add` usa validador `Result`.
2. `NOTAS-CC.md` con reglas propias.
3. `done` marca hábito o fecha (mínimo viable).

## Errores comunes

- Validar solo en CLI y no en funciones de dominio.
- Refactor cosmético sin cambiar comportamiento testeable.
- Nombres en inglés mezclados con mensajes en español sin criterio (elige: código EN, UX ES está bien).

## Siguiente

[L19 — Vitest: primeros tests](L19-vitest-primeros-tests.md)
