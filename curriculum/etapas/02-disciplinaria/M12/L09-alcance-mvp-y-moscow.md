---
id: L09
materia: M12
orden: 9
titulo: Alcance MVP y MoSCoW
horas: 5
semana: 3
lectura: "producto-saas fases"
evidencia: "srs-borrador alcance"
---

# L09 — Alcance MVP y MoSCoW

**~5 h · Semana 3**

## Objetivo

Priorizar Must/Should/Could/Won't para build de 4 semanas (auth, citas, clientes, admin).

## Por qué importa

Freeze evita MVP infinito.

## Conceptos

- MoSCoW.
- freeze.
- fuera de alcance.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tabla MoSCoW. Lista explícita: multi-tenant, billing, IA = Won't ahora.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l09 alcance-mvp-y-moscow"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | producto-saas.md | — |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. MoSCoW completo.
2. Won't documentado.
3. Fecha freeze propuesta.

## Errores comunes

- Todo es Must.
- Cambiar vertical.

## Siguiente

[L10 — Requisitos funcionales en SRS](L10-requisitos-funcionales-en-srs.md)
