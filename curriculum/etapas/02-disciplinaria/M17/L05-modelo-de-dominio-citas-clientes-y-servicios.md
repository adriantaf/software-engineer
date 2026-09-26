---
id: L05
materia: M17
orden: 5
titulo: Modelo de dominio citas, clientes y servicios
horas: 5
semana: 2
lectura: "m13 diagrama clases + srs-v1"
evidencia: "migraciones / entidades"
---

# L05 — Modelo de dominio citas, clientes y servicios

**~5 h · Semana 2**

## Objetivo

Alinear tablas y entidades con diseño M13: citas, clientes, servicios, relaciones y reglas en código dominio.

## Por qué importa

CRUD sin modelo coherente genera IDOR y datos huérfanos.

## Conceptos

- entidad.
- migración.
- dominio.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Migraciones aplicadas. Tipos dominio sin dependencia de ORM en reglas puras (carpeta `domain/`).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l05 modelo-de-dominio-citas-clientes-y-servi"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| m12-srs | RF citas | m13 clases |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. Migraciones.
2. domain/ con reglas.
3. Commit.

## Errores comunes

- Lógica solo en controllers.
- Sin FK.

## Siguiente

[L06 — API citas — crear y listar con reglas](L06-api-citas-crear-y-listar-con-reglas.md)
