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

## Análogos

- UABC: Lenguajes de Programación Orientada a Objetos
- Tec: Programación orientada a objetos

## Objetivos

1. Encapsulación, composición vs herencia, interfaces.
2. Tipos avanzados útiles en TS (uniones, generics básicos).
3. Errores como parte del diseño.
4. Empaquetar y versionar una librería pequeña.

## Cómo estudiar esta materia

- Prefiere **composición** antes que jerarquías profundas.
- Cada refactor: tests en verde antes y después.
- Lee *Código limpio* en dosis de 30–45 min y aplícalo al código de M02.

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

## Libros (español)

- *Código limpio* (Clean Code) — Robert C. Martin, ed. ES.
- *El programador pragmático* (ed. ES) — ortogonalidad y DRY (ligero).
- Docs TypeScript: generics / narrowing.

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

## Criterios de dominio (cierre Etapa Básica)

- [ ] Explicas cuándo NO usar herencia.
- [ ] Tu librería tiene API clara y tests.
- [ ] Revisas el código de M02 y señalas 5 mejoras concretas.
