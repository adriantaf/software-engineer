---
id: L23
materia: M18
orden: 23
titulo: Deserialización y JSON peligroso
horas: 5.0
semana: 6
lectura: Deserialization + API hardening
evidencia: projects/m18-appsec/docs/json-trust.md
---

# L23 — Deserialización y JSON peligroso

**~5.0 h · Semana 6**

Node rara vez hace Java deserialization, pero prototype pollution y lógica sí.

## Objetivo

`projects/m18-appsec/docs/json-trust.md`: endpoints + schema; límite de body; ≥1 mejora commitada.

## Pasos

### 1. Inventario JSON bodies (40–50 min)

```bash
cd projects/m17-agenda-ops 2>/dev/null || cd <repo-Agenda-Ops>
rg -n "express\.json|bodyParser|z\.object|Joi\.|safeParse" -g '!node_modules' | head -40
cat > projects/m18-appsec/docs/json-trust.md <<'EOF'
# JSON trust
| Endpoint | Schema (zod/joi/…) | Límite body | Notas |
|----------|--------------------|-------------|-------|
| POST /auth/login | | | |
| POST /api/citas | | | |
EOF
```
### 2. Límite + rechazo campos extra (60–80 min)

```ts
app.use(express.json({ limit: "100kb" }));

// zod: strip o strict
const CitaInput = z.object({
  clienteId: z.string().uuid(),
  inicio: z.string().datetime(),
  notas: z.string().max(2000).optional(),
}).strict();
```

```bash
# Payload enorme → 413
python3 - <<'PY'
print('{"x":"' + ('a'*200000) + '"}')
PY | curl -s -o /dev/null -w "%{http_code}\n" -X POST localhost:3000/api/citas \
  -H 'content-type: application/json' -b /tmp/m18-cj --data-binary @-
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/docs/json-trust.md
git commit -m "fix(m18): l23 json trust limits"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Deserialization + API hardening | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Lista endpoints + validación (artefacto: `projects/m18-appsec/docs/json-trust.md`).
2. Límite tamaño body (artefacto: `projects/m18-appsec/docs/json-trust.md`).
3. Commit `docs(m18): L23 deserializacion-y-json-peligroso`.

## Errores comunes

- Aceptar cualquier JSON.
- Confiar en tipos TS solo compile-time.

## Siguiente

[L24 — Consolidar hallazgos semana 6 en P2](L24-consolidar-hallazgos-semana-6-en-p2.md)
