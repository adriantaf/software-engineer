---
id: L32
materia: M17
orden: 32
titulo: Cierre M17 — evidencias, dominio y handoff M19
horas: 5
semana: 8
lectura: "Ficha M17 criterios dominio"
evidencia: "projects/m17-agenda-ops/docs/nota-cierre-m17.md"
---

# L32 — Cierre M17 — evidencias, dominio y handoff M19

**~5 h · Semana 8**

## Objetivo

Auditar P1–P3, proyecto piloto, criterios dominio, README final y handoff deploy M19.

## Por qué importa

Cierras la materia más densa del plan disciplinario.

## Conceptos

- cierre.
- handoff M19.
- dominio.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

nota-cierre-m17.md. README con URLs, tests, ADR, checklist. Commit `docs(m17): cierre materia`.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l32 cierre-m17-evidencias-dominio-y-handoff-"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M17-aplicaciones-web.md | ../M19-nube-devops.md |
| Catálogo | Entrada M17 | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

1. P1–P3 verificados.
2. HTTPS demo.
3. Criterios dominio.
4. Handoff M19.

## Errores comunes

- Marcar completo sin deploy.
- Auth solo front.
