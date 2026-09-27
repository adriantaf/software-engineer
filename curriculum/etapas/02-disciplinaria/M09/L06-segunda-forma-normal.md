---
id: L06
materia: M09
orden: 6
titulo: Segunda forma normal
horas: 5.0
semana: 2
lectura: "Elmasri: 2FN, dependencia parcial"
evidencia: Ejemplo PK compuesta + eliminación de dependencia parcial
---

# L06 — Segunda forma normal

**~5.0 h · Semana 2**

2FN elimina dependencias parciales de una clave compuesta. Aunque uses UUID, debes saber detectar el antipatrón.

## Objetivo

Explicar 2FN con un ejemplo del dominio (líneas de cita o staff+día) y justificar por qué tu esquema actual cumple o qué cambiarías.

## Pasos

### 1. Lectura (45 min)

Dependencia funcional y 2FN en Elmasri.

### 2. Caso que viola 2FN (60 min)

Imagina tabla `cita_detalle` con PK `(cita_id, servicio_id)` y columnas `nombre_servicio`, `precio_serv`. `nombre_servicio` depende solo de `servicio_id` → viola 2FN.

Escríbelo en `er-agenda.md` con la descomposición correcta (tabla `servicios` + hechos de la cita).

### 3. Tu esquema real (60 min)

Revisa PKs de `001_init.sql`. Con surrogate keys, 2FN suele cumplirse si no repites atributos del padre. Confirma por escrito: “no hay atributos que dependan de parte de la clave porque…”.

### 4. Mini ejercicio SQL (45 min)

Inserta un servicio y una cita; actualiza el nombre del servicio; verifica que las citas históricas **siguen** viendo el nombre nuevo vía JOIN (trade-off que verás en L08 — snapshot de precio).

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): segunda forma normal"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: 2FN, dependencia parcial | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Documentas un caso con PK compuesta que viola 2FN (inventado o histórico).
2. Muestras tablas resultantes en 2FN.
3. Actualizas la fila 2FN en `er-agenda.md`.

## Errores comunes

- Decir “ya estoy en 2FN” solo porque usas UUID surrogate sin analizar dependencias.
- Meter `nombre_cliente` en una tabla con PK `(cita_id, servicio_id)` y dejarlo así.
- Confundir 2FN con “tener índices”.

## Siguiente

[L07 — Tercera forma normal (P1)](L07-tercera-forma-normal-p1.md)
