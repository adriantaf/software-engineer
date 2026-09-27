---
id: L02
materia: M06
orden: 2
titulo: Objetos con comportamiento real
horas: 5
semana: 1
lectura: "Código limpio cap. 3 (funciones) + cap. 10 intro (clases)"
evidencia: "Métodos de dominio con tests; commit feat(m06): comportamiento en entidades"
---

# L02 — Objetos con comportamiento real

**~5 h · Semana 1**

Un objeto combina datos y **comportamiento**. Datos anémicos + servicios gigantes es un antipatrón que corregirás hoy.

## Objetivo

Mover reglas de negocio a métodos cohesivos (entidad o agregado pequeño); evitar clases contenedor vacías.

## Pasos

### 1. Lectura (45 min)

CC cap. 3 (funciones pequeñas) + inicio cap. 10. Lista: ¿cuándo una clase aporta vs cuándo estorba?

### 2. Refactor de anémico → rico (120 min)

Si tu `Libro` solo expone campos, añade métodos como `marcarPrestado(): void` con invariantes (no prestar dos veces). La fachada `Biblioteca` orquesta, no reimplementa toda la lógica en ifs sueltos.

### 3. Tests de invariantes (90 min)

- No prestar si ya prestado.
- Devolver solo si estaba prestado.
- Mensajes de error legibles (string constantes o pequeño catálogo).

### 4. Extracción de funciones (60 min)

Identifica un método >15 líneas; extrae funciones puras con nombres verbales. Commit atómico.

## Hecho cuando

1. Reglas de negocio viven en métodos nombrados, no dispersos.
2. Tests cubren invariantes principales.
3. Commit con mensaje que mencione comportamiento en entidades.

## Errores comunes

- God class `Biblioteca` de 400 líneas.
- Getters/setters sin reglas.

## Siguiente

[L03 — Encapsulación en TypeScript](L03-encapsulacion-en-typescript.md)
