---
id: L04
materia: M17
orden: 4
titulo: Cierre semana 1 — suite auth P1
horas: 5
semana: 1
lectura: "Ficha M17 P1"
evidencia: "projects/m17-agenda-ops/tests/auth.test.ts"
---

# L04 — Cierre semana 1 — suite auth P1

**~5 h · Semana 1**

## Objetivo

Consolidar tests auth (register, login, me, logout) y marcar P1 parcial en README.

## Por qué importa

P1 es puerta para todo CRUD.

## Conceptos

- P1.
- suite auth.
- logout.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥6 tests auth. README comando `npm test`. Commit cierre semana 1.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m17): l04 cierre-semana-1-suite-auth-p1"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M17-aplicaciones-web.md | m15 CI |

## Hecho cuando

1. Suite auth verde.
2. Logout documentado.
3. P1 parcial README.

## Errores comunes

- Auth sin tests.
- Solo manual Postman.

## Siguiente

[L05 — Modelo de dominio citas, clientes y servicios](L05-modelo-de-dominio-citas-clientes-y-servicios.md)
