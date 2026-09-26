---
id: L01
materia: M16
orden: 1
titulo: Recorrido persona nueva y fricciones día 1
horas: 5
semana: 1
lectura: "Krug cap. 1 + producto Agenda Ops"
evidencia: "projects/m16-ihc/heuristicas/fricciones-dia1.md"
---

# L01 — Recorrido persona nueva y fricciones día 1

**~5 h · Semana 1**

## Objetivo

Recorrer UI/wireframe del piloto como usuario nuevo y listar ≥10 fricciones al agendar cita.

## Por qué importa

Tu intuición de dev no es la del dueño del negocio.

## Conceptos

- fricción.
- tarea.
- design partner.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m16-ihc/heuristicas projects/m16-ihc/sesiones
```
Sin ayuda: crear cita. Anota cada pausa/confusión.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m16): l01 recorrido-persona-nueva-y-fricciones-dia"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Krug | No me hagas pensar | producto-saas.md |
| Catálogo | Entrada M16 | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

1. ≥10 fricciones.
2. Fecha y contexto.
3. Commit docs(m16).

## Errores comunes

- Lista genérica.
- Sin probar flujo real.

## Siguiente

[L02 — Auditoría Nielsen — tres heurísticas profundas](L02-auditoria-nielsen-tres-heuristicas-profundas.md)
