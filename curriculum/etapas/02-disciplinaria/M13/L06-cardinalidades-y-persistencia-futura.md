---
id: L06
materia: M13
orden: 6
titulo: Cardinalidades y persistencia futura
horas: 5.0
semana: 2
lectura: Cardinalidades 1..* / *..*; FK futuras M09
evidencia: clases.md con cardinalidades + nota de tablas/FK
---

# L06 — Cardinalidades y persistencia futura

**~5.0 h · Semana 2**

Las flechas bonitas mienten si no dices *cuántos*. Hoy fijamos multiplicidad y el puente a tablas.

## Objetivo

Actualizar `diagramas/clases.md` con cardinalidades y un mapa clase→tabla coherente con M09.

## Pasos (hazlos en orden)

### 1. Revisa M09 si existe (25–35 min)

```bash
ls projects/m09-bases-datos/migrations 2>/dev/null
cat projects/m09-bases-datos/er-agenda.md 2>/dev/null | head -80
```

Si no hay M09 aún, asume tablas `usuarios`, `clientes`, `servicios`, `citas` como en el scaffold típico.

### 2. Anota multiplicidades (50–60 min)

Ejemplo piloto:

| Asociación | Multiplicidad | Regla |
|------------|---------------|-------|
| Cliente–Cita | 1 a * | toda cita tiene un cliente |
| Servicio–Cita | 1 a * | MVP: un servicio por cita |
| Usuario–Cita | 1 a * | quién la creó / staff asignado |

Actualiza el Mermaid (`"1" --> "*"`).

### 3. Sección persistencia (60–70 min)

Añade a `clases.md`:

```markdown
## Persistencia futura (M09 / M17)

| Clase | Tabla | FK |
|-------|-------|-----|
| Cita | citas | cliente_id, servicio_id, usuario_id |
| … | … | … |

Índices probables: (inicio), (cliente_id), unique parcial anti-doble-booking (decidir en ADR persistencia).
```

### 4. Commit (15 min)

```bash
git add projects/m13-diseno/diagramas/clases.md
git commit -m "docs(m13): cardinalidades y mapeo a persistencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Multiplicidad en asociaciones; mapeo a FK en PostgreSQL | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. Cada asociación en `clases.md` tiene multiplicidad explícita (1, 0..1, 1..*, *).
2. Sección “Persistencia futura” mapea clase→tabla y FK (aunque no escribas SQL hoy).
3. Commit `docs(m13): cardinalidades y mapeo a persistencia`.

## Errores comunes

- Cita *—* Servicio sin aclarar si una cita es un solo servicio (MVP).
- Cardinalidades que contradicen el ER de M09.
- “N:N citas-servicios” sin tabla puente pensada.

## Siguiente

[L07 — Secuencia: autenticación y sesión](L07-secuencia-autenticacion-y-sesion.md)
