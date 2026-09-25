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

**En resumen:** modelas un dominio con tipos serios, refactorizas con Código limpio y empaquetas algo reutilizable.


## Objetivos

1. Encapsulación, composición vs herencia, interfaces.
2. Tipos avanzados útiles en TS (uniones, generics básicos).
3. Errores como parte del diseño.
4. Empaquetar y versionar una librería pequeña.

## Cómo estudiar esta materia

- Prefiere **composición** antes que jerarquías profundas.
- Cada refactor: tests en verde antes y después.
- Lee *Código limpio* en dosis de 30–45 min y aplícalo al código de M02.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| OO + tipos | 6–8 | Dominio + interfaces |
| Refactor CC | 6–8 | Diff antes/después |
| Lib + tests | 4–6 | `npm pack` local |
| Retro | 1 | Cuándo NO usar herencia |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h)

1. Elige un dominio simple: inventario o biblioteca.
2. Sin framework, modela en TS:
   ```ts
   interface Libro {
     id: string;
     titulo: string;
     prestado: boolean;
   }

   interface Biblioteca {
     agregar(libro: Libro): void;
     prestar(id: string): void;
   }
   ```
3. Implementa una clase `BibliotecaMemoria` con array interno.
4. Escribe 3 tests: agregar, prestar, prestar inexistente (debe fallar claro).
5. Lee el capítulo de nombres/funciones de *Código limpio*.

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

## Temario

| Semana | Temas |
|--------|-------|
| 1 | OO sólido: objetos, responsabilidades |
| 2 | Interfaces, composición, SOLID intro (S, O, D) |
| 3 | Generics, uniones, narrowing |
| 4 | Errores, Result pattern simple, logging |
| 5 | Empaquetado + proyecto |

## Lecturas

Canon: *Código limpio* (Martin, ed. ES) + *El programador pragmático* (Hunt & Thomas, ed. ES) + Handbook TS. Ver [bibliografía](../../bibliografia.md).

| Semana | Capítulos / secciones | Alternativa |
|--------|----------------------|-------------|
| 1 | CC **caps. 1–3** (limpio; nombres; funciones) + Pragmático **DRY / ortogonalidad** (temas equivalentes en tu ed.) | Refactor de un módulo tuyo aplicando solo nombres y funciones |
| 2 | CC **caps. 6 y 10** (objetos/estructuras; clases) + lectura corta SOLID S/O/D (artículo o resumen mentor) | Handbook TS *Object Types* |
| 3 | TS Handbook **Generics** + **Narrowing** (oficial) | Ejemplos oficiales del Handbook |
| 4 | CC **cap. 7** (errores) + patrón Result (notas M06 / ejemplo en repo) | Docs de errores en Node |
| 5 | CC **cap. 9** (pruebas) + empaquetado npm (`package.json`, semver, README) | Docs npm + Vitest |

**Regla:** cada capítulo de CC → un commit de refactor en `projects/m06-*` con el principio en el mensaje.

## Prácticas

1. **P1:** Dominio “biblioteca” o “inventario” solo con TS (sin Express).
2. **P2:** Antes/después de refactor; guarda el diff.
3. **P3:** Tests que cubran null, vacío, duplicados.

## Proyecto útil

Librería pequeña (validación o utilidades). README, semver, tests, ejemplo de uso. Aunque sea `npm pack` local, debe sentirse profesional.

## Errores comunes

- Herencia de 5 niveles “porque OOP”.
- Clases sin comportamiento (solo getters/setters vacíos).
- Tragar errores con `catch (e) {}`.
- Publicar sin README ni versión.

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
