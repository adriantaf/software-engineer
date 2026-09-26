---
id: L18
materia: M02
orden: 18
titulo: Validación y código legible
horas: 3
semana: 5
lectura: "Código limpio caps. 2–3 (nombres; funciones)"
evidencia: "refactor nombres en habits + validadores en src/validacion/"
---

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
