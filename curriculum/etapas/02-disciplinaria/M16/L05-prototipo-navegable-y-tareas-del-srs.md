---
id: L05
materia: M16
orden: 5
titulo: Prototipo navegable y tareas del SRS
horas: 5.0
semana: 2
lectura: Prototipo clicable; tareas Must del SRS
evidencia: prototipo/ navegable + mapa de tareas
---

# L05 — Prototipo navegable y tareas del SRS

**~5.0 h · Semana 2**

Sin prototipo, las sesiones inventan la UI. Hoy lo dejas clicable.

## Objetivo

`projects/m16-ihc/prototipo/` usable en test de 15–30 min.

## Pasos (hazlos en orden)

### 1. Pantallas mínimas (90–120 min)

HTML estático o Figma prototype: Login, Agenda del día, Nueva pedido, Confirmación/error.

### 2. tareas-srs.md (40 min)

| Tarea test | Historia SRS |
|------------|--------------|
| Agendar pedido cliente nuevo | H-pedido-01 |
| Cancelar pedido de hoy | H-pedido-02 |

### 3. Commit

`feat(m16): prototipo navegable y tareas SRS`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Prototipo para test de pasillo alineado al SRS | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. Prototipo navegable (HTML/Figma) cubriendo login → agenda → crear pedido (mínimo).
2. `prototipo/tareas-srs.md` mapea tareas de test a historias Must.
3. Commit `feat(m16): prototipo navegable y tareas SRS`.

## Errores comunes

- Prototipo de marketing no usable en test.
- Tareas que no existen en el SRS.
- Dependencias rotas (links muertos entre pantallas).

## Siguiente

[L06 — Guion de test de usabilidad 15–30 min](L06-guion-de-test-de-usabilidad-15-30-min.md)
