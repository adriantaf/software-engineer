---
id: L11
materia: M13
orden: 11
titulo: Componentes y despliegue (C4 ligero)
horas: 5
semana: 3
lectura: "C4 nivel 1-2"
evidencia: "diagramas/componentes.md"
---

# L11 — Componentes y despliegue (C4 ligero)

**~5 h · Semana 3**

## Objetivo

Diagrama contenedores: browser, API, Postgres, (futuro) worker.

## Por qué importa

Prepara M11 playbook y M19 deploy.

## Conceptos

- contenedor C4.
- dependencia.
- puerto.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Mermaid o texto. Postgres solo red interna.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l11 componentes-y-despliegue-c4-ligero"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| C4 | modelo contenedor | m11 playbook |
| Catálogo | Entrada M13 | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

1. componentes.md.
2. DB interna.
3. Enlace arquitectura.

## Errores comunes

- DB pública en diagrama.
- Falta API.

## Siguiente

[L12 — Boundaries actualizados y amenazas](L12-boundaries-actualizados-y-amenazas.md)
