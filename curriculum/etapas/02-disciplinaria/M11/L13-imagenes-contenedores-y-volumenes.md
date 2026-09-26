---
id: L13
materia: M11
orden: 13
titulo: Imágenes, contenedores y volúmenes
horas: 5
semana: 4
lectura: "Docker docs + Silberschatz síntesis"
evidencia: "labs/docker-intro.md"
---

# L13 — Imágenes, contenedores y volúmenes

**~5 h · Semana 4**

## Objetivo

Diferenciar imagen, contenedor, volumen; levantar `hello-world` y un contenedor Node efímero.

## Por qué importa

Agenda Ops usará Postgres persistente; hoy separas datos de imagen.

## Conceptos

- capa de imagen.
- volumen nombrado.
- ephemeral container.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
docker run --rm hello-world
docker volume create m11-pgdata
```

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m11): l13 imagenes-contenedores-y-volumenes"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Docker | Volumes overview | Silberschatz |
| Catálogo | Entrada M11 | [Bibliografía · M11](../../../bibliografia.md#m11-sistemas-operativos) |


## Hecho cuando

1. Glosario imagen/contenedor/volumen.
2. Volumen creado.
3. Notas para compose.

## Errores comunes

- Datos en capa writable sin volumen.
- docker system prune sin pensar.

## Siguiente

[L14 — Dockerfile Node sin root (P3)](L14-dockerfile-node-sin-root-p3.md)
