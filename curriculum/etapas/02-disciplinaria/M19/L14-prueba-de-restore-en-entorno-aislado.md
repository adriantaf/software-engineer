---
id: L14
materia: M19
orden: 14
titulo: Prueba de restore en entorno aislado
horas: 5
semana: 4
lectura: "Restore docs"
evidencia: "projects/m19-ops/restore-test.md"
---

# L14 — Prueba de restore en entorno aislado

**~5 h · Semana 4**

## Objetivo

Restaurar dump en DB de prueba, verificar citas visibles, registrar tiempo y resultado.

## Por qué importa

Un restore nunca probado no cuenta.

## Conceptos

- restore
- RTO idea
- vacuum

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

restore-test.md: fecha, dump usado, duración, éxito/fallo, captura query count citas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l14 prueba-de-restore-en-entorno-aislado"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M19 P3 | — |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. Restore real documentado.
2. Verificación datos.
3. Fecha.

## Errores comunes

- Solo teoría
- Restore sobre prod

## Siguiente

[L15 — Runbook completo de producción](L15-runbook-completo-de-produccion.md)
