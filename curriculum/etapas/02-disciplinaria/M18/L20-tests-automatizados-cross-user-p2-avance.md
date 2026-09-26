---
id: L20
materia: M18
orden: 20
titulo: Tests automatizados cross-user (P2 avance)
horas: 5.0
semana: 5
lectura: Testing access control
evidencia: tests en repo producto + projects/m18-appsec/findings-table.md
---

# L20 — Tests automatizados cross-user (P2 avance)

**~5.0 h · Semana 5**

P2 pide hallazgo→fix→test; hoy consolidas access control.

## Objetivo

≥2 tests authz (cross-user + rol) + `projects/m18-appsec/findings-table.md` con ≥3 filas.

## Pasos

### 1. Fixture dos usuarios (30–40 min)

```ts
// tests/security/authz-cross-user.test.ts
async function login(email: string) { /* cookie jar / token */ }

it("B cannot read A's cita", async () => {
  const a = await login("a@test.local");
  const b = await login("b@test.local");
  const cita = await a.post("/api/citas", { /* … */ });
  const res = await b.get(`/api/citas/${cita.id}`);
  expect([403, 404]).toContain(res.status);
});

it("staff cannot patch settings", async () => {
  const staff = await login("staff@test.local");
  const res = await staff.patch("/api/settings", { tz: "UTC" });
  expect(res.status).toBe(403);
});
```
### 2. Corre tests + actualiza tabla (60–80 min)

```bash
npm test -- --testPathPattern=authz || npm test -- security
# Actualiza findings-table: 001–003 + rate limit
rg -n '^\|' projects/m18-appsec/findings-table.md
```
### 3. Commit (10 min)

```bash
git add -A && git commit -m "test(m18): l20 authz cross-user"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Testing access control | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥2 tests authz verdes (artefacto: `tests en repo producto`).
2. findings-table ≥3 filas (artefacto: `tests en repo producto`).
3. Commit `docs(m18): L20 tests-automatizados-cross-user-p2-avance`.

## Errores comunes

- Tests que mockean auth siempre true.
- Un solo usuario en tests.

## Siguiente

[L21 — SSRF: superficie en webhooks e integraciones](L21-ssrf-superficie-en-webhooks-e-integraciones.md)
