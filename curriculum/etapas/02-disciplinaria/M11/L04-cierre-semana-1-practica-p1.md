---
id: L04
materia: M11
orden: 4
titulo: Cierre semana 1 — práctica P1
horas: 5
semana: 1
lectura: "Repaso Silberschatz procesos"
evidencia: "labs/semana-01-procesos.md consolidado"
---

# L04 — Cierre semana 1 — práctica P1

**~5 h · Semana 1**

## Objetivo

Consolidar labs de procesos/señales/permisos para P1.

## Por qué importa

P1 exige comandos reproducibles, no capturas sueltas.

## Conceptos

- Trazabilidad comando → efecto.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Une L01–L03 en un solo archivo con índice. Verifica que otro pueda reproducir.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l04 cierre-semana-1-practica-p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M11-sistemas-operativos.md | — |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. P1 semana 1 completa.
2. Commit consolidado.
3. Checklist permisos.

## Errores comunes

- Mezclar logs de distintas máquinas sin fecha.
- Olvidar umask en explicación.

## Siguiente

[L05 — Memoria virtual y paginación (intuición)](L05-memoria-virtual-y-paginacion-intuicion.md)
