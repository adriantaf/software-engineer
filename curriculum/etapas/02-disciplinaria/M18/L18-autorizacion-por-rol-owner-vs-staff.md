---
id: L18
materia: M18
orden: 18
titulo: Autorización por rol owner vs staff
horas: 5.0
semana: 5
lectura: Access Control Cheat Sheet
evidencia: projects/m18-appsec/docs/rbac-matrix.md
---

# L18 — Autorización por rol owner vs staff

**~5.0 h · Semana 5**

Vitrina distingue dueño y staff; la API debe hacerlo explícito.

## Objetivo

Matriz rol×recurso×acción en `projects/m18-appsec/docs/rbac-matrix.md` + ≥1 prueba manual de gap.

## Pasos

### 1. Matriz RBAC (50–60 min)

```bash
cat > projects/m18-appsec/docs/rbac-matrix.md <<'EOF'
# RBAC — Vitrina
| Recurso / acción | Owner | Staff | Anónimo |
|------------------|-------|-------|---------|
| Listar pedidos | ✓ | ✓ (alcance) | ✗ |
| Crear pedido | ✓ | ✓ | ✗ |
| Borrar cualquier pedido | ✓ | ? | ✗ |
| Configuración negocio | ✓ | ✗ | ✗ |
| Gestionar usuarios | ✓ | ✗ | ✗ |

## Gaps código vs SRS
- …
## Prueba manual
- Actor: staff · Acción: … · Resultado HTTP: …
EOF
```
### 2. Prueba staff vs owner (50–70 min)

```bash
curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-staff \
  -X PATCH localhost:3000/api/settings -H 'content-type: application/json' -d '{"tz":"UTC"}'
# esperado: 403
```

```ts
// guard ilustrativo
if (req.user.role !== "owner") return res.status(403).json({ error: "forbidden" });
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/rbac-matrix.md
git commit -m "docs(m18): l18 rbac matrix"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Access Control Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Matriz completa (artefacto: `projects/m18-appsec/docs/rbac-matrix.md`).
2. ≥1 prueba manual rol (artefacto: `projects/m18-appsec/docs/rbac-matrix.md`).
3. Commit `docs(m18): L18 autorizacion-por-rol-owner-vs-staff`.

## Errores comunes

- Un solo rol ‘admin’.
- 404 para esconder sin authz.

## Siguiente

[L19 — Rate limiting en login y endpoints sensibles](L19-rate-limiting-en-login-y-endpoints-sensibles.md)
