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
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Capa `validacion/` para argumentos CLI y refactor de al
      menos 3 funciones con nombres que revelan intención.


      La CLI crece. Sin validación y nombres claros, el archivo principal se
      vuelve inmantenible.
  - id: s2
    tipo: ejemplo
    titulo: 1. Validadores
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Validación y código legible" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: refactor nombres en habits + validadores en src/validacion/
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
      ¿Es buena práctica en esta lección? “Validar solo en CLI y no en funciones
      de dominio."
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
          Capa `validacion/` para argumentos CLI y refactor de al menos 3
          funciones con nombres que revelan intención.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Lectura Código limpio
    xp: 10
    cuerpo: >-
      Caps. 2–3: anota 5 reglas aplicables a tu CLI en
      `projects/m02-habits/NOTAS-CC.md`.
  - id: s7
    tipo: explicacion
    titulo: 3. Refactor
    xp: 10
    cuerpo: |-
      - Funciones ≤25 líneas donde sea razonable.
      - Renombra variables de una letra salvo bucles triviales.
      - Elimina duplicación entre `list` y futuro `stats`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - '`add` usa validador `Result`.'
      - '`NOTAS-CC.md` con reglas propias.'
      - '`done` marca hábito o fecha (mínimo viable).'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
