---
id: L01
materia: M17
orden: 1
titulo: Scaffold Agenda Ops — API, DB y stack.md
horas: 5
semana: 1
lectura: "producto-saas.md + m13-diseno + M09 esquema"
evidencia: "projects/m17-agenda-ops/stack.md + scaffold API"
---

# L01 — Scaffold Agenda Ops — API, DB y stack.md

**~5 h · Semana 1**

## Objetivo

Inicializar `projects/m17-agenda-ops/` con TypeScript strict, conexión Postgres y documentar stack fijo.

## Por qué importa

Cambiar stack a mitad de materia sin ADR destruye velocidad.

## Conceptos

- scaffold.
- Postgres.
- monolito modular.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m17-agenda-ops/docs projects/m17-agenda-ops/src
```
Crea `stack.md` (framework HTTP, ORM, front). Migra o enlaza esquema M09. Health `GET /health` 200.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l01 scaffold-agenda-ops-api-db-y-stack-md"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m13-diseno | endpoints.md | m09 esquema |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. Repo scaffold.
2. stack.md.
3. DB conecta local.
4. Health check.

## Errores comunes

- Stack sin documentar.
- Secrets en repo.

## Siguiente

[L02 — Registro con hash de contraseña](L02-registro-con-hash-de-contrasena.md)
