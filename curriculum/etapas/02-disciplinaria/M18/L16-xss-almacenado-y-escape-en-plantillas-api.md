---
id: L16
materia: M18
orden: 16
titulo: XSS almacenado y escape en plantillas/API
horas: 5.0
semana: 4
lectura: DOM XSS + stored XSS
evidencia: commit fix + findings/002 actualizado
---

# L16 — XSS almacenado y escape en plantillas/API

**~5.0 h · Semana 4**

El CRM guarda texto que vuelve a listarse; ahí vive el stored XSS.

## Objetivo

Fix escape/sanitización; actualizar finding; filas SQLi+XSS en `projects/m18-appsec/findings-table.md`.

## Pasos

### 1. Stored en notas de cita (50–60 min)

```bash
# Crea cita con payload en notas (cuenta prueba)
curl -s -X POST localhost:3000/api/citas -H 'content-type: application/json' -b /tmp/m18-cj \
  -d '{"clienteId":"…","inicio":"2026-01-02T10:00:00Z","notas":"<img src=x onerror=alert(1)>"}'
# Lista y verifica escape en HTML
```
### 2. Fix + test (60–80 min)

Usa textContent / escape del framework; evita `dangerouslySetInnerHTML` con input usuario.

```ts
// API: devolver texto; el front escapa al render
// Test:
it("escapes stored XSS in notas", async () => {
  const payload = "<script>alert(1)</script>";
  await createCita({ notas: payload });
  const html = await renderListaCitas();
  expect(html).not.toContain("<script>");
  expect(html).toContain("&lt;script&gt;") // o equivalente escapado
});
```
### 3. Tabla P2 (20–30 min)

```bash
cat > projects/m18-appsec/findings-table.md <<'EOF'
# Findings P2
| ID | OWASP | PoC | Commit fix | Test |
|----|-------|-----|------------|------|
| 001 | A03 | findings/001-sqli.md | | |
| 002 | A03/XSS | findings/002-xss-reflected.md | | |
EOF
git add -A && git commit -m "fix(m18): l16 xss stored escape"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | DOM XSS + stored XSS | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥2 filas en findings-table (artefacto: `commit fix`).
2. Test o verificación manual repetible (artefacto: `commit fix`).
3. Commit `docs(m18): L16 xss-almacenado-y-escape-en-plantillas-api`.

## Errores comunes

- strip_tags inventado.
- innerHTML con input usuario.

## Siguiente

[L17 — IDOR en citas y recursos por ID](L17-idor-en-citas-y-recursos-por-id.md)
