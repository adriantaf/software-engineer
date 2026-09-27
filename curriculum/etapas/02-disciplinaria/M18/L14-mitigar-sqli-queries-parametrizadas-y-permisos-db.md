---
id: L14
materia: M18
orden: 14
titulo: "Mitigar SQLi: queries parametrizadas y permisos DB"
horas: 5.0
semana: 4
lectura: SQLi Prevention Cheat Sheet
evidencia: commit fix + test en repo producto
---

# L14 — Mitigar SQLi: queries parametrizadas y permisos DB

**~5.0 h · Semana 4**

Hallazgo sin fix no cuenta para P2.

## Objetivo

Fix parametrizado + test de regresión; `001-sqli.md` → Cerrado con commit hash.

## Pasos

### 1. Parametriza la query (60–80 min)

```ts
// MAL
// db.query(`SELECT * FROM clientes WHERE nombre LIKE '%${q}%'`)

// BIEN (pg)
await db.query(
  "SELECT id, nombre, telefono FROM clientes WHERE nombre ILIKE $1 LIMIT 50",
  [`%${q}%`],
);
```

```sql
-- Usuario app sin DDL (idea)
-- CREATE ROLE agenda_app LOGIN PASSWORD '...';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO agenda_app;
-- (sin CREATE/DROP)
```
### 2. Test de regresión (40–50 min)

```ts
// tests/security/sqli-search.test.ts
it("rejects or safely handles SQLi-like search", async () => {
  const res = await api.get("/api/clientes", { q: "' OR '1'='1" });
  expect(res.status).not.toBe(500);
  expect(String(res.body)).not.toMatch(/syntax error|pg_|SQL/i);
});
```

```bash
npm test -- --testPathPattern=sqli || npm test -- security
```
### 3. Cierra finding (20 min)

```bash
printf "\n## Estado: Cerrado\n- Commit fix: \n- Test: \n" >> projects/m18-appsec/findings/001-sqli.md
git add -A && git commit -m "fix(m18): l14 sqli parametrized"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | SQLi Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Test de regresión (artefacto: `commit fix`).
2. Finding actualizado a Cerrado (artefacto: `commit fix`).
3. Commit `docs(m18): L14 mitigar-sqli-queries-parametrizadas-y-permisos-d`.

## Errores comunes

- Escapar manualmente sin parametrizar.
- Silenciar error sin arreglar query.

## Siguiente

[L15 — XSS reflejado en campos de cliente o búsqueda](L15-xss-reflejado-en-campos-de-cliente-o-busqueda.md)
