---
id: L08
materia: M17
orden: 8
titulo: Seeds demo y datos design partner
horas: 5
semana: 2
lectura: "Fixtures reproducibles"
evidencia: "projects/m17-agenda-ops/scripts/seed.ts"
---

# L08 — Seeds demo y datos design partner

**~5 h · Semana 2**

## Objetivo

Script seed con negocio piloto, owner, staff, citas ejemplo para demo.

## Por qué importa

Demo reproducible evita ‘en mi máquina sí’.

## Conceptos

- seed.
- demo.
- idempotencia.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

seed documentado en README. No PII real del partner en repo.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l08 seeds-demo-y-datos-design-partner"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| README | demo creds test | — |

## Hecho cuando

1. Seed corre.
2. README creds test.
3. Cierre semana 2.

## Errores comunes

- Datos reales en git.
- Seed no repetible.

## Siguiente

[L09 — Matriz de permisos owner y staff](L09-matriz-de-permisos-owner-y-staff.md)
