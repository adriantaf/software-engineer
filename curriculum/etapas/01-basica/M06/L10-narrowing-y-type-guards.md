---
id: L10
materia: M06
orden: 10
titulo: Narrowing y type guards
horas: 5
semana: 3
lectura: "TS Handbook — Narrowing"
evidencia: "Type guards user-defined + tests de ramas"
---

# L10 — Narrowing y type guards

**~5 h · Semana 3**

TypeScript estrecha tipos tras comprobaciones; tú diseñas guards reutilizables.

## Objetivo

Implementar type guards (`is`) y narrowing con `in`, `typeof`, discriminantes; cubrir ramas con tests.

## Pasos

### 1. Lectura (60 min)

Handbook Narrowing completo (secciones principales).

### 2. Guards (90 min)

```ts
export function esPrestado(e: EstadoLibro): e is Extract<EstadoLibro, { tipo: "prestado" }> {
  return e.tipo === "prestado";
}
```

### 3. API pública (90 min)

Funciones que aceptan union y devuelven Result o throw según política (unifica criterio).

### 4. Tests por rama (60 min)

Cada variante del union tiene ≥1 test.

### 5. Elimina casts (30 min)

Busca `as` innecesarios; reemplaza por guards.

## Hecho cuando

1. ≥2 type guards reutilizables.
2. Sin `as` salvo casos documentados.
3. Tests por discriminante.

## Errores comunes

- Cast para callar al compilador.
- Guard incorrecto (mentira al tipo system).

## Siguiente

[L11 — Generics: funciones y contenedores](L11-generics-funciones-y-contenedores.md)
