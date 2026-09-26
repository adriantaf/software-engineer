---
id: L06
materia: M13
orden: 6
titulo: Cardinalidades y persistencia futura
horas: 5
semana: 2
lectura: "Elmasri relaciones (repaso)"
evidencia: "clases.md cardinalidades"
---

# L06 — Cardinalidades y persistencia futura

**~5 h · Semana 2**

## Objetivo

Anotar cardinalidades y FKs futuras coherentes con M09.

## Por qué importa

Evita modelo que no se puede implementar en SQL.

## Conceptos

- 1:N.
- nullable.
- índice (nota).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tabla entidad-relación texto. Marca PII.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l06 cardinalidades-y-persistencia-futura"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| M09 | ficha repaso | srs-v1 datos |

## Hecho cuando

1. Cardinalidades en diagrama.
2. PII marcada.
3. Notas FK.

## Errores comunes

- Many-to-many sin tabla intermedia.
- Mezclar staff y owner en una clase.

## Siguiente

[L07 — Secuencia: autenticación y sesión](L07-secuencia-autenticacion-y-sesion.md)
