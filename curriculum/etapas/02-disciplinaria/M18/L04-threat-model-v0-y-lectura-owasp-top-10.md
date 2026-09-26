---
id: L04
materia: M18
orden: 4
titulo: Threat model v0 y lectura OWASP Top 10
horas: 5.0
semana: 1
lectura: OWASP Top 10 (2021) — lectura completa en español
evidencia: projects/m18-appsec/owasp-top10-map.md
---

# L04 — Threat model v0 y lectura OWASP Top 10

**~5.0 h · Semana 1**

Cierras la semana 1 con backlog de riesgo alineado a la industria.

## Objetivo

Mapa Top 10 en `projects/m18-appsec/owasp-top10-map.md` + `threat-model-v0.md` con riesgo residual semana 1.

## Pasos

### 1. Lectura Top 10 (40–50 min)

Lee OWASP Top 10 (2021) ES. Anota A01, A03, A07 como foco M18.

```bash
curl -sI https://owasp.org/Top10/es/ | head -5
```
### 2. Mapa 10 filas (70–90 min)

```bash
cat > projects/m18-appsec/owasp-top10-map.md <<'EOF'
# OWASP Top 10 → Agenda Ops

| Id | Ejemplo Agenda Ops | Mitigación | Semana |
|----|--------------------|------------|--------|
| A01 | GET /api/citas/:id cross-user | authz owner | 5 |
| A02 | secretos en repo | .env + rotación | 7 |
| A03 | búsqueda concat SQL | params/ORM | 4 |
| A04 | sin rate limit login | 429 | 5 |
| A05 | cookies sin flags | Secure/HttpOnly | 3 |
| A06 | deps vulnerables | npm audit | 7 |
| A07 | hash débil / sesión | bcrypt + rotate | 2 |
| A08 | integridad build | CI firmada (idea) | 8 |
| A09 | logs sin retención | política mínima | 8 |
| A10 | SSRF webhook futuro | allowlist | 6 |
EOF
```
### 3. Cierra threat-model-v0 (25–35 min)

Sección **Riesgo residual semana 1** (3 bullets). Confirma P1 tras semana 2 auth.

```bash
printf "\n## Riesgo residual semana 1\n- Auth aún no endurecida\n- Access control por verificar\n- Deps sin audit\n" >> projects/m18-appsec/threat-model-v0.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/owasp-top10-map.md projects/m18-appsec/threat-model-v0.md
git commit -m "docs(m18): l04 threat model v0 owasp"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP Top 10 (2021) — lectura completa en español | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Mapa 10 filas mínimo (artefacto: `projects/m18-appsec/owasp-top10-map.md`).
2. threat-model-v0 actualizado (artefacto: `projects/m18-appsec/owasp-top10-map.md`).
3. Commit `docs(m18): L04 threat-model-v0-y-lectura-owasp-top-10`.

## Errores comunes

- Marcar ‘no aplica’ en todo.
- Atacar sitios que no controlas.

## Siguiente

[L05 — Inventario de autenticación actual](L05-inventario-de-autenticacion-actual.md)
