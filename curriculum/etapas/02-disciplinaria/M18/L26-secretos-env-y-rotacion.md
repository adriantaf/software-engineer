---
id: L26
materia: M18
orden: 26
titulo: Secretos, .env y rotación
horas: 5.0
semana: 7
lectura: Secrets Management Cheat Sheet
evidencia: projects/m18-appsec/docs/rotacion-secretos.md
---

# L26 — Secretos, .env y rotación

**~5.0 h · Semana 7**

Secretos en git son incidentes. Inventario (sin valores) + plan de rotación.

## Objetivo

`projects/m18-appsec/docs/rotacion-secretos.md`: inventario, dónde viven, pasos rotar session secret / DB URL.

## Pasos

### 1. Busca secretos en historial (30–40 min)

```bash
git log -p --all -S 'DATABASE_URL' 2>/dev/null | head -20 || true
git ls-files | rg -i '\.env|credential|secret|\.pem' || true
# gitleaks / trufflehog si los tienes instalados
```
### 2. Inventario + rotación (70–90 min)

```bash
cat > projects/m18-appsec/docs/rotacion-secretos.md <<'EOF'
# Secretos y rotación
| Secreto | Dónde (local/staging) | En git? | Rotar cómo |
|---------|----------------------|---------|------------|
| DATABASE_URL | .env / PaaS | no | … |
| SESSION_SECRET | .env | no | reiniciar sesiones |
| SMTP_KEY | … | | |

## Pasos rotar SESSION_SECRET (staging)
1. Generar nuevo valor
2. Deploy
3. Invalidar sesiones previas
4. Verificar login
EOF
```

```bash
# Genera candidato (no lo commits)
openssl rand -hex 32
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/rotacion-secretos.md
git status   # .env no debe aparecer
git commit -m "docs(m18): l26 rotacion secretos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Secrets Management Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Inventario sin valores (artefacto: `projects/m18-appsec/docs/rotacion-secretos.md`).
2. grep historial ejecutado (artefacto: `projects/m18-appsec/docs/rotacion-secretos.md`).
3. Commit `docs(m18): L26 secretos-env-y-rotacion`.

## Errores comunes

- Pegar secretos en issue.
- Rotar sin probar logout.

## Siguiente

[L27 — Cabeceras de seguridad con Helmet o equivalente](L27-cabeceras-de-seguridad-con-helmet-o-equivalente.md)
