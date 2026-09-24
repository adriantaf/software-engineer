---
id: M14
titulo: Patrones de software
etapa: disciplinaria
orden: 14
semanas: 4
horas: 80
practicas:
  - id: p1
    titulo: Implementar Strategy, Observer, Factory
  - id: p2
    titulo: Repository + Service en el backend
  - id: p3
    titulo: Refactor de un módulo legacy tuyo
proyecto:
  id: proj
  titulo: Aplicar ≥5 patrones en el CRM con justificación
---

# M14 — Patrones de software

## Por qué existe
Patrones son vocabulario compartido. Mal usados = cargo cult.

## Día 1 (2–3 h)
Implementa Strategy para “calcular precio” (base vs con descuento) con tests. Escribe cuándo NO usar el patrón.

## Ejemplo
```ts
type Precio = { calcular(base: number): number };
const normal: Precio = { calcular: (b) => b };
const promo: Precio = { calcular: (b) => b * 0.9 };
```

## Temario
GoF selectos → Repository/Service → refactor CRM → justificación en ADR.

## Libros (ES)
GoF ed. ES si la consigues; o resúmenes guiados + mentor.

## Errores comunes
Nombrar “Factory” sin factory; over-engineering.

## Criterios de dominio
- [ ] 5 patrones aplicados con justificación escrita.
