---
id: L15
materia: M11
orden: 15
titulo: docker compose: API y base de datos
horas: 5
semana: 4
lectura: "Compose file reference"
evidencia: "docker-compose.yml documentado"
---

# L15 — docker compose: API y base de datos

**~5 h · Semana 4**

## Objetivo

Definir compose mínimo API+Postgres: red interna, volumen DB, puerto API solo.

## Por qué importa

Playbook M11 debe levantar stack reproducible.

## Conceptos

- service network.
- depends_on.
- ports mapping.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Compose con Postgres no publicado a 0.0.0.0 salvo necesidad documentada. `.env.example`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l15 docker-compose-api-y-base-de-datos"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docker | Compose | Postgres image doc |

## Hecho cuando

1. `docker compose up` funciona.
2. DB no expuesta públicamente.
3. .env.example sin secretos.

## Errores comunes

- Puerto 5432 publicado “temporal”.
- Contraseña en git.

## Siguiente

[L16 — Playbook local y cierre M11](L16-playbook-local-y-cierre-m11.md)
