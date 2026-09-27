---
id: L15
materia: M18
orden: 15
titulo: XSS reflejado en campos de cliente o búsqueda
horas: 5.0
semana: 4
lectura: XSS Prevention Cheat Sheet
evidencia: projects/m18-appsec/findings/002-xss-reflected.md
---

# L15 — XSS reflejado en campos de cliente o búsqueda

**~5.0 h · Semana 4**

XSS roba sesiones si las cookies son legibles por JS.

## Objetivo

PoC reflejado en `projects/m18-appsec/findings/002-xss-reflected.md` (solo tu cuenta de prueba; sin exfiltración externa).

## Pasos

### 1. Localiza render de input (30–40 min)

```bash
cd projects/m17-vitrina 2>/dev/null || cd <repo-Agenda-Ops>
rg -n 'dangerouslySetInnerHTML|innerHTML|\$\{.*q|searchParams|mensaje' -g '!node_modules' | head -30
```
### 2. PoC local (60–80 min)

Payloads: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`. Solo impacto local.

```bash
cat > projects/m18-appsec/findings/002-xss-reflected.md <<'EOF'
# Finding 002 — XSS reflejado
- Pantalla / query:
- Payload:
- ¿Ejecutó en el navegador? sí/no
- Contexto (HTML text / attr / JS):
EOF
# Ejemplo
curl -sG "localhost:3000/clientes" --data-urlencode "q=<script>alert(1)</script>" | rg -n 'script|onerror' | head
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/findings/002-xss-reflected.md
git commit -m "docs(m18): l15 poc xss reflected"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | XSS Prevention Cheat Sheet | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. PoC documentada (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
2. Contexto identificado (artefacto: `projects/m18-appsec/findings/002-xss-reflected.md`).
3. Commit `docs(m18): L15 xss-reflejado-en-campos-de-cliente-o-busqueda`.

## Errores comunes

- XSS persistente en prod sin aviso.
- Confiar en ‘React escapa todo’.

## Siguiente

[L16 — XSS almacenado y escape en plantillas/API](L16-xss-almacenado-y-escape-en-plantillas-api.md)
