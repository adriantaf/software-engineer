---
id: L15
materia: M15
orden: 15
titulo: Política bug → test el mismo día
horas: 5
semana: 4
lectura: "Regresión documentada"
evidencia: "projects/m15-calidad/regresiones.md"
---

# L15 — Política bug → test el mismo día

**~5 h · Semana 4**

## Objetivo

Documentar un bug real o simulado y el test añadido el mismo día.

## Por qué importa

Esta regla separa equipos serios de demos frágiles.

## Conceptos

- regresión.
- política.
- postmortem ligero.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Entrada en `regresiones.md`: síntoma, causa, test, commit hash.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m15): l15 politica-bug-test-el-mismo-dia"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Código limpio | pruebas | — |

## Hecho cuando

1. regresiones.md con 1 caso.
2. Test asociado.
3. Commit.

## Errores comunes

- Bug sin test.
- Solo fix manual.

## Siguiente

[L16 — Cierre M15 — pipeline, coverage dominio, dominio](L16-cierre-m15-pipeline-coverage-dominio-dominio.md)
