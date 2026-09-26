---
id: L03
materia: M19
orden: 3
titulo: "Compose prod-like: API + Postgres + volúmenes"
horas: 5
semana: 1
lectura: "Compose file reference"
evidencia: "compose.yml + projects/m19-ops/docker.md"
---

# L03 — Compose prod-like: API + Postgres + volúmenes

**~5 h · Semana 1**

## Objetivo

Orquestar API y PostgreSQL con volúmenes persistentes, red interna y healthchecks.

## Por qué importa

P1 M19 es stack local idéntico en espíritu a prod.

## Conceptos

- depends_on healthy
- volumen db-data
- puerto 5432 no publicado

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

`compose.yml`: servicios api, db; env desde `.env.example` sin secretos reales.

`docker compose up --build` documentado con tiempo de arranque y curl `/health`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l03 compose-prod-like-api-postgres-volumenes"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docker | Compose | M11 compose |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. Compose levanta stack.
2. Healthcheck OK.
3. Postgres con volumen.

## Errores comunes

- 5432:5432 público
- password en compose commiteado

## Siguiente

[L04 — Stack local documentado y P1 Docker](L04-stack-local-documentado-y-p1-docker.md)
