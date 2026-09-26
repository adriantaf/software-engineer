---
id: L07
materia: M09
orden: 7
titulo: Tercera forma normal (P1)
horas: 5.0
semana: 2
lectura: "Elmasri: 3FN / intro BCNF"
evidencia: er-agenda.md en 3FN — cierra P1
---

# L07 — Tercera forma normal (P1)

**~5.0 h · Semana 2**

3FN elimina dependencias transitivas. Con esto cierras la práctica **P1**.

## Objetivo

Dejar `er-agenda.md` en 3FN con justificación y enlazarlo como evidencia P1 en el README.

## Pasos

### 1. Lectura (45–60 min)

3FN e intro a BCNF. Diferencia en una frase tuya: 3FN vs BCNF.

### 2. Caza transitivas (60 min)

Ejemplo a analizar: `cliente_id → codigo_postal → ciudad → estado`. Si modelaras dirección completa, ¿qué tablas salen?

Para Agenda Ops MVP: decide si dirección es necesaria día 1. Si no, escríbelo como fuera de alcance (eso también es diseño).

### 3. Congela el ER 3FN (75 min)

Actualiza diagrama + tabla de normalización. Añade fecha y una frase: “P1 lista porque…”.

### 4. Checklist P1 en README (30 min)

Marca mentalmente (y en texto) que `er-agenda.md` cumple el criterio de la ficha M09.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): er en 3FN cierra P1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: 3FN / intro BCNF | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas al menos una dependencia transitiva evitada o eliminada.
2. Tabla de normalización en `er-agenda.md` marca 1FN–3FN.
3. README indica que P1 (ER hasta 3FN) está listo.

## Errores comunes

- Guardar `ciudad` y `estado` redundantes con una tabla de códigos postales a medias.
- Declarar 3FN sin mencionar dependencias transitivas.
- Cerrar P1 sin diagrama actualizado.

## Siguiente

[L08 — Trade-offs de desnormalización](L08-trade-offs-de-desnormalizacion.md)
