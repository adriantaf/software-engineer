---
id: L04
materia: M17
orden: 4
titulo: Cierre semana 1 — suite auth P1
horas: 5.0
semana: 1
lectura: Ficha M17 P1
evidencia: projects/m17-vitrina/tests/auth.test.ts
---

# L04 — Cierre semana 1 — suite auth P1

**~5.0 h · Semana 1**

P1 es puerta para todo CRUD.

## Objetivo

Consolidar tests auth (register, login, me, logout) y marcar P1 parcial en README.

## Conceptos clave

- P1
- suite auth
- logout

## Pasos (hazlos en orden)

### 1. Consolida suite auth (80–100 min)

En `projects/m17-vitrina/tests/auth.test.ts` (o equivalente) cubre: register, login, me, logout, 401, password malo. Mínimo **6** tests.

```ts
// esqueleto
it("login → me 200", async () => { /* ... */ });
it("me sin cookie → 401", async () => { /* ... */ });
it("logout invalida sesión", async () => { /* ... */ });
```

### 2. Documenta comando en README (20–30 min)

```bash
npm test
# anota en README la línea exacta que deja P1 verde
```

Marca P1 parcial en el checklist del README de `projects/m17-vitrina/`.

### 3. Commit cierre semana 1 (15 min)

```bash
git add projects/m17-vitrina
git commit -m "test(m17): L04 suite auth P1 semana 1"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Ficha M17 P1 | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe `projects/m17-vitrina/tests/auth.test.ts` (o equiv.) con ≥6 tests verdes.
2. README documenta el comando exacto `npm test`.
3. Checklist P1 parcial marcado en README (artefacto: `projects/m17-vitrina/tests/auth.test.ts`).
4. Commit `docs(m17): L04 cierre-semana-1-suite-auth-p1`.

## Errores comunes

- Dar P1 por hecho solo con Postman manual.
- Suite <6 casos o flaky.

## Siguiente

[L05 — Modelo de dominio pedidos, clientes y servicios](L05-modelo-de-dominio-pedidos-clientes-y-servicios.md)
