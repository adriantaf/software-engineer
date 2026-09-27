---
id: L13
materia: M06
orden: 13
titulo: Errores como diseño (CC cap. 7)
horas: 5
semana: 4
lectura: "Código limpio cap. 7 (manejo de errores)"
evidencia: "Jerarquía o catálogo de errores de dominio; sin catch vacíos"
---

# L13 — Errores como diseño (CC cap. 7)

**~5 h · Semana 4**

Los errores son flujo de control y UX para quien llama tu API. Tragar excepciones es deuda.

## Objetivo

Aplicar CC cap. 7: excepciones con contexto, límites claros, sin `catch {}`; definir errores de dominio expresivos.

## Pasos

### 1. Lectura (60 min)

CC cap. 7. Anota reglas sobre checked vs unchecked (adaptado a TS).

### 2. Auditoría (45 min)

Busca `catch`, `throw new Error("error")` genéricos.

### 3. Catálogo de errores (90 min)

```ts
export class LibroNoEncontradoError extends Error {
  constructor(public readonly id: string) {
    super(`Libro no encontrado: ${id}`);
    this.name = "LibroNoEncontradoError";
  }
}
```

O union de errores si prefieres sin excepciones (prepara L14).

### 4. Refactor llamadas (90 min)

Mensajes con datos; logs en frontera, no en cada línea.

### 5. Tests de error (45 min)

`expect(() => ...).toThrow(LibroNoEncontradoError)` o equivalente Result.

## Hecho cuando

1. Cero `catch` vacíos.
2. Errores nombrados con contexto.
3. Tests demuestran fallos esperados.

## Errores comunes

- String errors everywhere.
- Loguear y re-lanzar sin añadir info.

## Siguiente

[L14 — Patrón Result tipado](L14-patron-result-tipado.md)
