---
id: L01
materia: M12
orden: 1
titulo: Design partner y guion de entrevista
horas: 5
semana: 1
lectura: "plantilla.md + producto-saas.md"
evidencia: "entrevistas/guion-v1.md"
---

# L01 — Design partner y guion de entrevista

**~5 h · Semana 1**

## Objetivo

Elegir sub-vertical estable y redactar ≥10 preguntas abiertas sobre flujo de citas y dolores actuales.

## Por qué importa

Agenda Ops empieza con problema real, no con pantallas.

## Conceptos

- ICP.
- design partner.
- preguntas abiertas.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m12-srs/entrevistas
cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
```
Guion: roles, herramientas actuales (WhatsApp/libreta), no-shows, datos sensibles.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l01 design-partner-y-guion-de-entrevista"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | producto-saas.md | plantilla SRS |

## Hecho cuando

1. Sub-vertical elegido.
2. Guion ≥10 preguntas.
3. Sin cambiar vertical en 3 semanas.

## Errores comunes

- Preguntas cerradas sí/no.
- Saltar roles staff.

## Siguiente

[L02 — Entrevista y notas timestamp](L02-entrevista-y-notas-timestamp.md)
