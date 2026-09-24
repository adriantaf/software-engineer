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
- *El programador pragmático* (ed. ES) — capítulos de ortogonalidad y DRY (lectura ligera).
- Docs TypeScript: generics / narrowings.

## Prácticas

1. **P1:** Dominio “biblioteca” o “inventario” solo con TS (sin Express).
2. **P2:** Antes/después de refactor; captura el diff.
3. **P3:** Tests que cubran null, vacío, duplicados, permisos.

## Proyecto útil

Publica una librería pequeña (por ejemplo validación de formularios o utilidades de fechas locales MX). README, semver, tests, ejemplo de uso. Aunque sea `npm pack` local, debe sentirse profesional.

## Criterios de dominio (cierre Etapa Básica)

- [ ] Explicas cuándo NO usar herencia.
- [ ] Tu librería tiene API clara y tests.
- [ ] Puedes revisar el código de M02 y señalar 5 mejoras concretas.
