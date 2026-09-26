---
id: L19
materia: M20
orden: 19
titulo: Release notes y demo cruzada con web
horas: 5
semana: 5
lectura: "Paridad auth web/móvil"
evidencia: "projects/m20-movil/release-notes.md"
---

# L19 — Release notes y demo cruzada con web

**~5 h · Semana 5**

## Objetivo

Notas versión; misma cuenta web y móvil ven mismas citas.

## Por qué importa

Proyecto M20 demuestra canal móvil del CRM.

## Conceptos

- paridad
- demo

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

release-notes.md + pasos demo 10 segundos del día citas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l19 release-notes-y-demo-cruzada-con-web"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | proyecto M20 | M17 web |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. release-notes
2. Demo cruzada documentada
3. Mismas citas

## Errores comunes

- Cuentas distintas sin explicar
- Datos mock

## Siguiente

[L20 — Cierre M20 — dominio y README proyecto](L20-cierre-m20-dominio-y-readme-proyecto.md)
