---
id: L11
materia: M06
orden: 11
titulo: "Generics: funciones y contenedores"
horas: 5
semana: 3
lectura: "TS Handbook — Generics"
evidencia: "src/generics/ con funciones reutilizables testeadas"
---

# L11 — Generics: funciones y contenedores

**~5 h · Semana 3**

Los generics expresan estructuras sin perder tipo: repositorios, utilidades, colecciones.

## Objetivo

Escribir funciones genéricas (`mapResult`, `findById`) y un contenedor tipado simple con tests.

## Pasos

### 1. Lectura (60 min)

Handbook Generics: constraints, `extends`.

### 2. Utilidades (120 min)

```ts
export function findById<T extends { id: string }>(items: T[], id: string): T | undefined {
  return items.find((x) => x.id === id);
}
```

### 3. Repositorio genérico (opcional, 90 min)

`RepositorioEnMemoria<T extends Identificable>` si no rompe claridad del dominio.

### 4. Tests (60 min)

Varias instancias de `T` (libro, usuario mock).

## Hecho cuando

1. ≥2 funciones genéricas con constraints.
2. Tests instancian tipos distintos.
3. Sin `any`.

## Errores comunes

- Generic `T` sin constraint cuando accedes a `.id`.
- Sobre-generalizar el dominio entero.

## Siguiente

[L12 — Generics en APIs del dominio](L12-generics-en-apis-del-dominio.md)
