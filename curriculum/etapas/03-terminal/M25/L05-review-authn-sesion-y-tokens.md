---
id: L05
materia: M25
orden: 5
titulo: Review authn — sesión y tokens
horas: 5.0
semana: 2
lectura: OWASP — Identity / Authorization testing
evidencia: projects/m25-ciber/review/authn.md
---

# L05 — Review authn — sesión y tokens

**~5 h · Semana 2**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/review/authn.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Documentar flujo login/logout/refresh y dónde vive tenant_id.

## Por qué empieza así

Cosmética CSS no salva un leak entre barberías.

Conceptos que debes poder explicar al cerrar:

- Authn vs authz
- tenant_id en sesión
- Tests de regresión

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP — Identity / Authorization testing_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo).

### 2. Dibuja el flujo authn (25–35 min)

En `projects/m25-ciber/review/authn.md` secciones: **Login**, **Sesión/JWT**, **Logout/refresh**.

Anota dónde vive `tenant_id` (claim, cookie, header, fila DB).

### 3. Inspecciona tokens reales (90–110 min)

Login como staff A en staging. Documenta (redactado):

```bash
# captura Set-Cookie o body de login — redacta signature/secret
curl -s -D - -o /tmp/login.json -X POST "$API/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"staff-a@example.test","password":"$PASS"}'
```

Tabla: cookie/token | HttpOnly | Secure | SameSite | expira | lleva tenant_id?

### 4. Amenazas y gaps (30–40 min)

≥4 amenazas (token en localStorage, refresh eterno, tenant_id solo en client, logout incompleto). Cada una: severidad + mitigación. Bitácora semana-02.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l05 review-authn-sesi-n-y-tokens"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP — Identity / Authorization testing | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/review/authn.md`.
2. Evidencia en ruta indicada.
3. Si es test: corre en CI o documenta por qué no aún.
4. Commit `docs(m25): l05 …` en el historial.

## Errores comunes

- 50 hallazgos menores y cero cross-tenant.
- tenant_id solo en frontend.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L06 — Review authz — roles staff vs admin](L06-review-authz-roles-staff-vs-admin.md)
