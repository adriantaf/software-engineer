---
id: L07
materia: M06
orden: 7
titulo: "SOLID intro: S, O y D"
horas: 5
semana: 2
lectura: "Resumen SOLID (S, O, D) + CC cap. 6 y 10"
evidencia: "Tres mejoras etiquetadas S/O/D en comentarios o ADR corto solid-notas.md"
---

# L07 — SOLID intro: S, O y D

**~5 h · Semana 2**

SOLID no es culto: son heurísticas. Hoy aplicarás **S** (responsabilidad única), **O** (abierto/cerrado) y **D** (inversión de dependencias) a tu dominio.

## Objetivo

Identificar y corregir al menos una violación de S, O y D en el código M06 con cambios medibles (menos acoplamiento, extensión sin editar clase core).

## Pasos

### 1. Lectura (60 min)

Lee resumen SOLID (libro, artículo mentor o apuntes fiables). Para cada letra: definición + ejemplo **no** trivial.

### 2. `solid-notas.md` (45 min)

Por principio: violación encontrada → cambio propuesto → commit previsto.

### 3. S — Responsabilidad única (75 min)

Divide clase que mezcla persistencia + reglas + formato de informe.

### 4. O — Abierto/cerrado (75 min)

Ejemplo: nueva regla de préstamo vía estrategia/política sin editar `ServicioPrestamo` entero.

### 5. D — Dependencias (60 min)

Servicio depende de interfaces; wiring en `crearApp()` o factory de tests.

### 6. Commits (15 min)

Hasta tres commits: `refactor(m06): SRP ...`, etc.

## Hecho cuando

1. `solid-notas.md` enlaza commits reales.
2. Extensión demostrada (nueva política) sin modificar código prohibido (documenta qué tocaste).
3. Tests verdes.

## Errores comunes

- Una clase por línea (SRP mal entendido).
- Interfaces duplicadas sin implementaciones.

## Siguiente

[L08 — Refactor documentado (P2)](L08-refactor-documentado-p2.md)
