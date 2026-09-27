---
id: L13
materia: M18
orden: 13
titulo: "SQLi: reproducir en tu propia API"
horas: 5.0
semana: 4
lectura: OWASP A03 Injection + SQLi Prevention
evidencia: projects/m18-appsec/findings/001-sqli.md
---

# L13 — SQLi: reproducir en tu propia API

**~5.0 h · Semana 4**

Solo contra tu API. P2 empieza con hallazgo real; SQLi sigue vivo en ORMs mal usados.

## Objetivo

PoC o “no reproducible con ORM” en `projects/m18-appsec/findings/001-sqli.md` (sin PII real).

## Pasos

### 1. Caza concatenación SQL (50–60 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "\$\{|query\(|\.query\(|execute\(|raw\(|sql`" -g '!node_modules' | head -50
rg -n "SELECT.*\+|WHERE.*\+" -g '*.ts' -g '*.js' | head -20 || true
```
### 2. PoC controlada (60–80 min)

Cuenta de prueba. Payload en búsqueda clientes/citas. **No** `DROP` en staging compartido.

```bash
mkdir -p projects/m18-appsec/findings projects/m18-appsec/pocs
cat > projects/m18-appsec/findings/001-sqli.md <<'EOF'
# Finding 001 — SQLi
- Endpoint:
- Payload (ejemplo): `' OR '1'='1`
- Respuesta / impacto:
- ¿ORM parametrizado? evidencia:
- PII: ninguna en este reporte
EOF
# Ejemplo de prueba (ajusta query param)
curl -sG "localhost:3000/api/clientes" --data-urlencode "q=' OR '1'='1" | head -c 400
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/001-sqli.md
git commit -m "docs(m18): l13 poc sqli"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A03 Injection + SQLi Prevention | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Finding documentado o prueba de mitigación (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
2. Solo tu entorno (artefacto: `projects/m18-appsec/findings/001-sqli.md`).
3. Commit `docs(m18): L13 sqli-reproducir-en-tu-propia-api`.

## Errores comunes

- SQLi en producción de terceros.
- Drop table en staging compartido.

## Siguiente

[L14 — Mitigar SQLi: queries parametrizadas y permisos DB](L14-mitigar-sqli-queries-parametrizadas-y-permisos-db.md)
