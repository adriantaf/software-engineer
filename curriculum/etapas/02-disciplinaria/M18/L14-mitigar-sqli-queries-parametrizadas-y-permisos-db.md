---
id: L14
materia: M18
orden: 14
titulo: 'Mitigar SQLi: queries parametrizadas y permisos DB'
horas: 5
semana: 4
lectura: SQLi Prevention Cheat Sheet
evidencia: commit fix + test en repo producto
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Fix parametrizado + test de regresión; `001-sqli.md` →
      Cerrado con commit hash.


      Hallazgo sin fix no cuenta para P2.
  - id: s2
    tipo: ejemplo
    titulo: 1. Parametriza la query
    xp: 10
    cuerpo: |-
      ```ts
      // MAL
      // db.query(`SELECT * FROM clientes WHERE nombre LIKE '%${q}%'`)

      // BIEN (pg)
      await db.query(
        "SELECT id, nombre, telefono FROM clientes WHERE nombre ILIKE $1 LIMIT 50",
        [`%${q}%`],
      );
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Mitigar SQLi: queries parametrizadas y permisos DB" como
      hecha, ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: commit fix + test en repo producto
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Escapar manualmente sin
      parametrizar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Fix parametrizado + test de regresión; `001-sqli.md` → Cerrado con
          commit hash.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Test de regresión
    xp: 10
    cuerpo: "```ts\n// tests/security/sqli-search.test.ts\nit(\"rejects or safely handles SQLi-like search\", async () => {\n  const res = await api.get(\"/api/clientes\", { q: \"' OR '1'='1\" });\n  expect(res.status).not.toBe(500);\n  expect(String(res.body)).not.toMatch(/syntax error|pg_|\bSQL\b/i);\n});\n```\n\n```bash\nnpm test -- --testPathPattern=sqli || npm test -- security\n```"
  - id: s7
    tipo: ejemplo
    titulo: 3. Cierra finding
    xp: 10
    cuerpo: >-
      ```bash

      printf "\n## Estado: Cerrado\n- Commit fix: \n- Test: \n" >>
      projects/m18-appsec/findings/001-sqli.md

      git add -A && git commit -m "fix(m18): l14 sqli parametrized"

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Test de regresión (artefacto: `commit fix`).'
      - 'Finding actualizado a Cerrado (artefacto: `commit fix`).'
      - >-
        Commit `docs(m18): L14
        mitigar-sqli-queries-parametrizadas-y-permisos-d`.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
