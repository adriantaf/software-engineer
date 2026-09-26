---
id: L09
materia: M19
orden: 9
titulo: Promover configuración a producción
horas: 5
semana: 3
lectura: "12-factor config"
evidencia: "projects/m19-ops/ambientes.md actualizado"
---

# L09 — Promover configuración a producción

**~5 h · Semana 3**

## Objetivo

Desplegar prod con misma imagen que staging y distintas env vars; documentar diferencias.

## Por qué importa

Prod es para design partner, no laboratorio.

## Conceptos

- promoción imagen
- separación datos

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Segunda entrada deploy-log prod. Tabla diff staging vs prod en ambientes.md.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l09 promover-configuracion-a-produccion"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | M19 semana 3 | — |

## Hecho cuando

1. Prod URL.
2. Diff documentado.
3. Datos separados.

## Errores comunes

- Migrar en prod primero
- Misma DB staging/prod

## Siguiente

[L10 — Logs, rollback y versión desplegada](L10-logs-rollback-y-version-desplegada.md)
