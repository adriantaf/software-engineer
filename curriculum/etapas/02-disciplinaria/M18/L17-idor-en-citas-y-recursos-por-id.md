---
id: L17
materia: M18
orden: 17
titulo: IDOR en citas y recursos por ID
horas: 5.0
semana: 5
lectura: OWASP A01 Broken Access Control
evidencia: projects/m18-appsec/findings/003-idor.md
---

# L17 — IDOR en citas y recursos por ID

**~5.0 h · Semana 5**

Ocultar botones no basta: autorización server-side.

## Objetivo

PoC cross-user en `projects/m18-appsec/findings/003-idor.md` con dos cuentas de prueba.

## Pasos

### 1. Dos usuarios de prueba (20–30 min)

```bash
# Login A y B; guarda cookies separadas
curl -c /tmp/m18-a -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"a@test.local","password":"***"}' -o /dev/null
curl -c /tmp/m18-b -s -X POST localhost:3000/auth/login -H 'content-type: application/json' \
  -d '{"email":"b@test.local","password":"***"}' -o /dev/null
```
### 2. PoC IDOR (60–80 min)

A crea cita → B intenta `GET/PUT /api/citas/:id`.

```bash
CITA_ID=…  # id creado por A
curl -s -o /dev/null -w "%{http_code}\n" -b /tmp/m18-b localhost:3000/api/citas/$CITA_ID
# esperado tras fix: 403 o 404 (no 200 con datos de A)

cat > projects/m18-appsec/findings/003-idor.md <<'EOF'
# Finding 003 — IDOR
- Ruta: GET/PUT /api/citas/:id
- Pasos:
- Impacto:
- Estado:
EOF
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/003-idor.md
git commit -m "docs(m18): l17 poc idor"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | OWASP A01 Broken Access Control | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. PoC con dos usuarios (artefacto: `projects/m18-appsec/findings/003-idor.md`).
2. Impacto descrito (artefacto: `projects/m18-appsec/findings/003-idor.md`).
3. Commit `docs(m18): L17 idor-en-citas-y-recursos-por-id`.

## Errores comunes

- Probar en datos de design partner real.
- Autorización solo en front.

## Siguiente

[L18 — Autorización por rol owner vs staff](L18-autorizacion-por-rol-owner-vs-staff.md)
