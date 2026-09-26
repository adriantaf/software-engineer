---
id: L08
materia: M15
orden: 8
titulo: IDOR y roles — casos 403
horas: 5
semana: 2
lectura: "Hilo seguridad + stories M12"
evidencia: "projects/m15-calidad/tests/seguridad-idor.test.ts"
---

# L08 — IDOR y roles — casos 403

**~5 h · Semana 2**

## Objetivo

Añadir tests que demuestren 403 al acceder a cita de otro negocio o acción de owner como staff.

## Por qué importa

IDOR en piloto destruye confianza del design partner.

## Conceptos

- IDOR.
- 403.
- multi-negocio futuro.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥2 tests 403 documentados con usuario/rol en comentario del test.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l08 idor-y-roles-casos-403"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Hilo | seguridad.md | m12 RNF |

## Hecho cuando

1. 403 reproducible.
2. Documentado en piramide.md capa API.
3. Commit.

## Errores comunes

- 403 manual solo.
- Mensaje que filtra datos.

## Siguiente

[L09 — Workflow GitHub Actions — esqueleto](L09-workflow-github-actions-esqueleto.md)
