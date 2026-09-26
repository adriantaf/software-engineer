---
id: L13
materia: M13
orden: 13
titulo: Plantilla ADR y decisiones de diseño
horas: 5
semana: 4
lectura: "ADR M01"
evidencia: "adr/README o 002"
---

# L13 — Plantilla ADR y decisiones de diseño

**~5 h · Semana 4**

## Objetivo

Fijar plantilla ADR y abrir ADR 002 (stack o persistencia).

## Por qué importa

Decisiones explícitas evitan debate infinito en M17.

## Conceptos

- contexto.
- decisión.
- consecuencias.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

ADR 002: p.ej. Postgres + ORM/query builder. Alternativas rechazadas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l13 plantilla-adr-y-decisiones-de-diseno"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M01 | ADR ejemplo | srs RNF |

## Hecho cuando

1. ADR 002 completo.
2. Plantilla documentada.
3. Commit.

## Errores comunes

- ADR sin alternativas.
- Copiar texto genérico.

## Siguiente

[L14 — ADR persistencia y modelo de datos](L14-adr-persistencia-y-modelo-de-datos.md)
