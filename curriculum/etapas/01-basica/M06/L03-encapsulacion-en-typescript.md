---
id: L03
materia: M06
orden: 3
titulo: Encapsulación en TypeScript
horas: 5
semana: 1
lectura: "Handbook TS — Classes (fields private, readonly)"
evidencia: "Estado interno privado; tests no acceden a campos internos"
---

# L03 — Encapsulación en TypeScript

**~5 h · Semana 1**

Encapsulación protege invariantes: el exterior no muta estado inválido.

## Objetivo

Usar `#privado`, `private`, `readonly` donde corresponda; exponer API mínima estable.

## Pasos

### 1. Lectura Handbook (40 min)

Classes: parameter properties, `readonly`, private fields.

### 2. Auditar superficie pública (60 min)

Lista cada export: ¿debe ser público? Reduce exports en `index.ts` si creaste barrel.

### 3. Implementación (120 min)

- Colección interna no expuesta como array mutable.
- Métodos `agregar`, `buscar`, no `items.push` desde fuera.

### 4. Tests solo vía API (90 min)

Reescribe tests que tocaban campos internos. Si necesitas inspección, método `cantidad()` o snapshot de DTO inmutable.

### 5. Nota de diseño (30 min)

En `DOMINIO.md`, sección **Encapsulación**: qué ocultaste y por qué.

## Hecho cuando

1. No hay acceso directo a estructuras mutables desde fuera del módulo.
2. Tests pasan usando solo API pública.
3. Documentaste decisiones de visibilidad.

## Errores comunes

- `public items: Libro[]` exportado.
- `#private` en todo por estética sin criterio.

## Siguiente

[L04 — Nombres y funciones pequeñas (CC 1–3)](L04-nombres-y-funciones-cc-1-3.md)
