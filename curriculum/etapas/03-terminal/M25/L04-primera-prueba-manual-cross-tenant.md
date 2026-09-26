---
id: L04
materia: M25
orden: 4
titulo: Primera prueba manual cross-tenant
horas: 5.0
semana: 1
lectura: OWASP Testing Guide — information gathering
evidencia: projects/m25-ciber/aislamiento/prueba-manual-01.md
---

# L04 — Primera prueba manual cross-tenant

**~5 h · Semana 1**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/aislamiento/prueba-manual-01.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Intentar leer recurso del tenant B autenticado como A; documentar resultado.

## Por qué empieza así

M25 capa C: el bug #1 en SaaS es IDOR cross-tenant.

Conceptos que debes poder explicar al cerrar:

- IDOR
- 403 vs 404
- Evidencia reproducible

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Testing Guide — information gathering_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Prepara IDs de prueba (20–30 min)

Usa tenants A/B de L03. Anota en `aislamiento/prueba-manual-01.md`: `tenant_a_id`, `tenant_b_id`, `cita_b_id`, usuario A.

### 3. Prueba manual IDOR (90–110 min)

Autenticado como A, pide recurso de B (GET cita / cliente). Documenta:

```bash
# ejemplo — adapta a tu API; redacta tokens
curl -s -o /tmp/a.json -w "%{http_code}" -H "Authorization: Bearer $TOKEN_A" \
  "$API/citas/$CITA_B_ID"
```

Pega status + fragmento de body **redactado**. Espera 403/404; si 200 con datos de B → hallazgo crítico.

### 4. Clasifica resultado (30–40 min)

Sección **Resultado**: PASS / FAIL. Si FAIL, abre issue y enlázalo. No “arregles en silencio” sin evidencia.

### 5. Commit atómico (15 min)

```bash
git add projects/ curriculum/etapas/03-terminal/ || git add projects/
git status
git commit -m "docs(m25): l04 primera-prueba-manual-cross-tenant"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Testing Guide — information gathering | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/aislamiento/prueba-manual-01.md`.
2. Sin secretos en markdown.
3. Conexión Agenda Ops escrita en bitácora.
4. Commit `docs(m25): l04 …` en el historial.

## Errores comunes

- Inventario sin staging.
- Probar solo en localhost sin deploy.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L05 — Review authn — sesión y tokens](L05-review-authn-sesion-y-tokens.md)
