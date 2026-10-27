---
id: L27
materia: M18
orden: 27
titulo: Cabeceras de seguridad con Helmet o equivalente
horas: 5.0
semana: 7
lectura: Security Headers Cheat Sheet
evidencia: commit headers + captura curl
---

# L27 — Cabeceras de seguridad con Helmet o equivalente

**~5.0 h · Semana 7**

Headers baratos reducen XSS clickjacking y MIME sniffing.

## Objetivo

Helmet (o equiv) en la API/front; captura `curl -I` en evidencia.

## Pasos

### 1. Baseline headers (20–30 min)

```bash
curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-before.txt | rg -i 'x-|content-security|strict-transport|referrer|permissions'|| true
```
### 2. Activa Helmet (60–80 min)

```ts
import helmet from "helmet";
app.use(helmet({
  contentSecurityPolicy: false, // CSP en L28
  frameguard: { action: "deny" },
  noSniff: true,
  referrerPolicy: { policy: "no-referrer" },
}));
```

```bash
curl -sI localhost:3000/ | tee projects/m18-appsec/pocs/headers-after.txt
diff -u projects/m18-appsec/pocs/headers-before.txt projects/m18-appsec/pocs/headers-after.txt || true
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/pocs/headers-*.txt
git commit -m "fix(m18): l27 security headers"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Security Headers Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Headers visibles en staging (artefacto: `commit headers`).
2. Login sigue funcionando (artefacto: `commit headers`).
3. Commit `docs(m18): L27 cabeceras-de-seguridad-con-helmet-o-equivalente`.

## Errores comunes

- HSTS en localhost sin TLS.
- CSP rota todo sin reporte.

## Siguiente

[L28 — CSP básica sin romper Vitrina](L28-csp-basica-sin-romper-vitrina.md)
