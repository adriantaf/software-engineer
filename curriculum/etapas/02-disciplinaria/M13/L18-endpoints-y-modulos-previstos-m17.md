---
id: L18
materia: M13
orden: 18
titulo: Endpoints y módulos previstos M17
horas: 5
semana: 5
lectura: "OpenAPI borrador opcional"
evidencia: "endpoints.md"
---

# L18 — Endpoints y módulos previstos M17

**~5 h · Semana 5**

## Objetivo

Listar rutas REST previstas con método, auth, DTO (texto).

## Por qué importa

Scaffold M17 usa esta lista.

## Conceptos

- ruta.
- método.
- rol.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tabla ≥12 rutas Must. Coherente con casos de uso.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l18 endpoints-y-modulos-previstos-m17"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| srs-v1 | RF | arquitectura |

## Hecho cuando

1. endpoints.md.
2. Auth por ruta.
3. Coherencia CU.

## Errores comunes

- Rutas no en SRS.
- Falta POST citas.

## Siguiente

[L19 — Checklist listo para scaffold](L19-checklist-listo-para-scaffold.md)
