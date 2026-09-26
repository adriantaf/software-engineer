---
id: L02
materia: M13
orden: 2
titulo: Actores y casos de uso prioritarios
horas: 5
semana: 1
lectura: "Larman casos de uso"
evidencia: "casos-de-uso.md borrador"
---

# L02 — Actores y casos de uso prioritarios

**~5 h · Semana 1**

## Objetivo

Derivar casos de uso Must del SRS: login, CRUD citas/clientes, admin roles.

## Por qué importa

Casos de uso son guía de pruebas y API.

## Conceptos

- actor.
- caso de uso.
- precondición.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥6 casos con ID CU-XX. Enlaza a US del SRS.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m13): l02 actores-y-casos-de-uso-prioritarios"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Larman | casos de uso | srs-v1 |

## Hecho cuando

1. ≥6 casos.
2. Trazabilidad SRS.
3. Actores correctos.

## Errores comunes

- Casos decorativos.
- Olvidar staff.

## Siguiente

[L03 — Escenarios alternos y errores](L03-escenarios-alternos-y-errores.md)
