---
id: L21
materia: M18
orden: 21
titulo: "SSRF: superficie en webhooks e integraciones"
horas: 5.0
semana: 6
lectura: SSRF Prevention Cheat Sheet
evidencia: projects/m18-appsec/findings/004-ssrf.md
---

# L21 — SSRF: superficie en webhooks e integraciones

**~5.0 h · Semana 6**

Aun sin feature URL, documentar el control evita sorpresas en M26.

## Objetivo

Doc SSRF + allowlist en `projects/m18-appsec/findings/004-ssrf.md`. Sin escanear terceros ni metadata cloud en prod.

## Pasos

### 1. Busca fetch server-side (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'fetch\(|axios\.|got\(|request\(|http\.get' -g '!node_modules' | head -40
```
### 2. Diseño / PoC aislada (70–90 min)

Si no hay feature: simula diseño. Si hay: prueba URL interna **solo en staging aislado**.

```bash
cat > projects/m18-appsec/findings/004-ssrf.md <<'EOF'
# Finding 004 — SSRF (superficie)
## ¿Hay URL server-side hoy?
- webhook / import / avatar: sí/no · ruta:

## Riesgo ilustrativo
`http://169.254.169.254/` (metadata) — **no probar en cloud compartido**

## Allowlist propuesta
- hosts: `hooks.stripe.com`, …
- schemata: https only
- bloqueo: link-local, RFC1918, localhost

## Estado
- N/A feature | Mitigado | Abierto
EOF
```

```ts
function assertSafeUrl(raw: string) {
  const u = new URL(raw);
  if (u.protocol !== "https:") throw new Error("scheme");
  const allow = new Set(["hooks.example.com"]);
  if (!allow.has(u.hostname)) throw new Error("host");
}
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/004-ssrf.md
git commit -m "docs(m18): l21 ssrf superficie"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | SSRF Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Doc SSRF con allowlist (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
2. Riesgo nombrado (artefacto: `projects/m18-appsec/findings/004-ssrf.md`).
3. Commit `docs(m18): L21 ssrf-superficie-en-webhooks-e-integraciones`.

## Errores comunes

- curl a metadata cloud en prod.
- SSRF ‘para probar AWS’ en cuenta ajena.

## Siguiente

[L22 — Subida de archivos segura](L22-subida-de-archivos-segura.md)
