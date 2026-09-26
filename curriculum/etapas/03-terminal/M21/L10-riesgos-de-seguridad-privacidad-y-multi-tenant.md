---
id: L10
materia: M21
orden: 10
titulo: Riesgos de seguridad, privacidad y multi-tenant
horas: 5
semana: 3
lectura: "Hilo seguridad + OWASP ASVS (selecto)"
evidencia: "projects/m21-proyectos/riesgos.md sección seguridad"
---

# L10 — Riesgos de seguridad, privacidad y multi-tenant

**~5 h · Semana 3**

## Objetivo

Añadir ≥2 riesgos de seguridad/privacidad (IDOR cross-tenant, secretos, backup sin restore) con mitigaciones enlazadas a M18/M25.

## Por qué importa

Ignorar seguridad hasta M25 es exactamente el anti-patrón del plan.

## Conceptos

- IDOR.
- Secreto en repo.
- Restore no probado.
- Dependencia API LLM (M23).

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Extiende `projects/m21-proyectos/riesgos.md` con sección **Seguridad y privacidad** (≥2 filas).

Para cada uno: **cómo sabrías que ocurrió** y **evidencia de mitigación** (test, runbook, issue).

Cross-ref [hilo seguridad](../../hilos/seguridad.md) y issues M18 si existen.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l10 riesgos-de-seguridad-privacidad-y-multi-"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plan | ../../hilos/seguridad.md | ../M18-seguridad.md |
| Catálogo | Entrada M21 | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

1. ≥2 riesgos seguridad.
2. Evidencia mitigación citada.
3. Issue enlazado si aplica.

## Errores comunes

- Mitigación ‘confío en el framework’.
- Mezclar riesgo con bug puntual sin impacto.

## Siguiente

[L11 — Tablero vivo, sprints 3–4 y DoD en práctica](L11-tablero-vivo-sprints-3-4-y-dod-en-practica.md)
