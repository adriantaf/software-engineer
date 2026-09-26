---
id: L03
materia: M21
orden: 3
titulo: Roadmap trimestral alineado a producto-saas
horas: 5
semana: 1
lectura: "producto-saas.md — piloto → tenants → billing"
evidencia: "projects/m21-proyectos/roadmap-trimestre.md"
---

# L03 — Roadmap trimestral alineado a producto-saas

**~5 h · Semana 1**

## Objetivo

Redactar roadmap de un trimestre con 3–5 objetivos medibles de Agenda Ops (multi-tenant, staging estable, trials, handoff M23).

## Por qué importa

P1 exige un documento que un mentor pueda cuestionar; debe reflejar [producto-saas]({PS}), no features al azar.

## Conceptos

- Outcome vs output.
- Dependencia M22/M26.
- Design partner.
- Corte explícito (MoSCoW).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

En `projects/m21-proyectos/roadmap-trimestre.md`:

- **Visión 90 días** (3–5 bullets).
- Tabla objetivos: **qué**, **por qué ahora**, **métrica**, **issue/milestone** enlazado.
- Sección **No haremos este trimestre** (≥3 ítems) para combatir scope creep.

Relee [producto-saas.md](../../../producto-saas.md) y marca qué objetivo habilita trials comerciales y qué habilita FAQ por tenant.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l03 roadmap-trimestral-alineado-a-producto-s"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../../producto-saas.md | ../M21-admin-proyectos.md |

## Hecho cuando

1. roadmap con 3–5 objetivos.
2. Tabla con métricas.
3. Sección ‘no haremos’.

## Errores comunes

- 40 features sin orden.
- Roadmap sin enlace a milestones.

## Siguiente

[L04 — Backlog refinado y criterios de aceptación](L04-backlog-refinado-y-criterios-de-aceptacion.md)
