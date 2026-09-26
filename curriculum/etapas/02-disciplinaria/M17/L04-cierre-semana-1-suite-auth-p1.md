---
id: L04
materia: M17
orden: 4
titulo: Cierre semana 1 — suite auth P1
horas: 5.0
semana: 1
lectura: Ficha M17 P1
evidencia: projects/m17-agenda-ops/tests/auth.test.ts
---

# L04 — Cierre semana 1 — suite auth P1

**~5.0 h · Semana 1**

P1 es la puerta del CRUD. Hoy consolidas la suite auth.

## Objetivo

≥6 tests auth verdes (register, login, me, logout) y README con comando reproducible.

## Pasos (hazlos en orden)

### 1. Completa logout (40–50 min)

Invalida sesión/cookie. Test: tras logout, `/me` → 401.

### 2. Suite y CI local (60–80 min)

```bash
npm test
```

Documenta en README: `npm test` / `npm run test:auth`. Enlaza P1 parcial.

### 3. Bitácora semana 1 (30 min)

`docs/semana-01.md`: commits, gaps, decisión auth.

### 4. Commit

`test(m17): l04 suite auth cierre p1`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 P1 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Suite auth verde (artefacto: `projects/m17-agenda-ops/tests/auth.test.ts`).
2. Logout documentado (artefacto: `projects/m17-agenda-ops/tests/auth.test.ts`).
3. P1 parcial README (artefacto: `projects/m17-agenda-ops/tests/auth.test.ts`).
4. Commit `docs(m17): L04 cierre-semana-1-suite-auth-p1`.

## Errores comunes

- Auth sin tests.
- Solo manual Postman.

## Siguiente

[L05 — Modelo de dominio citas, clientes y servicios](L05-modelo-de-dominio-citas-clientes-y-servicios.md)
