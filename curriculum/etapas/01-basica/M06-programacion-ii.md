---
id: M06
titulo: Programación II (OO, tipos y errores)
etapa: basica
orden: 6
semanas: 5
horas: 100
practicas:
  - id: p1
    titulo: Modelar un dominio con clases/interfaces (sin framework)
  - id: p2
    titulo: Refactor a Código limpio (nombres, funciones pequeñas)
  - id: p3
    titulo: Manejo de errores tipado + tests de borde
proyecto:
  id: proj
  titulo: Librería reutilizable publicada (npm local o GitHub package)
---

# M06 — Programación II (OO, tipos y errores)

## Por qué existe

Cierras la etapa básica escribiendo código que otro ingeniero (o tú en 6 meses) pueda mantener.

**En resumen:** modelas un dominio con tipos serios, refactorizas con *Código limpio* y empaquetas algo reutilizable.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Modelar un dominio con encapsulación, composición e interfaces (sin frameworks web).
2. Aplicar principios de diseño legible (nombres, funciones pequeñas, responsabilidades claras).
3. Usar tipos avanzados útiles en TS (uniones, narrowing, generics básicos) y errores como parte del diseño.
4. Empaquetar, versionar y documentar una librería pequeña con tests.

## Cómo estudiar esta materia (piloto de lecciones)

M06 sigue el formato de lecciones cortas y completas (como M01): marcas una a una cuando cumples “Hecho cuando”.

1. Abre las lecciones **en orden** (L01 → L20).
2. Cada lección trae objetivo, pasos, lectura y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. Las **prácticas / proyecto** exigen evidencia en `projects/m06-programacion-ii/` (o prefijo `m06-*` acordado).
5. Prefiere **composición** antes que jerarquías profundas. Cada refactor: tests en verde antes y después.
6. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| OO + tipos | 6–8 | L01–L08, dominio + interfaces |
| Refactor + TS avanzado | 6–8 | L09–L12, generics y narrowing |
| Errores + tests | 6–8 | L13–L16, Result y bordes |
| Lib + cierre | 4–6 | L17–L20, `npm pack` y README |
| Retro | 1 | Cuándo NO usar herencia |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Objetos, responsabilidades y estilo (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Dominio inicial y entorno del proyecto](M06/L01-dominio-inicial-y-entorno.md) | 5 |
| L02 | [Objetos con comportamiento real](M06/L02-objetos-con-comportamiento-real.md) | 5 |
| L03 | [Encapsulación en TypeScript](M06/L03-encapsulacion-en-typescript.md) | 5 |
| L04 | [Nombres y funciones pequeñas (CC 1–3)](M06/L04-nombres-y-funciones-cc-1-3.md) | 5 |

### Semana 2 — Interfaces, composición y SOLID intro (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Interfaces y contratos de dominio](M06/L05-interfaces-y-contratos.md) | 5 |
| L06 | [Composición frente a herencia](M06/L06-composicion-frente-a-herencia.md) | 5 |
| L07 | [SOLID intro: S, O y D](M06/L07-solid-intro-s-o-d.md) | 5 |
| L08 | [Refactor documentado (P2)](M06/L08-refactor-documentado-p2.md) | 5 |

### Semana 3 — Uniones, narrowing y generics (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L09 | [Union types y modelado de estados](M06/L09-union-types-y-estados.md) | 5 |
| L10 | [Narrowing y type guards](M06/L10-narrowing-y-type-guards.md) | 5 |
| L11 | [Generics: funciones y contenedores](M06/L11-generics-funciones-y-contenedores.md) | 5 |
| L12 | [Generics en APIs del dominio](M06/L12-generics-en-apis-del-dominio.md) | 5 |

### Semana 4 — Errores, Result y tests de borde (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L13 | [Errores como diseño (CC cap. 7)](M06/L13-errores-como-diseno.md) | 5 |
| L14 | [Patrón Result tipado](M06/L14-patron-result-tipado.md) | 5 |
| L15 | [Tests de borde: null, vacío, duplicados (P3)](M06/L15-tests-de-borde-p3.md) | 5 |
| L16 | [Logging, diagnóstico y contratos de error](M06/L16-logging-y-diagnostico.md) | 5 |

### Semana 5 — Empaquetado y librería (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L17 | [Estructura de paquete npm](M06/L17-estructura-paquete-npm.md) | 5 |
| L18 | [Semver, scripts y build](M06/L18-semver-scripts-y-build.md) | 5 |
| L19 | [README, API pública y ejemplos](M06/L19-readme-api-y-ejemplos.md) | 5 |
| L20 | [Librería final y cierre de etapa básica](M06/L20-libreria-final-y-cierre.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *Código limpio* (Martin, ed. ES) + *El programador pragmático* (Hunt & Thomas, ed. ES) + [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html). Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / secciones |
|--------|-----------|----------------------|
| 1 | L01–L04 | CC **caps. 1–3** + Pragmático **DRY / ortogonalidad** |
| 2 | L05–L08 | CC **caps. 6 y 10** + SOLID S/O/D (resumen mentor) + Handbook *Object Types* |
| 3 | L09–L12 | Handbook **Generics** + **Narrowing** |
| 4 | L13–L16 | CC **cap. 7** + patrón Result + docs de errores en Node |
| 5 | L17–L20 | CC **cap. 9** + empaquetado npm + Vitest |

**Regla:** cada capítulo de CC aplicado → un commit de refactor con el principio en el mensaje.

## Ejemplo — Result simple para errores

```ts
type Ok<T> = { ok: true; value: T };
type Err = { ok: false; error: string };
export type Result<T> = Ok<T> | Err;

export function prestar(libro: { prestado: boolean }): Result<void> {
  if (libro.prestado) return { ok: false, error: "Ya prestado" };
  libro.prestado = true;
  return { ok: true, value: undefined };
}
```

## Prácticas

1. **P1:** Dominio “biblioteca” o “inventario” solo con TS (sin Express) — L01–L07.
2. **P2:** Antes/después de refactor; guarda el diff — L08.
3. **P3:** Tests que cubran null, vacío, duplicados — L15.

## Proyecto útil

Librería pequeña (validación o utilidades del dominio). README, semver, tests, ejemplo de uso. Aunque sea `npm pack` local, debe sentirse profesional (L17–L20).

## Errores comunes

- Herencia de 5 niveles “porque OOP”.
- Clases sin comportamiento (solo getters/setters vacíos).
- Tragar errores con `catch (e) {}`.
- Publicar sin README ni versión.
- Marcar lecciones sin cumplir “Hecho cuando”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Dominio:** `projects/m06-*` con modelo TS (sin Express).
- **P2 — Refactor:** Commit/diff mostrando nombres y funciones pequeñas.
- **P3 — Bordes:** Tests de null, vacío, duplicados.
- **Proyecto — Librería:** README, semver, tests, ejemplo de uso.

## Criterios de dominio (cierre Etapa Básica)

- [ ] Explicas cuándo NO usar herencia.
- [ ] Tu librería tiene API clara y tests.
- [ ] Revisas el código de M02 y señalas 5 mejoras concretas.
