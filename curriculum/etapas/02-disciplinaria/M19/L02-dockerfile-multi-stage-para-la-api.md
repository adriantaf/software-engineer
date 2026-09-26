---
id: L02
materia: M19
orden: 2
titulo: Dockerfile multi-stage para la API
horas: 5
semana: 1
lectura: "Dockerfile best practices (oficial)"
evidencia: "Dockerfile en repo + projects/m19-ops/docker.md"
---

# L02 — Dockerfile multi-stage para la API

**~5 h · Semana 1**

## Objetivo

Escribir Dockerfile multi-stage: build TS/bundle y runtime slim sin devDependencies ni fuentes.

## Por qué importa

Imagen pequeña y sin toolchain reduce superficie.

## Conceptos

- multi-stage
- USER node
- HEALTHCHECK

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Implementa patrón de la ficha M19. Documenta comandos build en `projects/m19-ops/docker.md`.

`.dockerignore`: node_modules, .git, .env.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m19): l02 dockerfile-multi-stage-para-la-api"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docker | multi-stage | M11 Docker |
| Catálogo | Entrada M19 | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

1. Dockerfile multi-stage.
2. docker.md con comandos.
3. .dockerignore.

## Errores comunes

- COPY .env
- root en runtime

## Siguiente

[L03 — Compose prod-like: API + Postgres + volúmenes](L03-compose-prod-like-api-postgres-volumenes.md)
