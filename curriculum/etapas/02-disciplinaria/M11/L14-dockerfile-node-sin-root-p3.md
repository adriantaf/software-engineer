---
id: L14
materia: M11
orden: 14
titulo: Dockerfile Node sin root (P3)
horas: 5
semana: 4
lectura: "Dockerfile reference USER"
evidencia: "projects/m11-so/Dockerfile"
---

# L14 — Dockerfile Node sin root (P3)

**~5 h · Semana 4**

## Objetivo

Escribir Dockerfile Node con usuario no-root y dependencias `npm ci`.

## Por qué importa

Root en contenedor amplifica escape y escritura indebida.

## Conceptos

- USER.
- COPY --chown.
- slim images.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Dockerfile según ejemplo ficha M11; `docker build` y `docker run` verificando `whoami` dentro.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l14 dockerfile-node-sin-root-p3"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docker | Dockerfile best practices | Ficha M11 |

## Hecho cuando

1. Imagen construye.
2. Proceso no es root.
3. Nota en README.

## Errores comunes

- Secretos en ARG/ENV de build.
- latest sin pin.

## Siguiente

[L15 — docker compose: API y base de datos](L15-docker-compose-api-y-base-de-datos.md)
