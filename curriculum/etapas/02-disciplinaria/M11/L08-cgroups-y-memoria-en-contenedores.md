---
id: L08
materia: M11
orden: 8
titulo: cgroups y memoria en contenedores
horas: 5
semana: 2
lectura: "Docker docs memory + Silberschatz resumen"
evidencia: "labs/cgroups-nota.md"
---

# L08 — cgroups y memoria en contenedores

**~5 h · Semana 2**

## Objetivo

Relacionar cgroups con límites de memoria en Docker y qué ve el proceso dentro del contenedor.

## Por qué importa

M11 semana 4 dockeriza el stack; hoy entiendes por qué el contenedor muere “sin razón”.

## Conceptos

- cgroup v2 (idea).
- Límite memoria Docker.
- OOM en contenedor.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Esboza `deploy.resources.limits.memory` en compose futuro. Nota para playbook.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l08 cgroups-y-memoria-en-contenedores"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docker | Resource constraints | Silberschatz |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Nota cgroups en bitácora.
2. Enlace a playbook futuro.
3. Cierre semana 2.

## Errores comunes

- Sin límite memoria en compose.
- Asumir host ilimitado.

## Siguiente

[L09 — Sistema de archivos: inodos y espacio](L09-sistema-de-archivos-inodos-y-espacio.md)
