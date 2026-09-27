---
id: L24
materia: M17
orden: 24
titulo: Smoke test post-deploy
horas: 5.0
semana: 6
lectura: Checklist smoke
evidencia: projects/m17-vitrina/docs/smoke-test.md
---

# L24 — Smoke test post-deploy

**~5.0 h · Semana 6**

Detecta config rota antes de la demo.

## Objetivo

Script o checklist: register/login/crear pedido en staging.

## Conceptos clave

- smoke
- staging
- regresión manual

## Pasos (hazlos en orden)

### 1. Smoke script (60–80 min)

```bash
cat > projects/m17-vitrina/docs/smoke-test.md << 'EOF'
# Smoke post-deploy
1. GET /health → 200
2. POST /auth/login (user demo staging)
3. POST /pedidos → 201
4. GET /pedidos → incluye la pedido
Fecha: YYYY-MM-DD  Resultado: OK/FAIL
EOF
```

```bash
BASE=https://TU-STAGING.example
curl -sS "$BASE/health"
curl -sS -c /tmp/st.ck -X POST "$BASE/auth/login" -H 'content-type: application/json' \
  -d '{"email":"owner@demo.local","password":"FROM_SECRET_MANAGER"}'
```

### 2. Registra resultado + commit (30 min)

```bash
git add projects/m17-vitrina/docs/smoke-test.md
git commit -m "docs(m17): L24 smoke test post-deploy"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Checklist smoke | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/smoke-test.md` con health+login+pedido y fecha/resultado.
2. Commit `docs(m17): L24 smoke-test-post-deploy`.

## Errores comunes

- Smoke sin fecha/resultado.
- Password de staging pegado en markdown.

## Siguiente

[L25 — Mapa OWASP Top 10 en el piloto](L25-mapa-owasp-top-10-en-el-piloto.md)
