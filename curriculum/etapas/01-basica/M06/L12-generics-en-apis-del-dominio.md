---
id: L12
materia: M06
orden: 12
titulo: Generics en APIs del dominio
horas: 5
semana: 3
lectura: "Repaso Generics + Handbook Utility Types (Partial, Pick)"
evidencia: "API exportada tipada; semana 3 cerrada con commit"
---

# L12 — Generics en APIs del dominio

**~5 h · Semana 3**

Cierras semana 3 integrando generics en la superficie pública que consumirá tu librería (semana 5).

## Objetivo

Diseñar tipos exportados estables (`CrearLibroInput`, `Pagina<T>`) usando generics y utility types donde aporten.

## Pasos

### 1. Lectura utility types (45 min)

`Partial`, `Pick`, `Omit` — solo los que uses.

### 2. DTOs de entrada/salida (90 min)

Separa entidad interna de DTO público.

### 3. Paginación o lista genérica (90 min)

```ts
export interface Pagina<T> {
  items: T[];
  total: number;
}
```

### 4. Documentación TSDoc (60 min)

Comentarios en exports públicos (una línea útil cada uno).

### 5. Commit cierre semana 3 (15 min)

`feat(m06): API publica tipada semana 3`

## Hecho cuando

1. `src/index.ts` exporta API coherente y documentada.
2. Generics aparecen donde evitan duplicación real.
3. Tests de contratos públicos.

## Errores comunes

- Exportar todo el interior del dominio.
- Utility types ilegibles anidados.

## Siguiente

[L13 — Errores como diseño (CC cap. 7)](L13-errores-como-diseno.md)
