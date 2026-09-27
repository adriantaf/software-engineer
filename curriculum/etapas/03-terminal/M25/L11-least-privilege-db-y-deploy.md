---
id: L11
materia: M25
orden: 11
titulo: Least privilege DB y deploy
horas: 5.0
semana: 3
lectura: OWASP Configuration + Stripe webhooks docs
evidencia: projects/m25-ciber/hardening/least-privilege.md
---

# L11 — Least privilege DB y deploy

**~5 h · Semana 3**

El bug #1 a cazar es IDOR cross-tenant. Hoy entregas **`projects/m25-ciber/hardening/least-privilege.md`**. Sin ese artefacto en git, la lección no cuenta para el dominio de M25.

## Objetivo

Usuario DB no superuser; permisos CI mínimos.

## Por qué empieza así

Billing roto o secrets filtrados tumba el SaaS antes del primer cliente.

Conceptos que debes poder explicar al cerrar:

- Stripe signature
- Secrets manager / env
- Restore ≠ backup

## Pasos (hazlos en orden)

### 1. Lectura concreta de la fuente (40–60 min)

Abre [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) (o la sección citada) y lee: _OWASP Configuration + Stripe webhooks docs_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Vitrina (nombres de endpoint o activo).

### 2. Inventario de privilegios (25–35 min)

En `projects/m25-ciber/hardening/least-privilege.md`: rol DB app, rol CI deploy, quién puede `DROP`/`ALTER`.

Sin passwords.

### 3. Verifica usuario DB no-superuser (90–110 min)

En staging (o mirror), documenta:

```sql
-- corre como el rol de la app; pega solo el resultado
SELECT current_user, current_setting('is_superuser');
-- o \du en psql — sin passwords
```

Si es superuser: issue + migración a rol con grants mínimos (SELECT/INSERT/UPDATE/DELETE en schemas de app).

### 4. CI y deploy mínimos (30–40 min)

Lista tokens GitHub/Actions con scopes. Quita permisos write innecesarios o documenta por qué quedan. Bitácora semana-03.

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m25): l11 least-privilege-db-y-deploy"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP WSTG / Testing Guide | OWASP Configuration + Stripe webhooks docs | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M25](../../../bibliografia.md#m25-ciberseguridad-aplicada) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe el entregable: `projects/m25-ciber/hardening/least-privilege.md`.
2. Checklist ítem demostrado.
3. Sin valores de API keys.
4. Commit `docs(m25): l11 …` en el historial.

## Errores comunes

- Solo checklist teórico.
- Restore nunca probado.
- Marcar la lección en la UI sin archivo en git.

## Siguiente

[L12 — Backup y restore probado](L12-backup-y-restore-probado.md)
