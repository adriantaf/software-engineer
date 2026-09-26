---
id: L06
materia: M06
orden: 6
titulo: Composición frente a herencia
horas: 5
semana: 2
lectura: "CC cap. 10 (clases) + artículo corto composición vs herencia"
evidencia: "Eliminación o reducción de jerarquías; composición documentada en DOMINIO.md"
---

# L06 — Composición frente a herencia

**~5 h · Semana 2**

Herencia profunda acopla; la composición suele escalar mejor en dominios reales.

## Objetivo

Reemplazar (o evitar) jerarquías `extends` innecesarias por composición de comportamientos/interfaces.

## Pasos

### 1. Lectura (45 min)

CC cap. 10 + notas del plan M06. Escribe regla personal: “Heredo solo si hay relación **es-un** verdadera y estable”.

### 2. Auditoría (60 min)

Busca `extends` en el proyecto. Por cada uno: ¿justificado? Si no, plan de composición.

### 3. Refactor (150 min)

Ejemplo: en lugar de `LibroEspecial extends Libro`, composición con `PoliticaPrestamo` inyectada.

### 4. Tests (60 min)

Asegura paridad de comportamiento tras refactor.

### 5. Documento (30 min)

En `DOMINIO.md`, tabla: antes (herencia) → después (composición).

## Hecho cuando

1. Cero jerarquías de profundidad >2, o justificación escrita.
2. Tests verdes.
3. Puedes explicar un caso donde **no** usaste herencia.

## Errores comunes

- Mixin caótico sin interfaces claras.
- Herencia solo para reutilizar código (usa funciones).

## Siguiente

[L07 — SOLID intro: S, O y D](L07-solid-intro-s-o-d.md)
