---
id: L05
materia: M09
orden: 5
titulo: Primera forma normal y anomalías
horas: 5.0
semana: 2
lectura: "Elmasri: 1FN, anomalías de inserción/borrado/actualización"
evidencia: er-agenda.md sección 1FN + ejemplo de tabla mala descompuesta
---

# L05 — Primera forma normal y anomalías

**~5.0 h · Semana 2**

1FN exige atributos atómicos. Las hojas de Excel del salón casi nunca lo cumplen.

## Objetivo

Demostrar una violación de 1FN del dominio y dejar el esquema (o el diseño) en 1FN con evidencia escrita.

## Conceptos

- Valor atómico vs lista/repetición en la misma fila.
- Anomalías de actualización (cambiar un teléfono en N filas).
- Anomalías de borrado (perder el único dato del cliente al borrar una cita).

## Pasos

### 1. Lectura (45–60 min)

Capítulo/sección de 1FN y anomalías en Elmasri. Anota definiciones con tus palabras.

### 2. Tabla mala (45 min)

En `er-agenda.md` (sección Normalización), pega algo así y **explícalo**:

| cita_id | cliente | telefonos | servicios |
|---------|---------|-----------|-----------|
| 1 | Ana | 646-111, 646-222 | Corte, Barba |

Señala qué columnas no son atómicas.

### 3. Descomposición (75 min)

Escribe las tablas resultantes (Cliente, Telefono opcional, Servicio, Cita). Compara con `001_init.sql`: ¿ya estás en 1FN? Si añadiste un campo lista, corrígelo con migración o nota de deuda.

### 4. Anomalías (40 min)

Una fila de texto por tipo: inserción / actualización / borrado, usando el ejemplo malo.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): 1FN y anomalias agenda"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: 1FN, anomalías de inserción/borrado/actualización | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas una “tabla Excel” que viola 1FN (teléfonos múltiples o listas en una celda).
2. Muestras la descomposición a relaciones atómicas.
3. Marcas 1FN como cumplida en la tabla de normalización de `er-agenda.md`.

## Errores comunes

- Guardar `telefonos` como `'a,b,c'` en un solo `text` “porque es más fácil”.
- Declarar 1FN sin ejemplo de anomalía.
- Normalizar de oídas sin tocar el ER.

## Siguiente

[L06 — Segunda forma normal](L06-segunda-forma-normal.md)
