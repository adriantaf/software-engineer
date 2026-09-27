---
id: L03
materia: M18
orden: 3
titulo: STRIDE aplicado al SaaS de menú/pedidos
horas: 5.0
semana: 1
lectura: STRIDE cheat sheet (una categoría por componente)
evidencia: projects/m18-appsec/stride-matrix.md
---

# L03 — STRIDE aplicado al SaaS de menú/pedidos

**~5.0 h · Semana 1**

La matriz obliga a nombrar amenazas antes de buscar exploits al azar.

## Objetivo

Matriz STRIDE ≥4×6 en `projects/m18-appsec/stride-matrix.md` (login, pedidos, admin) con ≥3 amenazas priorizadas.

## Pasos

### 1. Plantilla STRIDE (25–35 min)

```bash
cat > projects/m18-appsec/stride-matrix.md <<'EOF'
# Matriz STRIDE — Vitrina

| Componente | S | T | R | I | D | E |
|------------|---|---|---|---|---|---|
| Login | | | | | | |
| Lista pedidos | | | | | | |
| Detalle pedido | | | | | | |
| Admin usuarios | | | | | | |
EOF
```
### 2. Relleno del dominio (90–110 min)

Frases concretas (no “hackeo”). Ejemplo Login/Spoofing: “fuerza bruta o credenciales robadas”. Incluye IDOR en detalle pedido e XSS en notas.

```markdown
| Componente | S | T | I |
|------------|---|---|---|
| Login | Fuerza bruta | Tamper cookie | Leak en error |
| Detalle pedido | — | PUT sin authz | IDOR lee notas |
```
### 3. Prioriza 3 celdas (30 min)

Marca las 3 amenazas de las semanas 2–5. Enlaza `threat-model-v0.md`.

```bash
printf "\n## Prioridades (rojas)\n1. ...\n2. ...\n3. ...\n" >> projects/m18-appsec/stride-matrix.md
```
### 4. Commit (10 min)

```bash
git add projects/m18-appsec/stride-matrix.md
git commit -m "docs(m18): l03 stride crm pedidos"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | STRIDE cheat sheet (una categoría por componente) | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Matriz ≥4 filas × 6 columnas (artefacto: `projects/m18-appsec/stride-matrix.md`).
2. ≥3 amenazas priorizadas (artefacto: `projects/m18-appsec/stride-matrix.md`).
3. Commit `docs(m18): L03 stride-aplicado-al-crm-de-pedidos`.

## Errores comunes

- Copiar tabla de blog sin adaptar.
- Dejar celdas vacías con ‘N/A’ en todo.

## Siguiente

[L04 — Threat model v0 y lectura OWASP Top 10](L04-threat-model-v0-y-lectura-owasp-top-10.md)
