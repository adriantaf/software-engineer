---
id: L08
materia: M13
orden: 8
titulo: "Secuencia: crear cita (P2)"
horas: 5
semana: 2
lectura: "Secuencia negocio"
evidencia: "diagramas/secuencia-crear-cita.md"
---

# L08 — Secuencia: crear cita (P2)

**~5 h · Semana 2**

## Objetivo

Secuencia crear cita con chequeo conflicto horario.

## Por qué importa

P2 exige clase + secuencia crítica.

## Conceptos

- transacción (idea).
- conflicto.
- 201/409.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Secuencia con rama conflicto. Enlaza CU y US.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l08 secuencia-crear-cita-p2"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Larman | secuencia | stories citas |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. P2 secuencia lista.
2. Conflicto modelado.
3. Commit semana 2.

## Errores comunes

- Happy path solo.
- Sin rol staff.

## Siguiente

[L09 — Arquitectura en capas](L09-arquitectura-en-capas.md)
