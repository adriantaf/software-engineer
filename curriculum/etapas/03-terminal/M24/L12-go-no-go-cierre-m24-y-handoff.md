---
id: L12
materia: M24
orden: 12
titulo: Go/no-go, cierre M24 y handoff
horas: 5
semana: 3
lectura: "Repaso ficha M24 criterios dominio"
evidencia: "projects/m24-emergentes/go-no-go.md + bitácora semana-03.md"
---

# L12 — Go/no-go, cierre M24 y handoff

**~5 h · Semana 3**

## Objetivo

Redactar decisión go/no-go argumentada; actualizar backlog; cerrar prácticas P2–P3 y criterios dominio.

## Por qué importa

Un ‘no’ bien fundado cumple el proyecto si el spike demostró costo/riesgo > valor.

## Conceptos

- Go / no-go / defer
- Issue derivado
- Archivar spike

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`projects/m24-emergentes/go-no-go.md`: decisión, criterios, próximos pasos si go, qué archivar si no.

Cierra bitácora semana 3. README del proyecto enlaza toda la evidencia P1–P3.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta a **Agenda Ops** (SaaS multi-tenant, piloto M17, egreso M26). Usa el escenario de [producto-saas](../../producto-saas.md) si aún no tienes deploy.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/
git status
git commit -m "docs(m24): l12 go-no-go-cierre-m24-y-handoff"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | Criterios dominio M24 | M26 alcance |

## Hecho cuando

1. go-no-go.md publicado.
2. README proyecto actualizado.
3. Backlog M21 tocado.

## Errores comunes

- Go sin plan de seguridad.
- No-go sin spike ejecutado.
